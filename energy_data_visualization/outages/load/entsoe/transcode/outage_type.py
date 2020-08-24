
"""
    Correspondances between the names of the types of outages 
    used by ENTSO-E and the user defined names.
"""

from ..... import global_var

outage_type = {'Forced'     : global_var.outage_type_fortuitous,
               'Planned'    : global_var.outage_type_planned,
               }


