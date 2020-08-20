
"""
Folders where the raw auctions data and the 
transformed dataframes are saved.
"""

import os
#
from .... import global_var


folder_raw = os.path.join(global_var.path_public_data,
                          '11_ENTSOE',
                          'DayAheadPrices',
                          )
fpath_tmp = os.path.join(global_var.path_transformed,
                         'ENTSOE',
                         'DayAheadPrices',
                         'DayAheadPrices_{map_code}.csv',
                         )