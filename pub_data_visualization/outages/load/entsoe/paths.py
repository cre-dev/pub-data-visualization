"""
    Folders where the raw outages data provided by ENTSO-E
    and the transformed dataframes are saved.
    
"""

import os
#
from .... import global_var

folder_raw = os.path.join(global_var.path_public_data,
                          '11_ENTSOE',
                          'Outages',
                          )
fpath_tmp = os.path.join(global_var.path_transformed,
                         'ENTSOE',
                         'Outages',
                         'Outages_{map_code}_{file}',
                         )
