

import pandas as pd
import os
import urllib
import datetime as dt
#
from .... import global_tools, global_var
from .load_raw import load_raw
from . import transcode, paths

def load(map_code = None,
         date_min = None,
         date_max = None,
         ):
    """
        Loads the load data provided by eCO2mix.
 
        :param map_code: The delivery zone
        :param date_min: The left bound
        :param date_max: The right bound
        :type map_code: string
        :type date_min: pd.Timestamp
        :type date_max: pd.Timestamp
        :return: The load data
        :rtype: pd.DataFrame
    """

    if not bool(date_min):
        date_min = pd.Timestamp('2012')
    if not bool(date_max):
        date_max = dt.datetime.now()

    assert map_code == global_var.geography_map_code_france
    df_path         = paths.fpath_load_tmp.format(date_min.year,
                                                  (date_max-pd.DateOffset(nanosecond = 1)).year,
                                                  )
    try:
        print('Load load/eco2mix - ', end = '')
        df = pd.read_csv(df_path,
                         header = [0],
                         sep = ';',
                         )
        df.loc[:,global_var.load_dt_utc] = pd.to_datetime(df[global_var.load_dt_utc])
        print('Loaded')
    except:
        print('fail - has to read raw data')
        dikt_load   = {}
        range_years = range(date_min.year,
                            ((date_max-pd.DateOffset(nanosecond = 1)).year+1),
                            )
        for ii, year in enumerate(range_years):
            print('\r{0:3}/{1:3} - {2}'.format(ii+1,
                                               len(range_years),
                                               year,
                                               ),
                  end = '',
                  )
            try:
                df = load_raw(year)
            except urllib.error.HTTPError:
                print('\nDownloads from eCO2mix failed and stopped at year {}'.format(year),
                      end = '',
                      )
                break
            df = df.rename(transcode.columns,
                           axis = 1,
                           )
            df[global_var.load_dt_local] = pd.to_datetime(  df[global_var.load_date_local]
                                                          + ' '
                                                          + df[global_var.load_time_local]
                                                          )
            df = df.loc[df[global_var.load_dt_local].apply(lambda x : global_tools.dt_exists_in_tz(x, 'CET'))]
            df[global_var.load_dt_local] = df[global_var.load_dt_local].dt.tz_localize('CET', ambiguous = True)
            df[global_var.load_dt_utc]   = df[global_var.load_dt_local].dt.tz_convert('UTC')
            df = df[[global_var.load_nature_forecast_day0,
                     global_var.load_nature_forecast_day1,
                     global_var.load_nature_observation,
                     global_var.load_dt_utc,
                     ]]
            df[global_var.geography_map_code] = global_var.geography_map_code_france
            df = df.set_index([global_var.load_dt_utc,
                               global_var.geography_map_code,
                               ])
            df.columns.name = global_var.load_nature
            # df[global_var.load_nature_forecast_day0_gw] = df[global_var.load_nature_forecast_day0_mw]/1e3
            # df[global_var.load_nature_forecast_day1_gw] = df[global_var.load_nature_forecast_day1_mw]/1e3
            # df[global_var.load_nature_observation_gw]   = df[global_var.load_nature_observation_mw]  /1e3
            df      = df.dropna(axis = 0, how = 'all')
            ds      = df.stack(0)
            ds.name = global_var.load_power_mw
            df = ds.reset_index()
            dikt_load[year] = df
        print()
        df = pd.concat([dikt_load[key]
                        for key in dikt_load.keys()
                        ],
                       axis = 0,
                       )
        df[global_var.commodity]     = global_var.commodity_electricity
        df[global_var.load_power_gw] = df[global_var.load_power_mw]/1e3

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

    
