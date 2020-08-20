

#
from ..... import global_var


production_source = {'Autre'                              : global_var.production_source_other,
                     'Biomasse'                           : global_var.production_source_biomass,
                     'Charbon'                            : global_var.production_source_fossil_coal,
                     'Gaz'                                : global_var.production_source_fossil_gas,
                     'Fioul'                              : global_var.production_source_fossil_oil,
                     'Hydraulique STEP'                   : global_var.production_source_hydro_pumped_storage,
                     'Hydraulique lacs'                   : global_var.production_source_hydro_reservoir,
                     "Hydraulique fil de l'eau / éclusée" : global_var.production_source_hydro_run_of_river,
                     'Marin'                              : global_var.production_source_marine,  
                     'nan'                                : global_var.production_source_unknown,
                     'Nucléaire'                          : global_var.production_source_nuclear,
                     }