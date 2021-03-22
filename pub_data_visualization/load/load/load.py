
import pandas as pd
#
from ... import global_var
from . import eco2mix, entsoe


def load(source      = None,
         map_code    = None,
         date_min    = None,
         date_max    = None,
         ):
    """
        Calls the appropriate loader of the load data
        from the given data source,
        in a given area,
        and between two dates.
 
        :param source: The data source
        :param map_code: The delivery zone
        :param date_min: The left bound
        :param date_max: The right bound
        :type source: string
        :type map_code: string
        :type date_min: pd.Timestamp
        :type date_max: pd.Timestamp
        :return: The selected load data
        :rtype: pd.DataFrame
    """
    
    if source == global_var.data_source_eco2mix:
        df = eco2mix.load(map_code = map_code,
                          date_min = date_min,
                          date_max = date_max,
                          )
    
    elif source == global_var.data_source_entsoe:
        df = entsoe.load(map_code = map_code)
    
    else: 
        raise ValueError('Incorrect source : {0}'.format(source))
    
    ### Pivot
    dg = df.pivot_table(values  = global_var.quantity_value, 
                        index   = global_var.load_dt_UTC, 
                        columns = [global_var.geography_map_code,
                                   global_var.load_nature,
                                   ],
                        )
    dg = dg.reindex(sorted(dg.columns), axis = 1)
    dg = dg.sort_index()

    dh = dg.loc[  pd.Series(True, index = dg.index)
                & ((dg.index >= date_min) if bool(date_min) else True)
                & ((dg.index <  date_max) if bool(date_max) else True)
                ]
    
    assert dh.shape[0] > 0
    assert dh.index.is_unique

    return dh

