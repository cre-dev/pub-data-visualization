
"""
    Correspondances between the names of the statutes of outages 
    used by ENTSO-E and the user defined names.
    
"""

from ..... import global_var

outage_status = {'Active'    : global_var.outage_status_active,
                 'Cancelled' : global_var.outage_status_cancelled,
                 'Withdrawn' : global_var.outage_status_cancelled,
                 }


