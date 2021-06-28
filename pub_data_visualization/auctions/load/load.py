
import pandas as pd
#
from ... import global_var
from . import entsoe


def load(source   = None,
         map_code = None,
         date_min = None,
         date_max = None,
         ):
    """
        Calls the appropriate loader of the prices
        between two dates from the given data source.
 
        :param source: The data source
        :param map_code: The bidding zone
        :param date_min: The left bound
        :param date_max: The right bound
        :type source: string
        :type map_code: string
        :type date_min: pd.Timestamp
        :type date_max: pd.Timestamp
        :return: The selected auction prices
        :rtype: pd.DataFrame
    """
    
    if source == global_var.data_source_auctions_entsoe:
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

