
import os
#
from .... import global_var


folder_production_entsoe_raw = os.path.join(global_var.path_public_data,
                                        '11_ENTSOE',
                                        'ActualGenerationOutputPerUnit',
                                        )
fpath_production_entsoe_tmp = os.path.join(global_var.path_transformed,
                                        'ENTSOE',
                                        'ActualGenerationOutputPerUnit',
                                        'ActualGenerationOutputPerUnit_{map_code}',
                                        )