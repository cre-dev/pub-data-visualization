

import os
#
from .... import global_var


folder_production_rte_raw = os.path.join(global_var.path_public_data,
                                        '24_RTE',
                                        'ProductionGroupe',
                                        )
fpath_production_rte_tmp = os.path.join(global_var.path_transformed,
                                        'RTE',
                                        'ProductionGroupe',
                                        )