

import pandas as pd
import os
#
from .... import global_tools, global_var
from . import transcode
from .paths    import fpath_load_tmp
from .load_raw import load_raw

def load(date_min = None,
         date_max = None,
         map_code = None,
         ):
    """
        Loads the load data provided by eCO2mix.
 
        :param date_min: The left bound
        :param date_max: The right bound
        :param map_code: The delivery zone
        :type date_min: pd.Timestamp
        :type date_max: pd.Timestamp
        :type map_code: string
        :return: The load data
        :rtype: pd.DataFrame
    """
    
    assert map_code == global_var.geography_map_code_france
    df_path         = fpath_load_tmp.format(date_min.year,
                                            (date_max-pd.DateOffset(nanosecond = 1)).year,
                                            )
    try:
        print('Load df - ', end = '')
        df = pd.read_csv(df_path,
                         header = [0],
                         sep = ';',
                         )
        df.loc[:,global_var.load_dt_UTC] = pd.to_datetime(df[global_var.load_dt_UTC])
        print('Loaded df') 
    except:
        print('fail - has to read raw data')
        dikt_load   = {}
        range_years = range(date_min.year,
                            (date_max-pd.DateOffset(nanosecond = 1)).year+1,
                            )
        for ii, year in enumerate(range_years):
            print('\r{0:3}/{1:3} - {2}'.format(ii,
                                               len(range_years),
                                               year,
                                               ),
                  end = '',
                  )
            df = load_raw(year)
            df = df.rename(transcode.columns,
                           axis = 1,
                           )
            df[global_var.load_dt_local] = pd.to_datetime(  df[global_var.load_date_local]
                                                          + ' '
                                                          + df[global_var.load_time_local]
                                                          )
            df = df.loc[df[global_var.load_dt_local].apply(lambda x : global_tools.dt_exists_in_tz(x, 'CET'))]
            df[global_var.load_dt_local] = df[global_var.load_dt_local].dt.tz_localize('CET', ambiguous = True)
            df[global_var.load_dt_UTC]   = df[global_var.load_dt_local].dt.tz_convert('UTC') 
            df = df[[
                     global_var.load_nature_forecast_day0_mw,
                     global_var.load_nature_forecast_day1_mw,
                     global_var.load_nature_observation_mw,
                     global_var.load_dt_UTC,
                     ]]
            df[global_var.geography_map_code] = global_var.geography_map_code_france
            df = df.set_index([global_var.load_dt_UTC,
                               global_var.geography_map_code,
                               ])
            df.columns.name = global_var.load_nature
            df[global_var.load_nature_forecast_day0_gw] = df[global_var.load_nature_forecast_day0_mw]/1e3
            df[global_var.load_nature_forecast_day1_gw] = df[global_var.load_nature_forecast_day1_mw]/1e3
            df[global_var.load_nature_observation_gw]   = df[global_var.load_nature_observation_mw]  /1e3
            df      = df.dropna(axis = 0, how = 'all')
            df      = df.stack(0)
            df.name = global_var.quantity_value
            df = df.reset_index()
            dikt_load[year] = df
        print()
        df = pd.concat([dikt_load[key]
                        for key in dikt_load.keys()
                        ],
                       axis = 0,
                       )
        # Save
        print('Save')
        os.makedirs(os.path.dirname(df_path),
                    exist_ok = True,
                    )
        df.to_csv(df_path,
                  sep   = ';',
                  index = False,
                  )
    print('done')
    return df

    
