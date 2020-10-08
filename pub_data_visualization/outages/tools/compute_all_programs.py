
import numpy as np
import pandas as pd
#
from ... import global_var, capacity
    
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
        capacity_end = capacity.unit.load(source     = global_var.data_source_rte,
                                          map_code   = 'FR',
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
        print('\rCompute program - {0:3}/{1:3} - {2:20}'.format(ii, 
                                                                len(list_plants),
                                                                unit_name,
                                                                ),
              end = '',
              )
        df_unit = df_outage.loc[df_outage[global_var.unit_name] == unit_name]
        dikt_programs[unit_name], dikt_bad_publications[unit_name] = compute_program(df_unit,
                                                                                     unit_name         = unit_name,
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
                    unit_name         = None,
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

    dg     = dg.sort_index(level = global_var.publication_dt_UTC)
    nb_pub = dg.shape[0]
    
    ### Checks
    assert nb_pub
    assert len(dg[global_var.unit_name].unique()) == 1
    
    ### Publication dates
    dt_start        = min(dg.index.get_level_values(global_var.publication_dt_UTC).min() - np.timedelta64(1, 'h'),
                          pd.to_datetime('2000-01-01 00:00').tz_localize('UTC'),
                          )
    dt_publications  = pd.DatetimeIndex([dt_start]).union(dg.index.get_level_values(global_var.publication_dt_UTC))
    
    ### Production Steps
    time_changes     = np.sort(np.unique(dg[[global_var.outage_begin_dt_UTC,
                                             global_var.outage_end_dt_UTC,
                                             ]]))    
    idx_to_timesteps = pd.concat([pd.DataFrame([time_changes.min() - np.timedelta64(1, 'h')], 
                                                index = ['initial'],
                                                ), 
                                  pd.DataFrame(time_changes,
                                               index = range(1, len(time_changes) + 1),
                                               ), 
                                  pd.DataFrame([time_changes.max() + np.timedelta64(1, 'h')], 
                                                index = ['final'],
                                                ), 
                                  ],
                                 axis = 0,
                                 )
    idx_to_timesteps.columns = [global_var.production_step_dt_UTC]
    timesteps_to_idx = {ts:ii 
                        for ii, ts in enumerate(idx_to_timesteps[global_var.production_step_dt_UTC])
                        }

    ### Capacity
    nameplate_capacity_max = max(dg[global_var.unit_nameplate_capacity])
    assert not np.isnan(nameplate_capacity_max)

    # Init program    
    dikt_active = {}
    program     = nameplate_capacity_max * np.ones((nb_pub + 1, idx_to_timesteps.shape[0]))
    bad_publications       = []
    cancelled_publications = []
    active_publication_dt  = pd.Series(index = time_changes)
    
    # Include all updates
    for ii, ((publi_id, version, publi_dt), publi) in enumerate(dg.iterrows()):
        #    
        if publi_id in dikt_active:
            # Delete effect of the previous version
            prev                     = dikt_active[publi_id]
            prev_outage_begin        = prev[global_var.outage_begin_dt_UTC]
            prev_outage_end          = prev[global_var.outage_end_dt_UTC]
            prev_name_plate_capacity = prev[global_var.unit_nameplate_capacity]
            if np.isnan(prev_name_plate_capacity):
                prev_name_plate_capacity = nameplate_capacity_max
            active_outage_window     = active_publication_dt.loc[prev_outage_begin:prev_outage_end]
            bool_prev_active         = (active_outage_window == publi_id)
            prev_outage_active       = active_outage_window.loc[bool_prev_active].index
            if not prev_outage_active.empty:
                prev_idx_correction = slice(timesteps_to_idx[prev_outage_active.min()],
                                            timesteps_to_idx[prev_outage_active.max()],
                                            )
                program[ii+1:,prev_idx_correction] = prev_name_plate_capacity
            del dikt_active[publi_id]
        else: 
            first_version       = (version == 1)
            publi_was_cancelled = (publi_id in cancelled_publications)
            publi_being_created = (publi[global_var.publication_creation_dt_UTC] == publi_dt)
            if not (   first_version 
                    or publi_was_cancelled
                    or publi_being_created
                    ):
                ### Store incoherences
                reasons = '+'.join([pb 
                                    for (pb, correct) in [('pb_version',         first_version),
                                                          ('pb_cancelled_publi', publi_was_cancelled),
                                                          ('publi_creation_dt',  publi_being_created),
                                                          ]
                                    if not correct
                                    ])
                bad_publications.append((reasons, publi))

        ### Add effect of the new publication
        remaining_power_mw   = publi[global_var.outage_remaining_power_mw]           
        correction_begin     = publi[global_var.outage_begin_dt_UTC]
        correction_end       = publi[global_var.outage_end_dt_UTC]
        nameplate_capacity   = publi[global_var.unit_nameplate_capacity]
        if np.isnan(nameplate_capacity):
            nameplate_capacity = nameplate_capacity_max
        idx_correction_begin = timesteps_to_idx[correction_begin]
        cond_capacity_end    = (    bool(capacity_end_date)
                                and correction_end >= capacity_end_date
                                )
        if publi[global_var.outage_status] == global_var.outage_status_cancelled:
            cancelled_publications.append(publi_id)
        else:
            if cond_capacity_end and (nameplate_capacity == 0):
                slice_correction = slice(idx_correction_begin,
                                         None,
                                         )
            else:
                slice_correction = slice(idx_correction_begin,
                                         timesteps_to_idx[correction_end],
                                         )
            program[ii+1:,slice_correction] = remaining_power_mw
            dikt_active[publi_id] = publi
            active_publication_dt.loc[correction_begin:correction_end] = publi_id
    program = pd.DataFrame(program, 
                           index   = dt_publications, 
                           columns = idx_to_timesteps[global_var.production_step_dt_UTC],
                           )
    program.index.name   = global_var.publication_dt_UTC
    program.columns.name = global_var.production_step_dt_UTC
    
    ### Eliminate the first of simultaneous publications
    program = program.groupby(global_var.publication_dt_UTC).tail(1)
    
    ### Checks
    assert not pd.isnull(program.index.values).any()
    assert not pd.isnull(program.columns).any()

    return program, bad_publications


