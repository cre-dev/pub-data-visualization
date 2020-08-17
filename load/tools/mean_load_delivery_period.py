

import pandas as pd
#
import global_var


def mean_load_delivery_period(df,
                              product_delivery_windows,
                              ):

    load_windows = pd.concat([df.loc[begin:end]
                              for begin, end in product_delivery_windows
                              ],
                             axis = 0,
                             )
    mean_load = load_windows[global_var.load_mw].mean()

    return mean_load

