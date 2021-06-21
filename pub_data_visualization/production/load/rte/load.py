

import pandas as pd
import os
#
from .... import global_tools, global_var
from . import paths, transcode


def load():
    """
        Loads the production data provided by RTE.

        :return: The production data
        :rtype: pd.DataFrame
    """
    df_path = paths.fpath_production_rte_tmp + '.csv'
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
            list_paths   = [(folder, fname)
                            for (folder, list_subfolders, list_files) in os.walk(paths.folder_production_rte_raw)
                            for fname in list_files
                            if os.path.splitext(fname)[1] == '.xls'
                            ]
            assert len(list_paths) > 0
        except Exception as e:
            print('Files not found.\n'
                  'They can be downloaded with the website share proposed by RTE at \n'
                  'https://www.services-rte.com/fr/home.html\n'
                  'and stored in\n'
                  '{0}'.format(paths.folder_production_rte_raw)
                  )
            raise e
        for ii, (folder, fname) in enumerate(list_paths):
            print('\r{0:3}/{1:3} - {2:<35}'.format(ii,
                                                   len(list_paths),
                                                   fname,
                                                   ),
                  end = '',
                  )
            df = pd.read_csv(os.path.join(folder,
                                          fname,
                                          ),
                             header    = [0,1], 
                             index_col = [0], 
                             sep       = '\t', 
                             encoding  = 'latin-1',
                             na_values = ["*"],
                             skipinitialspace = True,
                             low_memory       = False,
                             )
            df = df.dropna(axis = 1, how = 'all')
            df.index         = [transcode.format_str_date(e) for e in df.index] 
            df.index.name    = global_var.production_dt_UTC
            df               = df.loc[df.index.dropna()]
            df.columns.names = [global_var.production_source, global_var.unit_name]
            df.columns       = df.columns.remove_unused_levels()
            df = df.stack([0,1])
            df = df.apply(lambda x : float(x.replace(',', '.')) if type(x) == str else x)
            df.name = global_var.quantity_value
            df = df.reset_index()
            df[global_var.production_nature] = global_var.production_nature_observation_mw
            df[global_var.unit_name] = [global_tools.format_unit_name(e)
                                        for e in 
                                        df[global_var.unit_name]
                                        ]
            dikt_production[fname] = df
    
        df = pd.concat([dikt_production[key]
                        for key in dikt_production.keys()
                        ],
                       axis = 0,
                       )
        df[global_var.geography_map_code] = global_var.geography_map_code_france
        df[global_var.commodity] = global_var.commodity_electricity

        # Save
        print('\nSave')
        os.makedirs(os.path.dirname(df_path),
                    exist_ok = True,
                    )
        df.to_csv(df_path,
                  sep   = ';',
                  index = False,
                  )

    return df





    
