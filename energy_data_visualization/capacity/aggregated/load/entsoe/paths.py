
import os
#
from ..... import global_var



folder_raw = os.path.join(global_var.path_public_data,
                          '11_ENTSOE',
                          'InstalledGenerationCapacityAggregated',
                          )
fpath_tmp = os.path.join(global_var.path_transformed,
                         'ENTSOE',
                         'InstalledGenerationCapacityAggregated',
                         'InstalledGenerationCapacityAggregated_{map_code}',
                         )