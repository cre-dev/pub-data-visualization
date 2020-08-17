
import pandas as pd
#
import global_var
from . import meteofrance


def load(source   = global_var.data_source_meteofrance,
         zone     = 'Metropolitan_France',
         date_min = pd.Timestamp('2015').tz_localize('CET'),
         date_max = pd.Timestamp('2020').tz_localize('CET'),
         ):
    
    if source == global_var.data_source_meteofrance:
        df, coordinates_weather, trash_weather = meteofrance.load(zone     = zone,
                                                                  date_min = date_min,
                                                                  date_max = date_max,
                                                                  )
    
    else: 
        raise ValueError('Incorrect source : {0}'.format(source))
            
    dg = df.pivot_table(values  = global_var.quantity_value, 
                        index   = [global_var.weather_dt_UTC], 
                        columns = [
                                   global_var.weather_site_name,
                                   global_var.weather_physical_quantity,
                                   global_var.weather_nature,
                                   ],
                        )
    
    dg = dg.reindex(sorted(dg.columns), axis = 1)
    dg = dg.sort_index()
    
    dh = dg.loc[  pd.Series(True, index = dg.index)
                & ((dg.index >= date_min) if bool(date_min) else True)
                & ((dg.index <  date_max) if bool(date_max) else True)
                ]
    
    assert dh.shape[0] > 0
    assert dh.index.is_unique

    return dh


