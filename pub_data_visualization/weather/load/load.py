
import pandas as pd
#
from ... import global_var
from . import meteofrance


def load(source   = global_var.data_source_weather_meteofrance,
         zone     = global_var.geography_zone_france,
         date_min = pd.Timestamp('2015').tz_localize('CET'),
         date_max = pd.Timestamp('{}'.format(pd.Timestamp.now().year)).tz_localize('CET'),
         ):
    """
        Calls the appropriate loader of the weather data
        between two dates in the given zone.
 
        :param source: The data source
        :param zone: The selected zone
        :param date_min: The left bound
        :param date_max: The right bound
        :type source: string
        :type zone: string
        :type date_min: pd.Timestamp
        :type date_max: pd.Timestamp
        :return: The selected weather data
        :rtype: pd.DataFrame
    """
    
    if source == global_var.data_source_weather_meteofrance:
        df, coordinates_weather, trash_weather = meteofrance.load(zone     = zone,
                                                                  date_min = date_min,
                                                                  date_max = date_max,
                                                                  )
    
    else: 
        raise ValueError('Incorrect source : {0}'.format(source))

    assert set(df.columns) == {global_var.weather_physical_quantity,
                               global_var.weather_physical_quantity_value,
                               global_var.weather_dt_utc,
                               global_var.weather_nature,
                               global_var.weather_site_name,
                               }

    # Drop locations and average
    dg = df.drop(global_var.weather_site_name, axis = 1)
    dg = dg.groupby([global_var.weather_dt_utc,
                     global_var.weather_nature,
                     global_var.weather_physical_quantity,
                     ]).mean().reset_index()

    # Format
    dg = dg.set_index(global_var.weather_dt_utc)
    dg = dg.reindex(sorted(dg.columns), axis = 1)
    dg = dg.sort_index()

    # Filter
    dh = dg.loc[  pd.Series(True, index = dg.index)
                & ((dg.index >= date_min) if bool(date_min) else True)
                & ((dg.index <  date_max) if bool(date_max) else True)
                ]

    # Checks
    assert dh.shape[0] > 0
    assert not dh.reset_index()[[global_var.weather_dt_utc,global_var.weather_physical_quantity]].duplicated().sum()

    return dh


