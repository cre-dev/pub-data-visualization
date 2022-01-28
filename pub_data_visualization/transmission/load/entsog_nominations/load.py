
import os
import numpy as np
import pandas as pd
import requests
import io
#
from pub_data_visualization import global_tools, global_var
from . import paths, query, transcode


def load(date_min = None,
         date_max = None,
         ):
    """
        Loads the nominated capacities from ENTSOG API.

        :param date_min: The left bound
        :param date_max: The right bound
        :type date_min: pd.Timestamp
        :type date_max: pd.Timestamp
        :return: The selected capacities
        :rtype: pd.DataFrame
    """

    df_path = os.path.join(paths.fpath_tmp,
                           '_'.join(filter(None, ['entsog_nominations',
                                                  date_min.strftime('%Y%m%d_%H%M') if bool(date_min) else '',
                                                  date_max.strftime('%Y%m%d_%H%M') if bool(date_max) else '',
                                                  ])))
    try:
        print('Load df_nominations - ', end='')
        df = pd.read_csv(df_path,
                         sep=';',
                         )
        df.loc[:,global_var.transmission_begin_dt_utc]    = pd.to_datetime(df[global_var.transmission_begin_dt_utc])
        df.loc[:,global_var.transmission_end_dt_utc]      = pd.to_datetime(df[global_var.transmission_end_dt_utc])
        df.loc[:, global_var.transmission_begin_dt_local] = df[global_var.transmission_begin_dt_utc].dt.tz_convert('CET')
        df.loc[:, global_var.transmission_end_dt_local]   = df[global_var.transmission_end_dt_utc].dt.tz_convert('CET')
        print('Loaded')
    except FileNotFoundError:
        print('Not loaded')

        ### URL Connection
        api_query = query.entsog_nominations(date_min = date_min,
                                             date_max = date_max,
                                             )
        response = requests.get(api_query)
        response.raise_for_status()
        data = response.content
        df   = pd.read_csv(io.StringIO(data.decode('utf-8')))

        ### Columns
        assert set(df.columns) == set(transcode.columns).union(transcode.columns_dropped)
        df = df.drop(transcode.columns_dropped, axis=1)
        df = df.rename(transcode.columns, axis=1)
        if df.empty: return df

        ### Datetimes
        df[global_var.transmission_begin_dt_local] = pd.to_datetime(df[global_var.transmission_begin_dt_local]).dt.tz_localize('CET')
        df[global_var.transmission_end_dt_local]   = pd.to_datetime(df[global_var.transmission_end_dt_local]).dt.tz_localize('CET') + pd.Timedelta(seconds = 1)
        df[global_var.transmission_begin_dt_utc] = df[global_var.transmission_begin_dt_local].dt.tz_convert('UTC')
        df[global_var.transmission_end_dt_utc]   = df[global_var.transmission_end_dt_local].dt.tz_convert('UTC')

        # Power units
        assert set(df[global_var.transmission_unit].unique()) == {'kWh/d'}
        df[global_var.transmission_power_mwh_d] = df[global_var.transmission_value]/1e3

        # Additional infos
        df[global_var.data_source_transmission] = global_var.data_source_transmission_entsog_nominations
        df[global_var.commodity]                = global_var.commodity_gas

        # Drop
        df.drop([global_var.transmission_unit,
                 global_var.transmission_value,
                 ],
                axis=1,
                inplace=True,
                )

        # Save
        print('Save')
        os.makedirs(os.path.dirname(df_path),
                    exist_ok=True,
                    )
        df.to_csv(df_path,
                  sep=';',
                  index=False,
                  )
    print('done : df.shape = {0}'.format(df.shape))
    return df

