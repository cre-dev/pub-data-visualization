
import pandas as pd
#


def compute_energy_unavailability_product(product_delivery_windows,
                                          program,
                                          ):
    """
        Computes the availability of one unit
        during the delivery windows of one contract.
 
        :param product_delivery_windows_local: The delivery windows
        :param program: The expected programs of the production unit
        :type product_delivery_windows_local: list of pairs
        :type program: pd.Dataframe
        :return: The availability during the delivery
                 of the unit at different dates
        :rtype: pd.Series
    """
    
    nameplate_capacity = program.max().max()
    window_dt_UTC      = [d.tz_convert('UTC') 
                          for (begin, end) in product_delivery_windows
                          for d in [begin, end]
                          ]
    new_steps          = pd.Index(sorted(set(program.columns).union(window_dt_UTC).union(program.index)))
    unavailability     = (nameplate_capacity - program)*(-1)
    unavailability     = (unavailability.reindex(columns = new_steps)
                                        .fillna(method = 'ffill',
                                                axis = 1,
                                                )
                                        )
    for jj, dt_prod in enumerate(unavailability.columns):
        if dt_prod < unavailability.index[0]:
            continue
        last_publi_before = unavailability.index.get_loc(dt_prod,
                                                         method = 'ffill',
                                                         )
        unavailability.iloc[last_publi_before:,jj] = unavailability.iloc[last_publi_before,jj]
    durations = unavailability.columns[1:] - unavailability.columns[:-1]
    unavailability_product = pd.DataFrame(0,
                                          columns = [],
                                          index = unavailability.index,
                                          )
    for jj, (begin, end) in enumerate(product_delivery_windows):
        idx_begin = unavailability.columns.get_loc(begin)
        idx_end   = unavailability.columns.get_loc(end)
        for idx in range(idx_begin, idx_end):
            duration               = durations[idx]
            unavailable_power      = unavailability.iloc[:,idx]
            unavailability_product[(unavailability.columns[idx],
                                    unavailability.columns[idx+1],
                                    )] = unavailable_power*duration.total_seconds()/3600
    return unavailability_product.sum(axis = 1)

###############################################################################

def compute_missing_energy(product_delivery_windows_local,
                           dikt_programs,
                           ):
    """
        Computes the availability during the delivery windows of one contract.
 
        :param product_delivery_windows_local: The delivery windows
        :param dikt_programs: The set of expected programs for the units
        :type product_delivery_windows_local: list of pairs
        :type dikt_programs: dict of pd.Dataframes
        :return: The availability during the delivery
                 at different dates
        :rtype: pd.Series
    """

    dikt_energy           = {}
    for ii, unit_name in enumerate(dikt_programs):
        print('\rcompute_missing_energy loop 1 - {0:3}/{1:3}- {2:20}'.format(ii,
                                                                             len(dikt_programs),
                                                                             unit_name, 
                                                                             ),
              end = '',
              )
        assert not pd.isnull(dikt_programs[unit_name].columns).sum()
        assert not pd.isnull(dikt_programs[unit_name].index.values).sum()
        dikt_energy[unit_name] = compute_energy_unavailability_product(product_delivery_windows_local,
                                                                       dikt_programs[unit_name],
                                                                       )
    all_publications_dates = sorted(set([e
                                         for unit_name in dikt_energy
                                         for e in dikt_energy[unit_name].index
                                         ]))
    for ii, unit_name in enumerate(dikt_energy):
        print('\rcompute_missing_energy loop 2 - {0:3}/{1:3}- {2:20}'.format(ii,
                                                                             len(dikt_energy),
                                                                             unit_name, 
                                                                             ),
              end = '',
              )
        dikt_energy[unit_name] = (dikt_energy[unit_name].reindex(index = all_publications_dates, method = 'ffill')
                                                        .fillna(method = 'bfill', axis = 0)
                                                        )
    df_energy = pd.concat([dikt_energy[k] 
                           for k in dikt_energy.keys()
                           ],
                          axis    = 1,
                          )
    df_energy_tot = df_energy.sum(axis = 1)
    print()
    
    return df_energy_tot


