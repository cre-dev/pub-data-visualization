
import os
#
from .... import global_var

folder_load_entsoe_raw = os.path.join(global_var.path_public_data,
                                      '11_ENTSOE',
                                      'ActualTotalLoad',
                                      )
fpath_load_entsoe_tmp = os.path.join(global_var.path_transformed,
                                     'ENTSOE',
                                     'ActualTotalLoad',
                                     'ActualTotalLoad_{map_code}',
                                     )