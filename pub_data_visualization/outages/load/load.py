
import pandas as pd
#
from ... import global_var
from . import entsoe, rte


def load(source             = None,
         map_code           = None,
         producer           = None,
         unit_name          = None,
         production_source  = None,
         publication_dt_min = None,
         publication_dt_max = None,
         ):
    """
        Calls the appropriate loader of the outages data.
 
        :param source: The data source
        :param map_code: The delivery zone
        :param producer: The operator of the production assets
        :param unit_name: The names of the production assets
        :param production_source: The energy source of the production assets
        :param publication_dt_min: The left bound of the publications
        :param publication_dt_max: The right bound of the publications
        :type source: string
        :type map_code: string
        :type producer: string
        :type unit_name: string
        :type production_source: string
        :type publication_dt_min: pd.Timestamp
        :type publication_dt_max: pd.Timestamp
        :return: The selected outages data
        :rtype: pd.DataFrame
    """
    
    if source == global_var.data_source_outages_rte:
        df, dikt_incoherences = rte.load(map_code = map_code)
        
    elif source == global_var.data_source_outages_entsoe:
        df = entsoe.load(map_code = map_code)
    
    else: 
        raise ValueError('Incorrect source : {0}'.format(source))

    # Format
    df = df.set_index([global_var.publication_id,
                       global_var.publication_version, 
                       global_var.publication_dt_utc, 
                       ], 
                      drop = True,
                      )

    # Filter
    df = df[col_order]
    dg = df.loc[  pd.Series(True, index = df.index)
                & ((df[global_var.producer_name]    .isin([producer]          if type(producer)          == str else producer))          if bool(producer)            else True)
                & ((df[global_var.production_source].isin([production_source] if type(production_source) == str else production_source)) if bool(production_source)  else True)
                & ((df[global_var.unit_name]        .isin([unit_name]         if type(unit_name)         == str else unit_name))         if bool(unit_name)          else True)
                & ((df[global_var.publication_dt_utc] >= publication_dt_min)                                                             if bool(publication_dt_min) else True)
                & ((df[global_var.publication_dt_utc] <  publication_dt_max)                                                             if bool(publication_dt_max) else True)
                ]

    # Checks
    assert dg.shape[0] > 0
    
    return dg


col_order = [
global_var.outage_begin_dt_utc,
global_var.outage_end_dt_utc,
global_var.unit_name,
global_var.capacity_available_mw,
global_var.capacity_nominal_mw,
global_var.producer_name,
global_var.geography_map_code,
global_var.production_source,
global_var.publication_creation_dt_utc,
global_var.outage_type,
global_var.outage_cause,
global_var.outage_status,
global_var.file_name,
]   
