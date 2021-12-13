"""
    Module to match the names of the columns.
    
    This module establishes the connections between the user defined names
    and the names used in V_ALLOCATION.
    
"""

from pub_data_visualization import global_var

columns = {
    'id': global_var.transmission_id,
    'periodFrom': global_var.transmission_begin_dt_local,
    'periodTo': global_var.transmission_end_dt_local,
    'pointLabel': global_var.geography_point,
    'operatorLabel' : global_var.transmission_tso,
    'directionKey': global_var.transmission_direction,
    'unit': global_var.transmission_unit,
    'value': global_var.transmission_value,
    'pointKey' : global_var.geography_point_type,
}

