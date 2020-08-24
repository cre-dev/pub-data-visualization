

import pandas as pd
#
from ... import global_var


def mean_load_delivery_period(df,
                              product_delivery_windows,
                              ):
    """
        Computes the average load during
        the delivery windows of 
        a given contract.
 
        :param df: The load data
        :param product_delivery_windows: The delivery windows of the contract
        :type df: pd.DataFrame
        :type product_delivery_windows: list of pairs of pd.Timestamp
        :return: The average load
        :rtype: float
    """

    load_windows = pd.concat([df.loc[begin:end]
                              for begin, end in product_delivery_windows
                              ],
                             axis = 0,
                             )
    mean_load = load_windows[global_var.load_mw].mean()

    return mean_load

