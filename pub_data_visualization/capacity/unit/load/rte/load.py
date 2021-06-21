

import pandas as pd
import os
#
from ..... import global_var
from . import paths, transcode


def load(map_code = None):
    """
        Loads the unit capacities provided by RTE.
 
        :param map_code: The bidding zone
        :type map_code: string
        :return: The unit capacities
        :rtype: pd.DataFrame
    """
    assert map_code == global_var.geography_map_code_france
    df_path         = paths.fpath_tmp.format(map_code = map_code) + '.csv'
    try:
        print('Load df_capacity - ', end = '')
        df = pd.read_csv(df_path,
                         header = [0],
                         sep = ';',
                         )
        df.loc[:,global_var.capacity_end_date_UTC]         = pd.to_datetime(df[global_var.capacity_end_date_UTC])
        df.loc[:,global_var.publication_creation_dt_UTC]   = pd.to_datetime(df[global_var.publication_creation_dt_UTC])
        df.loc[:,global_var.publication_creation_dt_local] = df[global_var.publication_creation_dt_UTC].dt.tz_convert(global_var.dikt_tz[map_code])
        df.loc[:,global_var.capacity_end_date_local]       = df[global_var.capacity_end_date_UTC].dt.tz_convert(global_var.dikt_tz[map_code])
        print('Loaded') 
    except FileNotFoundError:
        print('fail - has to read raw data')
        dikt_capacity = {}
        list_files    = os.listdir(paths.folder_raw)
        list_files    = sorted([fname
                                for fname in os.listdir(paths.folder_raw)
                                if os.path.splitext(fname)[1] == '.xls'
                                ])
        for ii, fname in enumerate(list_files):
            print('\r{0:>3}/{1:>3} - {2}'.format(ii,
                                                 len(list_files),
                                                 fname,
                                                 ),
                  end = '',
                  )
            df = pd.read_csv(os.path.join(paths.folder_raw,
                                          fname,
                                          ), 
                             sep        = '\t', 
                             encoding   = 'latin-1',
                             skiprows   = [0],
                             skipfooter = 2,
                             engine     = 'python',
                             )
            df = df.rename(transcode.columns, 
                           axis = 1,
                           )
            df.loc[:,global_var.production_source] = df[global_var.production_source].astype(str).replace(transcode.columns)
            df[global_var.geography_map_code]      = map_code
            dikt_capacity[fname]                   = df
        print()
        df = pd.concat([dikt_capacity[key]
                        for key in dikt_capacity.keys()
                        ],
                       axis = 0,
                       )
        df = df.loc[df[global_var.capacity_end_date_local].dropna().index]
        df.loc[:,global_var.publication_creation_dt_local] = pd.to_datetime(df[global_var.publication_creation_dt_local]).dt.tz_localize(global_var.dikt_tz[map_code])
        df.loc[:,global_var.capacity_end_date_local]       = pd.to_datetime(df[global_var.capacity_end_date_local]).dt.tz_localize(global_var.dikt_tz[map_code])
        df[global_var.publication_creation_dt_UTC]         = df[global_var.publication_creation_dt_local].dt.tz_convert('UTC')
        df[global_var.capacity_end_date_UTC]               = df[global_var.capacity_end_date_local].dt.tz_convert('UTC')
        df[global_var.commodity]                           = global_var.commodity_electricity

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


    
