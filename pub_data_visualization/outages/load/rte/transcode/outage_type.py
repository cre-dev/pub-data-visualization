
"""
    Correspondances between the names of the types of outages 
    used by RTE and the user defined names.
"""

from ..... import global_var


outage_type = {"Indisponibilité fortuite"           : global_var.outage_type_fortuitous,
               "Indisponibilité planifiée"          : global_var.outage_type_planned,
               }