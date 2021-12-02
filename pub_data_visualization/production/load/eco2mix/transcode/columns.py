
"""
    Correspondances between the names used by eCO2mix
    and the user defined names.
    
"""

from ..... import global_var

columns = {'Périmètre'     : global_var.geography_area_name,
           'Nature'        : global_var.file_info,
           'Date'          : global_var.production_date_local,
           'Heures'        : global_var.production_time_local,
           'Consommation'  : global_var.load_nature_observation,
           'Prévision J-1' : global_var.load_nature_forecast_day1,
           'Prévision J'   : global_var.load_nature_forecast_day0,
           }