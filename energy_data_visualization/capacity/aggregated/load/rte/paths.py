
import os
#
from ..... import global_var


folder_raw = os.path.join(global_var.path_public_data,
                          '24_RTE',
                          'Capacite_installee_production',
                          )
fpath_tmp = os.path.join(global_var.path_transformed,
                         'RTE',
                         'Capacite_installee_production',
                         'Capacite_installee_production_{map_code}.csv',
                         )