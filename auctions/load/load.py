
import pandas as pd
#
import global_var
from . import entsoe


def load(source   = None,
         map_code = None,
         date_min = None,
         date_max = None,
         ):
        
    if source == global_var.data_source_entsoe:
        dg = entsoe.load(map_code = map_code)
    
    else: 
        raise ValueError('Incorrect source : {0}'.format(source))

    dh = dg.loc[  pd.Series(True, index = dg.index)
                & ((dg[global_var.auction_dt_UTC] >= date_min) if bool(date_min) else True)
                & ((dg[global_var.auction_dt_UTC] <  date_max) if bool(date_max) else True)
                ]
    
    assert dh.shape[0] > 0
    assert dh.index.is_unique
    
    return dh

