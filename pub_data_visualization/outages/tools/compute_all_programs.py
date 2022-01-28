
import numpy as np
import pandas as pd
#
from ... import global_var, production_capacity
    
def compute_all_programs(df_outage,
                         list_plants = None,
                         ):
    """
        Computes the availability programs from the unavailabilty files
        for each production asset at the different publication dates.
 
        :param df_outage: The outages dataframe
        :param list_plants: The list of production assets to consider
        :type df_outage: pd.DataFrame
        :type list_plants: list of strings
        :return: A dictionary of the availability programs and
                 the problematic publications found
        :rtype: (dict, dict)
    """  
    
    try:
        capacity_end = production_capacity.unit.load(source   = global_var.data_source_capacity_rte,
                                                     map_code = 'FR',
                                                     )
        capacity_end = {k:v
                        for ii, (k, v) in capacity_end[[global_var.unit_name,
                                                        global_var.capacity_end_date_local,
                                                        ]].iterrows()
                        if bool(v)
                        }
    except FileNotFoundError:
        capacity_end = {}
        
    ### Compute programs
    if list_plants is None:
        list_plants = sorted(set((df_outage[global_var.unit_name])))
    dikt_programs         = {}
    dikt_bad_publications = {}
    for ii, unit_name in enumerate(list_plants):
        print('\rCompute program - {0:3}/{1:3} - {2:20}'.format(ii+1,
                                                                len(list_plants),
                                                                unit_name,
                                                                ),
              end = '',
              )
        df_unit = df_outage.loc[df_outage[global_var.unit_name] == unit_name]
        dikt_programs[unit_name], dikt_bad_publications[unit_name] = compute_program(df_unit,
                                                                                     capacity_end_date = capacity_end.get(unit_name),
                                                                                     )
    print()
    dikt_bad_publications = {k:v
                             for k, v in dikt_bad_publications.items()
                             if len(v) > 0
                             }
            
    return dikt_programs, dikt_bad_publications

###############################################################################

def compute_program(dg,
                    capacity_end_date = None,
                    ):
    """
        Computes the availability programs
        for one asset asset at the different publication dates.
 
        :param dg: The outages dataframe for the considered unit
        :param unit_name: The name of the unit
        :param capacity_end_date: The nameplate capacity of the unit
        :type dg: pd.DataFrame
        :type unit_name: string
        :type capacity_end_date: float or None
        :return: The expected availabilty programs and
                 the set of problematic publications
        :rtype: (pd.DataFrame, list)
    """

    dg = dg.sort_index(level = global_var.publication_dt_utc)
    
    ### Checks
    assert dg.shape[0] > 0
    assert len(dg[global_var.unit_name].unique()) == 1
    
    ### Publication dates
    pub_dt_start    = min(dg.index.get_level_values(global_var.publication_dt_utc).min() - np.timedelta64(1, 'h'),
                          pd.to_datetime('2010-01-01 00:00').tz_localize('UTC'),
                          )
    dt_publications = pd.DatetimeIndex(  [pub_dt_start]
                                       + list(dg.index.get_level_values(global_var.publication_dt_utc)),
                                       name = global_var.publication_dt_utc,
                                       )
    
    ### Production Steps
    prod_timesteps   = np.sort(np.unique(dg[[global_var.outage_begin_dt_utc,
                                             global_var.outage_end_dt_utc,
                                             ]]))    
    production_steps = pd.DatetimeIndex(  [prod_timesteps.min() - np.timedelta64(1, 'h')]
                                        + list(prod_timesteps)
                                        + [prod_timesteps.max() + np.timedelta64(1, 'h')],
                                        name = global_var.production_step_dt_utc,
                                        )

    ### Capacity
    nameplate_capacity_max = max(dg[global_var.capacity_nominal_mw])
    assert not np.isnan(nameplate_capacity_max)

    # Init program    
    dikt_active = {}
    program     = pd.DataFrame(nameplate_capacity_max,
                               index   = dt_publications,
                               columns = production_steps,
                               )                               
    bad_publications       = []
    cancelled_publications = []
    active_publication_dt  = pd.Series(index = production_steps,
                                       dtype = str,
                                       )
    
    ### Include all updates
    for ii, ((publi_id, version, publi_dt), publi) in enumerate(dg.iterrows()):
        if publi_id in dikt_active:
            ### Get previous version of publication
            prev                     = dikt_active[publi_id]
            prev_outage_begin        = prev[global_var.outage_begin_dt_utc]
            prev_outage_end          = prev[global_var.outage_end_dt_utc]
            ### Get the nameplate capacity
            prev_nameplate_capacity = prev[global_var.capacity_nominal_mw]
            if np.isnan(prev_nameplate_capacity):
                prev_nameplate_capacity = nameplate_capacity_max
            ### Identify where previous publication is still the most recent
            active_outage_window = active_publication_dt.loc[prev_outage_begin:prev_outage_end].iloc[:-1]
            prev_outage_active   = active_outage_window.loc[(active_outage_window.values == publi_id)].index
            ### Reset the capacity
            if not prev_outage_active.empty:
                prev_still_active = [program.columns.get_loc(dd)
                                     for dd in prev_outage_active
                                     ]
                program.iloc[ii+1:,prev_still_active] = prev_nameplate_capacity
            del dikt_active[publi_id]
        else: 
            ### Check coherence
            first_version       = (version == 1)
            publi_was_cancelled = (publi_id in cancelled_publications)
            publi_being_created = (publi[global_var.publication_creation_dt_utc] == publi_dt)
            if not (   first_version 
                    or publi_was_cancelled
                    or publi_being_created
                    ):
                reasons = '+'.join([pb 
                                    for (pb, correct) in [('pb_version',         first_version),
                                                          ('pb_cancelled_publi', publi_was_cancelled),
                                                          ('publi_creation_dt',  publi_being_created),
                                                          ]
                                    if not correct
                                    ])
                bad_publications.append((reasons, publi))

        ### Add effect of the new publication
        if publi[global_var.outage_status] == global_var.outage_status_cancelled:
            cancelled_publications.append(publi_id)
        else:
            remaining_power_mw   = publi[global_var.capacity_available_mw]
            correction_begin     = publi[global_var.outage_begin_dt_utc]
            correction_end       = publi[global_var.outage_end_dt_utc]
            nameplate_capacity   = publi[global_var.capacity_nominal_mw]
            if np.isnan(nameplate_capacity):
                nameplate_capacity = nameplate_capacity_max
            cond_capacity_end    = (    bool(capacity_end_date)
                                    and correction_end >= capacity_end_date
                                    )
            if cond_capacity_end and (nameplate_capacity == 0):
                slice_correction = slice(program.columns.get_loc(correction_begin),
                                         None,
                                         )
            else:
                slice_correction = slice(program.columns.get_loc(correction_begin),
                                         program.columns.get_loc(correction_end),
                                         )
            program.iloc[ii+1:,slice_correction]         = remaining_power_mw
            active_publication_dt.iloc[slice_correction] = publi_id
            dikt_active[publi_id] = publi
    
    ### Eliminate the first of simultaneous publications
    program = program.groupby(global_var.publication_dt_utc).tail(1)
    
    ### Checks
    assert not pd.isnull(program.index.values).any()
    assert not pd.isnull(program.columns).any()

    return program, bad_publications


