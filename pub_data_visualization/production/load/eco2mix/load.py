

import pandas as pd
import os
import urllib
import datetime as dt
#
from .... import global_tools, global_var
from ....load.load.eco2mix.load_raw import load_raw
from . import paths, transcode


def load(date_min = None,
         date_max = None,
         map_code = None,
         ):
    """
        Loads the production data provided by eCO2mix
        between two dates in the given delivery zone.
 
        :param date_min: The left bound
        :param date_max: The right bound
        :param map_code: The bidding zone
        :type date_min: pd.Timestamp
        :type date_max: pd.Timestamp
        :type map_code: string
        :return: The production data
        :rtype: pd.DataFrame
    """
    
    assert map_code == global_var.geography_map_code_france
    fpath_csv = paths.fpath_tmp.format(date_min.year if bool(date_min) else 'None',
                                       (date_max - pd.DateOffset(nanosecond = 1)).year if bool(date_max) else 'None',
                                       )
    try:
        print('Load df - ', end = '')
        df = pd.read_csv(fpath_csv,
                         header = [0],
                         sep = ';',
                         )
        df.loc[:,global_var.production_dt_UTC] = pd.to_datetime(df[global_var.production_dt_UTC])
        print('Loaded df') 
    except:
        print('fail - has to read raw data')
        dikt_production = {}
        range_years     = range(date_min.year if bool(date_min) else 2012,
                                ((date_max-pd.DateOffset(nanosecond = 1)).year+1) if bool(date_max) else dt.datetime.now().year,
                                )
        for ii, year in enumerate(range_years):
            print('\r{0:3}/{1:3} - {2}'.format(ii,
                                               len(range_years),
                                               year,
                                               ),
                  end = '',
                  )
            try:
                df = load_raw(year)
            except urllib.error.HTTPError:
                print('\nDownloads failed and stopped at year {}'.format(year),
                      end = '',
                      )
                break
            df = df.rename(transcode.columns,
                           axis = 1,
                           )
            df[global_var.production_dt_local] = pd.to_datetime(  df[global_var.production_date_local] 
                                                                + ' ' 
                                                                + df[global_var.production_time_local],
                                                                )
            df = df.loc[~df[global_var.production_dt_local].isna()]
            df = df.loc[df[global_var.production_dt_local].apply(lambda x : global_tools.dt_exists_in_tz(x, 'CET'))]
            df.loc[:,global_var.production_dt_local] = df[global_var.production_dt_local].dt.tz_localize('CET', ambiguous = True)
            df[global_var.production_dt_UTC]         = df[global_var.production_dt_local].dt.tz_convert('UTC')
            df = df.drop([global_var.file_info,
                          global_var.load_nature_forecast_day0_mw,
                          global_var.load_nature_forecast_day1_mw,
                          global_var.load_nature_observation_mw,
                          global_var.production_date_local,
                          global_var.production_time_local,
                          global_var.geography_area_name,
                          global_var.production_dt_local,
                          ],
                         axis = 1,
                         )
            df = df.drop([col
                          for col in df.columns
                          if (   'Ech.' in col
                              or 'Co2' in col
                              )
                          ],
                         axis = 1,
                         )
            df[global_var.geography_map_code] = global_var.geography_map_code_france
            df = df.set_index([global_var.production_dt_UTC,
                               global_var.geography_map_code,
                               ])
            df.columns.name = global_var.production_source
            df = df.dropna(axis = 0, how = 'all')
            df = df.stack(0)
            df.name = global_var.quantity_value
            df = df.reset_index()
            df[global_var.unit_name] = 'agg'
            df[global_var.production_nature] = global_var.production_nature_observation_mw
            dikt_production[year] = df
        print()
        df = pd.concat([dikt_production[key]
                        for key in dikt_production.keys()
                        ],
                       axis = 0,
                       )

        # Save
        print('Save')
        os.makedirs(os.path.dirname(fpath_csv),
                    exist_ok = True,
                    )
        df.to_csv(fpath_csv,
                  sep = ';',
                  index = False,
                  )

    return df


    
    
