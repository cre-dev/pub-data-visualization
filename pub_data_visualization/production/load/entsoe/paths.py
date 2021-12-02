"""
    Folders where the raw production data provided by ENTSO-E
    and the transformed dataframes are saved.
    
"""

import os
#
from .... import global_var

folder_raw = os.path.join(global_var.path_public_data,
                          '11_ENTSOE',
                          'ActualGenerationOutputPerGenerationUnit_16.1.A',
                          )
fpath_tmp = os.path.join(global_var.path_transformed,
                          'ENTSOE',
                          'ActualGenerationOutputPerGenerationUnit_16.1.A',
                          'ActualGenerationOutputPerGenerationUnit_16.1.A_{map_code}',
                          )
