
import os
#
import global_var

website   = 'https://eco2mix.rte-france.com/download/eco2mix/'
fname_zip = 'eCO2mix_RTE_Annuel-Definitif_{year}.zip'
fname_xls = 'eCO2mix_RTE_Annuel-Definitif_{year}.xls'

folder_raw = os.path.join(global_var.path_public_data,
                          '24_RTE',
                          'eCO2mix_RTE',
                          )