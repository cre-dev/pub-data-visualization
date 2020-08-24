
"""
    Correspondances between the names used by ENTSO-E
    and the user defined names.
"""

from ..... import global_var

columns = {'ActualConsumption'       : global_var.production_negative_part_mw,
           'ActualGenerationOutput'  : global_var.production_positive_part_mw,
           'AreaCode'                : global_var.geography_area_code,
           'AreaName'                : global_var.geography_area_name,
           'AreaTypeCode'            : global_var.geography_area_type_code,
           'DateTime'                : global_var.production_dt_UTC,
           'Day'                     : global_var.production_day_UTC,
           'GenerationUnitEIC'       : global_var.unit_eic,
           'InstalledGenCapacity'    : global_var.unit_nameplate_capacity,
           'MapCode'                 : global_var.geography_map_code,
           'Month'                   : global_var.production_month_UTC,
           'PowerSystemResourceName' : global_var.unit_name,
           'ProductionTypeName'      : global_var.production_source,
           'ResolutionCode'          : global_var.time_resolution_code,
           'UpdateTime'              : global_var.publication_dt_UTC,
           'Year'                    : global_var.production_year_UTC,
           }