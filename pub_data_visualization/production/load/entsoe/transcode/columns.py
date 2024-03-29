
"""
    Connections between the names used by ENTSO-E
    and the user defined names.
    
"""

from ..... import global_var

columns = {'ActualConsumption'       : global_var.production_negative_part_mw,
           'ActualGenerationOutput'  : global_var.production_positive_part_mw,
           'AreaCode'                : global_var.geography_area_code,
           'AreaName'                : global_var.geography_area_name,
           'AreaTypeCode'            : global_var.geography_area_type_code,
           'DateTime'                : global_var.production_dt_utc,
           'Day'                     : global_var.production_day_utc,
           'GenerationUnitEIC'       : global_var.unit_eic,
           'InstalledGenCapacity'    : global_var.capacity_nominal_mw,
           'MapCode'                 : global_var.geography_map_code,
           'Month'                   : global_var.production_month_utc,
           'PowerSystemResourceName' : global_var.unit_name,
           'ProductionType'          : global_var.production_source,
           'ResolutionCode'          : global_var.time_resolution_code,
           'UpdateTime'              : global_var.publication_dt_utc,
           'Year'                    : global_var.production_year_utc,
           }