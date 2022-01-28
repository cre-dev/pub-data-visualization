

import pandas as pd
import os
#
from .... import global_var
from . import transcode, paths

def load(map_code = None):
    """
        Loads the load data provided by ENTSO-E.
 
        :param map_code: The delivery zone
        :type map_code: string
        :return: The load data
        :rtype: pd.DataFrame
    """
    
    df_path = paths.fpath_tmp.format(map_code = map_code) + '.csv'
    try:
        print('Load load/entsoe - ', end = '')
        df = pd.read_csv(df_path,
                         header = [0],
                         sep = ';',
                         )
        df.loc[:,global_var.load_dt_utc] = pd.to_datetime(df[global_var.load_dt_utc])
        print('Loaded')
    except Exception as e:
        print('fail')
        print(e)
        dikt_load = {}
        try:
            list_files  = sorted(os.listdir(paths.folder_raw))
            assert len(list_files) > 0
        except Exception as e:
            print('Files not found.\n'
                  'They can be downloaded with the SFTP share proposed by ENTSOE at \n'
                  'https://transparency.entsoe.eu/content/static_content/Static%20content/knowledge%20base/SFTP-Transparency_Docs.html\n'
                  'and stored in\n'
                  '{0}'.format(paths.folder_raw)
                  )
            raise e
        for ii, fname in enumerate(list_files):
            if os.path.splitext(fname)[1] == '.csv':
                print('\r{0:3}/{1:3} - {2:<28}'.format(ii+1,
                                                   len(list_files),
                                                   fname,
                                                   ),
                      end = '',
                      )
                df = pd.read_csv(os.path.join(paths.folder_raw,
                                              fname,
                                              ),
                                 encoding   = 'UTF-8',
                                 sep        = '\t',
                                 decimal    = '.',
                                 )
                df = df.rename(transcode.columns,
                               axis = 1,
                               )
                df[global_var.load_dt_utc] = pd.to_datetime(df[global_var.load_dt_utc]).dt.tz_localize('UTC')
                df = df[df[global_var.geography_map_code] == map_code]
                df = df[[global_var.load_dt_utc,
                         global_var.geography_map_code,
                         global_var.load_power_mw,
                         ]]
                df = df.set_index([global_var.load_dt_utc,
                                   global_var.geography_map_code,
                                   ])
                #df.columns.name = global_var.load_nature
                df      = df.dropna(axis = 0,
                                    how  = 'all',
                                    )
                #df      = df.stack(0)
                #df.name = global_var.quantity_value
                df = df.reset_index()
                dikt_load[fname] = df
        print()
        df = pd.concat([dikt_load[key]
                        for key in dikt_load.keys()
                        ],
                       axis = 0,
                       )
        df[global_var.commodity]     = global_var.commodity_electricity
        df[global_var.load_nature]   = global_var.load_nature_observation
        df[global_var.load_power_gw] = df[global_var.load_power_mw]/1e3
        df = df[~df[global_var.load_dt_utc].duplicated(keep='first')]

        # Save
        print('Save')
        os.makedirs(os.path.dirname(df_path),
                    exist_ok = True,
                    )
        df.to_csv(df_path,
                  sep = ';',
                  index = False,
                  )
        
    print('done')
    return df
