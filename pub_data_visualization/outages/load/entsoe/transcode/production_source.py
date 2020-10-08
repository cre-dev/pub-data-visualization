
"""
    Correspondances between the names of the energy production sources 
    used by ENTSO-E and the user defined names.
    
"""

from ..... import global_var

production_source = {'Biomass '                         : global_var.production_source_biomass,
                     'Fossil Hard coal '                : global_var.production_source_fossil_coal,
                     'Fossil Gas '                      : global_var.production_source_fossil_gas,
                     'Fossil Oil '                      : global_var.production_source_fossil_oil,
                     'Hydro Pumped Storage '            : global_var.production_source_hydro_pumped_storage,
                     'Hydro Water Reservoir '           : global_var.production_source_hydro_reservoir,
                     'Hydro Run-of-river and poundage ' : global_var.production_source_hydro_run_of_river,
                     'Marine '                          : global_var.production_source_marine,  
                     'Nuclear '                         : global_var.production_source_nuclear,
                     'Other '                           : global_var.production_source_other,           
                     }


