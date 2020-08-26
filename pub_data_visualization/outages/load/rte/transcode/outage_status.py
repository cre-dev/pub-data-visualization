
"""
    Correspondances between the names of the statutes of the outages 
    used by RTE and the user defined names.
"""

from ..... import global_var


outage_status = {"Annulée"  : global_var.outage_status_cancelled,
                 "Terminée" : global_var.outage_status_finished,
                 "nan"      : global_var.outage_status_nan,
                 }