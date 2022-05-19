
"""
    Matching between the names of the energy production sources
    used by RTE and the user defined names.
    
"""

from ..... import global_var


production_source = {'Autre'                              : global_var.production_source_other,
                     'Biomasse'                           : global_var.production_source_biomass,
                     'Charbon'                            : global_var.production_source_fossil_coal,
                     'Fioul'                              : global_var.production_source_fossil_oil,
                     'Fioul et pointe'                    : global_var.production_source_fossil_oil,
                     'Gaz'                                : global_var.production_source_fossil_gas,
                     'Hydraulique STEP'                   : global_var.production_source_hydro_pumped_storage,
                     "Hydraulique fil de l'eau / éclusée" : global_var.production_source_hydro_run_of_river,
                     "Hydraulique fil et éclusée"         : global_var.production_source_hydro_run_of_river,
                     'Hydraulique lac'                    : global_var.production_source_hydro_reservoir,
                     'Hydraulique lacs'                   : global_var.production_source_hydro_reservoir,
                     'Nucléaire'                          : global_var.production_source_nuclear,
                     }