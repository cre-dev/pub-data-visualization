
"""
    Correspondances between the names of the operating companies 
    used by RTE and the user defined names.
    
"""

import numpy as np
#
from ..... import global_var


producer_name = {'EDF'                     : global_var.producer_name_edf, 
                 'ENGIE'                   : global_var.producer_name_engie, 
                 'UNIPER'                  : global_var.producer_name_eon, 
                 'GDF'                     : global_var.producer_name_engie, 
                 'PSS POWER'               : global_var.producer_name_pss,
                 'GAZEL ENERGIE'           : global_var.producer_name_gazel,
                 'CELEST POWER'            : global_var.producer_name_gazel, 
                 'ALPIQ'                   : global_var.producer_name_alpiq, 
                 'TOTAL RAFFINAGE FRANCE ' : global_var.producer_name_total,
                 'DIRECT ENERGIE'          : global_var.producer_name_total, 
                 'TOTAL DIRECT ENERGIE'    : global_var.producer_name_total,
                 np.nan                    : global_var.producer_name_unknown,
                 }