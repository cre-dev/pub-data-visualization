
"""
    Correspondances between the names of the types of outages 
    used by RTE and the user defined names.
"""
#
from ..... import global_var


unit_type = {"Groupe"   : global_var.unit_type_group,
             "Centrale" : global_var.unit_type_plant,
             }