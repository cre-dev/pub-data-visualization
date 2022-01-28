
import pandas as pd
#
from ... import global_var
from . import entsoe_da


def load(source   = None,
         date_min = None,
         date_max = None,
         **kwargs,
         ):
    """
        Calls the appropriate loader of indices from the given data source.
 
        :param source: The data source
        :param date_min: The left bound
        :param date_max: The right bound
        :param kwargs: Additional kwargs
        :type source: string
        :type date_min: pd.Timestamp
        :type date_max: pd.Timestamp
        :type kwargs: dict
        :return: The selected indices
        :rtype: pd.DataFrame
    """
    
    if source == global_var.data_source_auctions_entsoe:
        dg = entsoe_da.load(**kwargs)
    
    else: 
        raise ValueError('Incorrect data source : {0}'.format(source))

    dh = dg.loc[  pd.Series(True, index = dg.index)
                & ((dg[global_var.auction_dt_UTC] >= date_min) if bool(date_min) else True)
                & ((dg[global_var.auction_dt_UTC] <  date_max) if bool(date_max) else True)
                ]
    
    assert dh.shape[0] > 0
    assert dh.index.is_unique
    
    return dh

