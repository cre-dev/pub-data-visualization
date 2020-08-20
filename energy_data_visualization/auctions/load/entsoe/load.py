
import pandas as pd
import os
#
from .... import global_var, global_tools
from . import paths, transcode

def load(map_code = None):
    df_path = paths.fpath_tmp.format(map_code = map_code)
    try:
        print('Load auctions - ', end = '')
        df = pd.read_csv(df_path,
                         sep = ';',
                         )
        df.loc[:,global_var.contract_delivery_begin_dt_UTC]     = pd.to_datetime(df[global_var.contract_delivery_begin_dt_UTC])
        df.loc[:,global_var.contract_delivery_begin_date_UTC]   = pd.to_datetime(df[global_var.contract_delivery_begin_date_UTC])
        df.loc[:,global_var.auction_dt_UTC]                     = pd.to_datetime(df[global_var.auction_dt_UTC])
        df.loc[:,global_var.contract_delivery_begin_dt_local]   = df.apply(lambda row : row[global_var.contract_delivery_begin_dt_UTC].tz_convert(global_var.dikt_tz[row[global_var.geography_map_code]]), axis = 1)
        df.loc[:,global_var.contract_delivery_begin_date_local] = df.apply(lambda row : row[global_var.contract_delivery_begin_date_UTC].tz_convert(global_var.dikt_tz[row[global_var.geography_map_code]]), axis = 1)
        print('Loaded') 
    except FileNotFoundError:
        print('Not loaded')
        # Read
        dikt_prices = {}
        list_files  = sorted(os.listdir(paths.folder_raw))
        assert len(list_files) > 0, ('Files not found.\n'
                                     'They can be downloaded with the ENTSOE SFTP share\n'
                                     'and stored in\n'
                                     '{0}'.format(paths.folder_raw)
                                     )
        for ii, fname in enumerate(list_files):
            print('\r{0:4}/{1:4} - {2}'.format(ii,
                                               len(list_files),
                                               fname,
                                               ),
                  end = '',
                  )
            fpath = os.path.join(paths.folder_raw,
                                 fname,
                                 )
            dg = pd.read_csv(fpath,
                             encoding   = 'UTF-16 LE',
                             sep        = '\t',
                             decimal    = '.',
                             )
            dg = dg.rename(transcode.columns,
                           axis = 1,
                           )
            dg = dg[[
                     global_var.geography_map_code,
                     global_var.contract_delivery_begin_dt_UTC,
                     global_var.auction_price_euro_mwh,
                     ]]
            dg = dg[dg[global_var.geography_map_code].isin([map_code] if type(map_code) == str else map_code)]
            if dg.empty:
                continue
            dg[global_var.contract_delivery_begin_dt_UTC]     = pd.to_datetime(dg[global_var.contract_delivery_begin_dt_UTC]).dt.tz_localize('UTC')
            dg[global_var.contract_delivery_begin_dt_local]   = dg.apply(lambda row : row[global_var.contract_delivery_begin_dt_UTC].tz_convert(global_var.dikt_tz[row[global_var.geography_map_code]]), axis = 1)
            dg[global_var.contract_delivery_begin_date_local] = dg[global_var.contract_delivery_begin_dt_local].apply(lambda x : x.replace(hour = 0, minute = 0))
            dg[global_var.contract_delivery_begin_year_local] = dg[global_var.contract_delivery_begin_dt_local].apply(lambda x : x.timetuple().tm_year)
            dg[global_var.contract_delivery_begin_date_UTC]   = dg[global_var.contract_delivery_begin_date_local].apply(lambda x : x.tz_convert('UTC'))
            dg[global_var.contract_product]                   = global_var.contract_product_hour
            dg[global_var.contract_profile]                   = global_var.contract_profile_hour
            dg[global_var.contract_delivery_period_index]     = dg.apply(lambda row : global_tools.compute_delivery_period_index(product  = row[global_var.contract_product],
                                                                                                                                 tz_local = global_var.dikt_tz[row[global_var.geography_map_code]],
                                                                                                                                 delivery_begin_dt_local = row[global_var.contract_delivery_begin_dt_local],
                                                                                                                                 ),
                
                                                                          axis = 1,
                                                                          )
            dg[global_var.auction_dt_UTC] = dg[global_var.contract_delivery_begin_dt_local].apply(lambda x : x.replace(hour = 12).tz_convert('UTC'))
            dikt_prices[fname] = dg
        print('\nConcatenate')
        df = pd.concat([dikt_prices[key] 
                        for key in dikt_prices.keys()
                        ],
                       axis = 0,
                       sort = False,
                       )
        df = df.sort_values(global_var.contract_delivery_begin_dt_UTC,
                            axis = 0,
                            )
        df = df.reset_index(drop = True)
        # Save
        print('Save')
        os.makedirs(os.path.dirname(df_path),
                    exist_ok = True,
                    )
        df.to_csv(df_path,
                  sep   = ';',
                  index = False,
                  )

    
    print('done : df.shape = {0}'.format(df.shape))   
    return df

