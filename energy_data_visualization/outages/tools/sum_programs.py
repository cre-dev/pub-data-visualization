

import pandas as pd
#


def sum_programs(dikt_programs,
                 production_dt_min  = None,
                 production_dt_max  = None,
                 publication_dt_min = None,
                 publication_dt_max = None,
                 ):
    
    
    all_production_steps  = sorted(set([e
                                        for unit_name in dikt_programs
                                        for e in dikt_programs[unit_name].columns
                                        ]))
    all_publication_steps = sorted(set([e
                                       for unit_name in dikt_programs
                                       for e in dikt_programs[unit_name].index
                                       ]))
    selected_production_steps = [e
                                 for ii, e in enumerate(all_production_steps)
                                 if (    (   ii+1 == len(all_production_steps)
                                          or all_production_steps[ii+1] >= production_dt_min
                                          )
                                     and all_production_steps[ii] <  production_dt_max
                                     )
                                 ]
    selected_publication_steps = [e
                                  for ii, e in enumerate(all_publication_steps)
                                  if (    (   ii+1 == len(all_publication_steps)
                                           or all_publication_steps[ii+1] >= publication_dt_min
                                           )
                                      and all_publication_steps[ii] <  publication_dt_max
                                      )
                                  ]
    dikt_programs = {k:v.reindex(index = selected_publication_steps,
                                 method = 'ffill',
                                 ).reindex(columns = selected_production_steps,
                                           method = 'ffill',
                                           )
                     for k, v in dikt_programs.items()
                     }    

    dikt = {}
    for ii, dd in enumerate(selected_publication_steps):
        dikt[dd] = pd.DataFrame({plant_name : dikt_programs[plant_name].loc[dd]
                                 for plant_name in dikt_programs
                                 }).sum(axis = 1)
    dm = pd.DataFrame(dikt).T

    return dm