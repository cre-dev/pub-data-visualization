
"""
    Correspondances between the names used by ENTSO-E
    for the columns and the user defined names.
    
"""

from ..... import global_var

columns = {'AreaCode'       : global_var.geography_area_code,
           'AreaTypeCode'   : global_var.geography_area_type_code,
           'AreaName'       : global_var.geography_area_name,
           'Currency'       : global_var.currency,
           'Day'            : global_var.contract_delivery_begin_day_utc,
           'DateTime'       : global_var.contract_delivery_begin_dt_utc,
           'Month'          : global_var.contract_delivery_begin_month_utc,
           'Year'           : global_var.contract_delivery_begin_year_utc,
           'MapCode'        : global_var.geography_map_code,
           'Price'          : global_var.auction_price_euro_mwh,
           'UpdateTime'     : global_var.publication_dt_utc,
           'ResolutionCode' : global_var.time_resolution_code,
           }