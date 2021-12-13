
import pandas as pd
#
from ... import global_var
from . import entsog_nominations


def load(source            = None,
         date_min          = None,
         date_max          = None,
         ):
    """
        Calls the appropriate loader
        of the transmission data
        from the given data source.
 
        :param source: The data source
        :param date_min: The left bound
        :param date_max: The right bound
        :type source: string
        :type date_min: pd.Timestamp
        :type date_max: pd.Timestamp
        :return: The selected transmission data
        :rtype: pd.DataFrame
    """
    
    if source == global_var.data_source_transmission_entsog_nominations:
        df = entsog_nominations.load(date_min = date_min,
                                     date_max = date_max,
                                     )
    
    else: 
        raise ValueError

    # Sort
    assert not set(col_orders).difference((df.columns))
    dg = df.reindex(col_orders+[col for col in df.columns if col not in col_orders], axis = 1)
    dg = dg.sort_values([global_var.transmission_begin_dt_local,
                         global_var.transmission_end_dt_local,
                         #global_var.geography_zone,
                         global_var.geography_point_type,
                         global_var.geography_point,
                         global_var.transmission_direction,
                         ])
    dg = dg.reset_index(drop = True)

    # Filter
    dh = dg.loc[  pd.Series(True, index = dg.index)
                & ((dg[global_var.transmission_end_dt_local]   >= date_min) if bool(date_min) else True)
                & ((dg[global_var.transmission_begin_dt_local] <  date_max) if bool(date_max) else True)
                ]

    # Checks
    assert dh.shape[0] > 0

    return dh

col_orders = [
    #global_var.geography_zone,
    global_var.geography_point_type,
    global_var.geography_point,
    global_var.transmission_direction,
    global_var.transmission_begin_dt_local,
    global_var.transmission_end_dt_local,
    global_var.transmission_power_mwh_d,
    global_var.transmission_tso,
    global_var.commodity,
    global_var.data_source_transmission,
    global_var.transmission_id,
    #global_var.geography_zone_info,
]


