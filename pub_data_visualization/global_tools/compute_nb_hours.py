
import numpy  as np
import pandas as pd
#
from .. import global_var


def compute_nb_hours(product_delivery_windows,
                     frequency = None,
                     ):
    """
        Computes the number of hours of a given delivery contract.
 
        :param product_delivery_windows: The delivery windows
        :type product_delivery_windows: list of pairs of pd.Timestamp
        :return: The number of hours of the contract
        :rtype: int
    """
    if product_delivery_windows is None:
        return None
    
    for beginning, end in product_delivery_windows:
        assert type(beginning) == pd.Timestamp
        assert type(end)       == pd.Timestamp
    nb_seconds = np.sum([end - beginning
                         for beginning, end in product_delivery_windows
                         ]).total_seconds()
    assert (   nb_seconds % 1800 == 0
            or frequency in [global_var.contract_frequency_bow,
                             ]
            )
    nb_hours   = (nb_seconds/3600)
    nb_hours   = float(nb_hours)
    return nb_hours