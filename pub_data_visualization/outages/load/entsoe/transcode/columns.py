
"""
    Correspondances between the names of the columns used by ENTSO-E
    and the user defined names.
    
"""

from ..... import global_var

columns = {'areacode'               : global_var.geography_area_code,
           'AreaCode'               : global_var.geography_area_code,
           'AreaName'               : global_var.geography_area_name,
           'AreaTypeCode'           : global_var.geography_area_type_code,
           'MapCode'                : global_var.geography_map_code,
           'AvailableCapacity'      : global_var.capacity_available_mw,
           'Day'                    : global_var.outage_begin_day_utc,
           'StartTS'                : global_var.outage_begin_dt_utc,
           'Month'                  : global_var.outage_begin_month_utc,
           'Year'                   : global_var.outage_begin_year_utc,
           'Reason'                 : global_var.outage_cause,
           'ReasonCode'             : global_var.outage_cause_code,
           'ReasonText'             : global_var.outage_cause_comments,
           'EndTS'                  : global_var.outage_end_dt_utc,
           'Status'                 : global_var.outage_status,
           'Type'                   : global_var.outage_type,
           'ProductionType'         : global_var.production_source,           
           'MRID'                   : global_var.publication_id,
           'UpdateTime'             : global_var.publication_dt_utc,
           'Version'                : global_var.publication_version,
           'TimeZone'               : global_var.time_zone,
           'PowerResourceEIC'       : global_var.unit_eic,
           'PowerRecourceEIC'       : global_var.unit_eic,
           'UnitName'               : global_var.unit_name,
           'InstalledGenCapacity'   : global_var.capacity_nominal_mw,
           'InstalledCapacity'      : global_var.capacity_nominal_mw,
           'VoltageConnectionLevel' : global_var.unit_voltage_connection,
           }


