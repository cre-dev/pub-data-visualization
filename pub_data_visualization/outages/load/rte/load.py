
import pandas as pd
import os
import pickle
#
from .... import global_tools, global_var
from . import paths, transcode
from .assemble import assemble



def load(map_code = None):
    """
        Loads the outages data provided by RTE in the given delivery zone.
 
        :param map_code: The delivery zone
        :type map_code: string
        :return: The outages data
        :rtype: pd.DataFrame
    """
    
    assert map_code == global_var.geography_map_code_france
    df_path                = paths.fpath_tmp.format(map_code = map_code,
                                                    file     = 'df',
                                                    ) + '.csv'
    dikt_incoherences_path = paths.fpath_tmp.format(map_code = map_code,
                                                    file     = 'dikt_incoherences',
                                                    ) + '.pkl'    
    try:
        print('Load outages/rte - ', end = '')
        df = pd.read_csv(df_path,
                         sep = ';',
                         low_memory = False,
                         )
        with open(dikt_incoherences_path, 'rb') as f:
            dikt_incoherences = pickle.load(f)
        df.loc[:,global_var.publication_dt_utc]          = pd.to_datetime(df[global_var.publication_dt_utc])
        df.loc[:,global_var.outage_begin_dt_utc]         = pd.to_datetime(df[global_var.outage_begin_dt_utc])
        df.loc[:,global_var.outage_end_dt_utc]           = pd.to_datetime(df[global_var.outage_end_dt_utc])
        df.loc[:,global_var.publication_creation_dt_utc] = pd.to_datetime(df[global_var.publication_creation_dt_utc])
        print('Loaded')
    except FileNotFoundError:
        print('fail - FileNotFound')
        
        dikt_outages = {}
        list_files   = sorted([fname
                               for fname in os.listdir(paths.folder_raw)
                               if os.path.splitext(fname)[1] == '.xls'
                               ])
        assert len(list_files) > 0, ('Files not found.\n'
                                     'They can be downloaded from www.services-rte.com/\n'
                                     'and stored in\n'
                                     '{0}'.format(paths.folder_raw)
                                     )
        for ii, fname in enumerate(list_files):
            print('\rRead{0:>3}/{1:>3} - {2:>15}'.format(ii,
                                                         len(list_files),
                                                         fname,
                                                         ),
                  end = '',
                  )
            df = pd.read_csv(os.path.join(paths.folder_raw,
                                          fname,
                                          ),
                             sep        = '\t',
                             decimal    = ",",
                             encoding   = 'latin-1',
                             skipfooter = 2,
                             index_col  = False,
                             engine     = 'python',
                             )
            df = df.rename(transcode.columns, 
                           axis = 1,
                           )
            df.drop([global_var.outage_period_begin_dt_local,
                     global_var.outage_period_end_dt_local
                     ],
                    axis = 1,
                    )
            df[global_var.file_name] = os.path.basename(fname)
            dikt_outages[fname] = df
        
        print('\nConcatenate')
        df = pd.concat([dikt_outages[key] 
                        for key in dikt_outages.keys()
                        ],
                       axis = 0,
                       sort = False,
                       )
        df = df.reset_index(drop = True)
        
        print('Localize and convert')
        df[global_var.geography_map_code]    = map_code
        df[global_var.capacity_available_gw] = df[global_var.capacity_available_mw]/1e3
        for col_local, col_utc in [(global_var.publication_creation_dt_local, global_var.publication_creation_dt_utc),
                                   (global_var.publication_dt_local,          global_var.publication_dt_utc),
                                   (global_var.outage_begin_dt_local,         global_var.outage_begin_dt_utc),
                                   (global_var.outage_end_dt_local,           global_var.outage_end_dt_utc),
                                   ]:
            df.loc[:,col_local] = pd.to_datetime(df[col_local], format = '%d/%m/%Y %H:%M').dt.tz_localize('CET', ambiguous = True)
            df[col_utc]         = df[col_local].dt.tz_convert('UTC')
            df = df.drop(col_local, axis = 1)        

        print('Transcode')
        df.loc[:,global_var.unit_name]         = df[global_var.unit_name].replace(transcode.eic_code).apply(global_tools.format_unit_name)
        df.loc[:,global_var.producer_name]     = df[global_var.producer_name].replace(transcode.producer_name)
        df.loc[:,global_var.outage_type]       = df[global_var.outage_type].replace(transcode.outage_type)
        df.loc[:,global_var.unit_type]         = df[global_var.unit_type].replace(transcode.unit_type)
        df.loc[:,global_var.production_source] = df[global_var.production_source].astype(str).replace(transcode.production_source)
        df.loc[:,global_var.outage_status]     = df[global_var.outage_status].astype(str).replace(transcode.outage_status)

        print('Assemble')
        df, dikt_incoherences = assemble(df)
        
        print('Complete capacities')
        for unit_name in sorted(df[global_var.unit_name].unique()):
            if pd.isnull(df.loc[df[global_var.unit_name] == unit_name][global_var.capacity_nominal_mw]).all() > 0:
                df.loc[df[global_var.unit_name] == unit_name,global_var.capacity_nominal_mw] = transcode.capacity[unit_name]
        df[global_var.commodity] = global_var.commodity_electricity
        
        print('Save')
        os.makedirs(os.path.dirname(df_path),
                    exist_ok = True,
                    )
        df.to_csv(df_path,
                  sep = ';',
                  index = False,
                  )
        with open(dikt_incoherences_path, 'wb') as f:
            pickle.dump(dikt_incoherences, f)

    print('done : df.shape = {0}'.format(df.shape))
    return df, dikt_incoherences


