
import global_var


outage_status = {"Annulée"  : global_var.outage_status_cancelled,
                 "Terminée" : global_var.outage_status_finished,
                 "nan"      : global_var.outage_status_nan,
                 }