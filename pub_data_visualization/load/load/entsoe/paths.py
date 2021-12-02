"""
    Folders where the raw load data provided by ENTSO-E
    and the transformed dataframes are saved.
    
"""

import os
#
from .... import global_var

folder_raw = os.path.join(global_var.path_public_data,
                          '11_ENTSOE',
                          'ActualTotalLoad_6.1.A',
                          )

fpath_tmp = os.path.join(global_var.path_transformed,
                         'ENTSOE',
                         'ActualTotalLoad_6.1.A',
                         'ActualTotalLoad_6.1.A_{map_code}',
                         )
