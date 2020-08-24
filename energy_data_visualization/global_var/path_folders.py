
"""
    Definition of :
        - the folders to read and save the data
        - the folders where the plots should be save
    Although a default configuration is proposed,
    the user can decide her own folders by creating 
    a module pers_var.py in this folder.
"""

import os

###############################################################################
path_home = r'{0}'.format(os.path.expanduser('~'))
###############################################################################

try: # Local non-synchronized file for personal folders path
    from .pers_var import path_public_data 
    from .pers_var import path_private_data
    from .pers_var import path_transformed
    from .pers_var import path_plots
    from .pers_var import path_outputs
    assert os.path.isdir(path_public_data)
    
except (ModuleNotFoundError, AssertionError):
    path_public_data = os.path.join(path_home,
                                    r'_energy_public_data',
                                    )
    path_private_data = os.path.join(path_home,
                                     r'_energy_private_data',
                                     )
    path_transformed = os.path.join(path_home, 
                                    r'_energy__tmp_data',
                                    )
    path_plots       = os.path.join(path_home, 
                                    r'_energy_plots',
                                    )
    path_outputs     = os.path.join(path_home, 
                                    r'_energy_outputs',
                                    )

