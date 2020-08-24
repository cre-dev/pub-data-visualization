
"""
    Correspondances between the names used by eCO2mix
    and the user defined names.
"""

from ..... import global_var

columns = {'Périmètre'     : global_var.geography_area_name,
           'Nature'        : global_var.file_info,
           'AreaName'      : global_var.geography_area_name,
           'Date'          : global_var.load_date_local,
           'Heures'        : global_var.load_time_local,
           'Consommation'  : global_var.load_nature_observation_mw,
           'Prévision J-1' : global_var.load_nature_forecast_day1_mw,
           'Prévision J'   : global_var.load_nature_forecast_day0_mw,
           }