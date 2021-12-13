"""
    Folders where transformed dataframes are saved.

"""

import os
#
from pub_data_visualization import global_var

fpath_tmp = os.path.join(global_var.path_transformed,
                         'transmission',
                         'sql_allocation',
                         'df_{0}_{1}.csv',
                         )