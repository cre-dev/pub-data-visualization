

import numpy as np
#
import global_var


company_name = {'EDF'                     : global_var.company_name_edf, 
                'ENGIE'                   : global_var.company_name_engie, 
                'UNIPER'                  : global_var.company_name_eon, 
                'GDF'                     : global_var.company_name_engie, 
                'PSS POWER'               : global_var.company_name_pss,
                'GAZEL ENERGIE'           : global_var.company_name_gazel,
                'CELEST POWER'            : global_var.company_name_gazel, 
                'ALPIQ'                   : global_var.company_name_alpiq, 
                'TOTAL RAFFINAGE FRANCE ' : global_var.company_name_total,
                'DIRECT ENERGIE'          : global_var.company_name_total, 
                'TOTAL DIRECT ENERGIE'    : global_var.company_name_total,
                np.nan                    : global_var.company_name_unknown,
                }