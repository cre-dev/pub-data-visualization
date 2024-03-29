
"""
    Correspondances between the names used by ENTSO-E
    and the user defined names.
    
"""

from ..... import global_var

columns = {'AreaCode'                : global_var.geography_area_code,
           'AreaName'                : global_var.geography_area_name,
           'AreaTypeCode'            : global_var.geography_area_type_code,
           'DateTime'                : global_var.load_dt_utc,
           'Day'                     : global_var.load_day_utc,
           'GenerationUnitEIC'       : global_var.unit_eic,
           'InstalledGenCapacity'    : global_var.capacity_nominal_mw,
           'MapCode'                 : global_var.geography_map_code,
           'Month'                   : global_var.load_month_utc,
           'PowerSystemResourceName' : global_var.unit_name,
           'ResolutionCode'          : global_var.time_resolution_code,
           'TotalLoadValue'          : global_var.load_power_mw,
           'UpdateTime'              : global_var.publication_dt_utc,
           'Year'                    : global_var.load_year_utc,
           }