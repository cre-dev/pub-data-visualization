
import os
#
from ..... import global_var


folder_raw = os.path.join(global_var.path_public_data,
                          '24_RTE',
                          'Centrales_production_reference',
                          )
fpath_tmp = os.path.join(global_var.path_transformed,
                         'RTE',
                         'Centrales_production_reference',
                         'Centrales_production_reference_{map_code}',
                         )