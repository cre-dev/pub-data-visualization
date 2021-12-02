
import pandas as pd
#
from ... import global_var
from . import eco2mix, entsoe, rte


def load(source            = None,
         map_code          = None,
         date_min          = None,
         date_max          = None,
         ):
    """
        Calls the appropriate loader of the production data
        from the given data source,
        in a given delivery_zone,
        and between two dates.
 
        :param source: The data source
        :param map_code: The bidding zone
        :param date_min: The left bound
        :param date_max: The right bound
        :type source: string
        :type map_code: string
        :type date_min: pd.Timestamp
        :type date_max: pd.Timestamp
        :return: The selected production data
        :rtype: pd.DataFrame
    """
    
    if source == global_var.data_source_production_eco2mix:
        df = eco2mix.load(map_code = map_code,
                             date_min = date_min,
                             date_max = date_max,
                             )
    
    elif source == global_var.data_source_production_rte:
        df = rte.load()
        
    elif source == global_var.data_source_production_entsoe:
        df = entsoe.load(map_code = map_code)
    
    else: 
        raise ValueError

    assert set(df.columns) == {global_var.commodity,
                               global_var.geography_map_code,
                               global_var.production_dt_UTC,
                               global_var.production_nature,
                               global_var.production_power_mw,
                               global_var.production_source,
                               global_var.unit_name,
                               }

    # Sort
    dg = df.reindex(sorted(df.columns), axis = 1)
    dg = dg.set_index(global_var.production_dt_UTC)
    dg = dg.sort_index()
    dg[global_var.production_power_gw] = dg[global_var.production_power_mw]/1e3

    # Filter
    dh = dg.loc[  pd.Series(True, index = dg.index)
                & ((dg.index >= date_min) if bool(date_min) else True)
                & ((dg.index <  date_max) if bool(date_max) else True)
                ]

    # Checks
    assert dh.shape[0] > 0
    assert not dh.reset_index()[[global_var.production_dt_UTC,global_var.unit_name]].duplicated().sum()

    return dh


