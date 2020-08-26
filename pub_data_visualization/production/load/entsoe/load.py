

import pandas as pd
import os
#
from .... import global_var
from . import paths, transcode

def load(map_code = None):
    """
        Loads the production data provided by ENTSO-E
        in the given delivery zone.
 
        :param map_code: The bidding zone
        :type map_code: string
        :return: The production data
        :rtype: pd.DataFrame
    """
    
    df_path = paths.fpath_production_entsoe_tmp.format(map_code = map_code) + '.csv'
    try:
        print('Load df - ', end = '')
        df = pd.read_csv(df_path,
                         header = [0],
                         sep = ';',
                         )
        df.loc[:,global_var.production_dt_UTC] = pd.to_datetime(df[global_var.production_dt_UTC])
        print('Loaded df') 
    except Exception as e:
        print('fail')
        print(e)
        dikt_production = {}
        try:
            list_files  = sorted([fname
                                  for fname in os.listdir(paths.folder_production_entsoe_raw)
                                  if os.path.splitext(fname)[1] == '.csv'
                                  ])
            assert len(list_files) > 0
        except Exception as e:
            print('Files not found.\n'
                  'They can be downloaded with the SFTP share proposed by ENTSOE at \n'
                  'https://transparency.entsoe.eu/content/static_content/Static%20content/knowledge%20base/SFTP-Transparency_Docs.html\n'
                  'and stored in\n'
                  '{0}'.format(paths.folder_production_entsoe_raw)
                  )
            raise e
        for ii, fname in enumerate(list_files):
            print('\r{0:3}/{1:3} - {2:<35}'.format(ii,
                                                   len(list_files),
                                                   fname,
                                                   ),
                  end = '',
                  )
            df = pd.read_csv(os.path.join(paths.folder_production_entsoe_raw,
                                          fname,
                                          ),
                             encoding   = 'UTF-16 LE',
                             sep        = '\t',
                             decimal    = '.',
                             )
            df = df.rename(transcode.columns,
                           axis = 1,
                           )
            
            df[global_var.quantity_value] = (  df[global_var.production_positive_part_mw].fillna(0) 
                                             - df[global_var.production_negative_part_mw].fillna(0) 
                                             )
            df[global_var.production_nature] = global_var.production_nature_observation_mw
            df.loc[:,global_var.production_dt_UTC] = pd.to_datetime(df[global_var.production_dt_UTC]).dt.tz_localize('UTC')
            df = df[[
                     global_var.production_dt_UTC,
                     global_var.geography_map_code,
                     global_var.unit_name,
                     global_var.production_source,
                     global_var.quantity_value,
                     global_var.production_nature,
                     ]]
            df = df[df[global_var.geography_map_code] == map_code]
            dikt_production[fname] = df
        print()
        
        df = pd.concat([dikt_production[key]
                        for key in dikt_production.keys()
                        ],
                       axis = 0,
                       )

        # Save
        print('Save')
        os.makedirs(os.path.dirname(df_path),
                    exist_ok = True,
                    )
        df.to_csv(df_path,
                  sep = ';',
                  index = False,
                  )

    return df

    
