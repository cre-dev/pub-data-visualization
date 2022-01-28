
"""
    Correspondances between the columns names used by ENTSO-E
    and the user defined names.
    
"""

from ...... import global_var

columns = {'AggregatedInstalledCapacity' : global_var.capacity_nominal_mw,
           'AreaCode'                    : global_var.geography_area_code,
           'AreaName'                    : global_var.geography_area_name,
           'AreaTypeCode'                : global_var.geography_area_type_code,
           'MapCode'                     : global_var.geography_map_code,
           'DateTime'                    : global_var.capacity_dt_utc,
           'Day'                         : global_var.capacity_day_utc,
           'DeletedFlag'                 : global_var.capacity_flag_deleted,
           'Month'                       : global_var.capacity_month_utc,
           'ProductionType'              : global_var.production_source,
           'ResolutionCode'              : global_var.time_resolution_code,
           'UpdateTime'                  : global_var.publication_dt_utc,
           'Year'                        : global_var.capacity_year_utc,
           }