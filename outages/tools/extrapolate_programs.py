


import pandas as pd
#


def extrapolate_programs(dikt_programs,
                         dates_to_extrapolate,
                         production_dt_min = None,
                         production_dt_max = None,
                         ):
    all_production_steps = sorted(set([e
                                       for unit_name in dikt_programs
                                       for e in dikt_programs[unit_name].columns
                                       ]))
    selected_production_steps = [e
                                 for ii, e in enumerate(all_production_steps)
                                 if (    (   ii+1 == len(all_production_steps)
                                          or all_production_steps[ii+1] >= production_dt_min
                                          )
                                     and all_production_steps[ii] <  production_dt_max
                                     )
                                 ]
    
    dikt_extrapolated_programs = {}
    for dd in dates_to_extrapolate:
        program_plants = pd.DataFrame({plant_name : programs.iloc[programs.index.get_loc(dd,
                                                                                         'ffill',
                                                                                         )].reindex(index = selected_production_steps,
                                                                                                    method = 'ffill',
                                                                                                    )
                                       for plant_name, programs in dikt_programs.items()
                                       })
        program_plants = program_plants.fillna(method = 'bfill', axis = 0)
        dikt_extrapolated_programs[dd] = program_plants.sum(axis = 1)
        
    return pd.DataFrame(dikt_extrapolated_programs)