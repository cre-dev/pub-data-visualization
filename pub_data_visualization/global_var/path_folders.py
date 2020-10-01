
"""
    Definition of the paths to the data.

    Definition of
    the folders to read and save the data
    and the folders where the plots should be saved.
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
    from .pers_var import path_transformed
    from .pers_var import path_outputs
    from .pers_var import path_plots
    assert os.path.isdir(path_public_data)
    
except (ModuleNotFoundError, AssertionError):
    path_public_data = os.path.join(path_home,
                                    r'_energy_public_data',
                                    )
    path_transformed = os.path.join(path_home, 
                                    r'_energy_tmp_data',
                                    )
    path_outputs     = os.path.join(path_home, 
                                    r'_energy_outputs',
                                    )
    path_plots       = os.path.join(path_home, 
                                    r'_energy_plots',
                                    )

