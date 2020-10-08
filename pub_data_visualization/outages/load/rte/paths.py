
"""
    Folders where the raw outages data provided by RTE
    and the transformed dataframes are saved.
    
"""

import os
#
from .... import global_var

folder_raw = os.path.join(global_var.path_public_data,
                          '24_RTE',
                          'DonneesIndisponibilitesProduction',
                          )
fpath_tmp = os.path.join(global_var.path_transformed,
                         'RTE',
                         'DonneesIndisponibilitesProduction',
                         'DonneesIndisponibilitesProduction_{map_code}_{file}',
                         )
