

import pandas as pd
import os
#
from ..... import global_var
from . import paths, transcode



def load(map_code = None):
    """
        Loads the aggregated capacities provided by ENTSO-E.
 
        :param map_code: The bidding zone
        :type map_code: string
        :return: The aggregated capacities
        :rtype: pd.DataFrame
    """
    df_path = paths.fpath_tmp.format(map_code = map_code) + '.csv'
    try:
        print('Load capacity/entsoe - ', end = '')
        df = pd.read_csv(df_path,
                         header = [0],
                         sep = ';',
                         )
        print('Loaded')
    except Exception as e:
        print('fail')
        print(e)
        dikt_capacity = {}
        list_files  = sorted([fname
                              for fname in os.listdir(paths.folder_raw)
                              if os.path.splitext(fname)[1] == '.csv'
                              ])
        assert len(list_files) > 0, ('Files not found.\n'
                                     'They can be downloaded with the ENTSOE SFTP share\n'
                                     'and stored in\n'
                                     '{0}'.format(paths.folder_raw)
                                     )
        for ii, fname in enumerate(list_files):
                print('\r{0:3}/{1:3} - {2}'.format(ii+1,
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
                df = df[df[global_var.geography_map_code] == map_code]
                dikt_capacity[fname] = df
    
        df = pd.concat([dikt_capacity[key]
                        for key in dikt_capacity.keys()
                        ],
                       axis = 0,
                       )
        df.loc[:,global_var.production_source] = df[global_var.production_source].astype(str).replace(transcode.production_source)
        df[global_var.commodity] = global_var.commodity_electricity

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

