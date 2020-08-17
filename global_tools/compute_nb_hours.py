
import numpy  as np
import pandas as pd


def compute_nb_hours(product_delivery_windows):
    for beginning, end in product_delivery_windows:
        assert type(beginning) == pd.Timestamp
        assert type(end)       == pd.Timestamp
    nb_seconds = np.sum([end - beginning
                         for beginning, end in product_delivery_windows
                         ]).total_seconds()
    assert nb_seconds % 3600 == 0
    nb_hours   = (nb_seconds/3600)
    nb_hours   = int(nb_hours)
    return nb_hours