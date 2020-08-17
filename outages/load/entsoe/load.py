
import pandas as pd
import os
import re
#
import global_var
import global_tools
from . import paths
from . import transcode
from .assemble import assemble


def load(map_code = None):
    df_path = paths.fpath_tmp.format(map_code = map_code,
                                     file     = 'df',
                                     ) + '.csv'
    try:
        print('Load df and dikt - ', end = '')
        df = pd.read_csv(df_path,
                         sep = ';',
                         )
        df.loc[:,global_var.publication_dt_UTC]          = pd.to_datetime(df[global_var.publication_dt_UTC])
        df.loc[:,global_var.outage_begin_dt_UTC]         = pd.to_datetime(df[global_var.outage_begin_dt_UTC])
        df.loc[:,global_var.outage_end_dt_UTC]           = pd.to_datetime(df[global_var.outage_end_dt_UTC])
        df.loc[:,global_var.publication_creation_dt_UTC] = pd.to_datetime(df[global_var.publication_creation_dt_UTC])
        print('Loaded') 
    except FileNotFoundError:
        print('fail - FileNotFound')

        dikt_outages = {}
        list_paths   = [(folder, fname)
                        for (folder, list_subfolders, list_files) in os.walk(paths.folder_raw)
                        for fname in list_files
                        ]
        assert len(list_paths) > 0, ('Files not found.\n'
                                     'They can be downloaded with the ENTSOE SFTP share\n'
                                     'and stored in\n'
                                     '{0}'.format(paths.folder_raw)
                                     )
        list_paths = sorted(list_paths, key = lambda x : x[1])
        for ii, (folder, fname) in enumerate(list_paths):
            if os.path.splitext(fname)[1] == '.csv':
                print('\rRead {0:>3}/{1:>3} - {2:>25}'.format(ii,
                                                              len(list_paths),
                                                              fname,
                                                              ),
                      end = '',
                      )
                df        = pd.read_csv(os.path.join(folder,
                                                     fname,
                                                     ),
                                        encoding   = 'UTF-16 LE',
                                        sep        = '\t',
                                        decimal    = '.',
                                        )
                df = df.rename(transcode.columns, 
                               axis = 1,
                               )
                df = df.loc[df[global_var.geography_map_code] == map_code]
                df[global_var.file_name] = os.path.basename(fname)
                match_unit_type = re.compile(r"^(\d{4})_(\d{1,2})_Outages(G|P)U.csv$").match(fname)
                assert match_unit_type.group(3) in ['G','P']
                df[global_var.unit_type] = (global_var.unit_type_group
                                            if match_unit_type.group(3) == 'G'
                                            else
                                            global_var.unit_type_plant
                                            )
                # Localize and Convert
                for col in [
                            global_var.publication_dt_UTC,
                            global_var.outage_begin_dt_UTC,
                            global_var.outage_end_dt_UTC,
                            ]:
                    df.loc[:,col] = pd.to_datetime(df[col],
                                                   format = '%Y/%m/%d %H:%M:%S',
                                                   )
                    df.loc[:,col] = df[[col, global_var.time_zone]].apply(lambda row : row[col].tz_localize(row[global_var.time_zone],
                                                                                                            ambiguous = True,
                                                                                                            ).tz_convert('UTC'),
                                                                          axis = 1,
                                                                          )
                dikt_id_creation_dt = df.groupby(global_var.publication_id)[global_var.publication_dt_UTC].agg(min).to_dict()
                df[global_var.publication_creation_dt_UTC] = df[global_var.publication_id].map(dikt_id_creation_dt)
                dikt_outages[fname] = df
            
        print('\nConcatenate')
        df = pd.concat([dikt_outages[key] 
                        for key in dikt_outages.keys()
                        ],
                       axis = 0,
                       sort = False,
                       )
        df = df.reset_index(drop = True)
        df[global_var.outage_remaining_power_gw] = df[global_var.outage_remaining_power_mw]/1e3
        df.loc[:,global_var.company_name]        = global_var.company_name_unknown
        
        print('Transcode')
        df.loc[:,global_var.unit_name]         = df[global_var.unit_name].apply(global_tools.format_unit_name)
        df.loc[:,global_var.outage_type]       = df[global_var.outage_type].replace(transcode.outage_type)
        df.loc[:,global_var.production_source] = df[global_var.production_source].astype(str).replace(transcode.production_source)
        df.loc[:,global_var.outage_status]     = df[global_var.outage_status].astype(str).replace(transcode.outage_status)
        
        print('Assemble')
        df = assemble(df)
            
        print('Save')
        os.makedirs(os.path.dirname(df_path),
                    exist_ok = True,
                    )
        df.to_csv(df_path,
                  sep = ';',
                  index = False,
                  )
            
    print('done : df.shape = {0}'.format(df.shape)) 
    return df


