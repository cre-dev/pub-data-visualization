
import os
#
import global_var

folder_raw = os.path.join(global_var.path_public_data,
                          '24_RTE',
                          'DonneesIndisponibilitesProduction',
                          )
fpath_tmp = os.path.join(global_var.path_transformed,
                         'RTE',
                         'DonneesIndisponibilitesProduction',
                         'DonneesIndisponibilitesProduction_{map_code}_{file}',
                         )
