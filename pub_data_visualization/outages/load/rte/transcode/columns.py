
"""
    Correspondances between the names of the columns 
    used by RTE and the user defined names.
    
"""

#
from ..... import global_var


columns = {"Nom du producteur"                : global_var.producer_name,
           "Début Période"                    : global_var.outage_period_begin_dt_local,
           "Fin Période"                      : global_var.outage_period_end_dt_local,
           "Puissance disponible restante"    : global_var.capacity_available_mw,
           "Début indispo"                    : global_var.outage_begin_dt_local,
           "Cause"                            : global_var.outage_cause,
           "Fin Indispo"                      : global_var.outage_end_dt_local,
           "Statut"                           : global_var.outage_status,
           "Type d'indisponibilité"           : global_var.outage_type,
           "Filière"                          : global_var.production_source,
           "Création"                         : global_var.publication_creation_dt_local,
           "Mise à jour"                      : global_var.publication_dt_local,
           "ID Indisponibilité de production" : global_var.publication_id,
           "Version"                          : global_var.publication_version,
           "Nom de l'unité"                   : global_var.unit_name,            
           "Puissance nominale"               : global_var.capacity_nominal_mw,
           "Type de l'unité de production"    : global_var.unit_type,
           }