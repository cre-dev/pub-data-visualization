
"""
    Folders where the raw production data provided by eCO2mix
    and the transformed dataframes are saved.
"""

import os
#
from .... import global_var

fpath_tmp = os.path.join(global_var.path_transformed,
                         'eCO2mix',
                         'production_{0}_{1}.csv',
                         )
