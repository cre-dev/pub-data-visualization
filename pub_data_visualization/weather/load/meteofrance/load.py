
import numpy as np
import pandas as pd
import os
import pickle
import shutil
import urllib
import gzip
#
from .... import global_var
from . import geography, paths, transcode, url

###############################################################################

def download_raw_weather_data(year  = None,
                              month = None,
                              ):
    """
        Downloads the weather data provided by Météo-France.
 
        :param year: The selected year
        :param month: The selected month
        :type year: int
        :type month: int
        :return: None
        :rtype: None
    """
    assert type(year)  == int and year > 2000, year
    assert type(month) == int and month in np.arange(1,13), month
    os.makedirs(paths.folder_weather_meteofrance_raw,
                exist_ok = True,
                )
    gzip_file_url = urllib.parse.urljoin(url.dikt['weather'],
                                         paths.dikt_files['weather.file_year_month'].format(year = year, month = month),
                                         ) + '.csv.gz'
    gz_file_path  = os.path.join(paths.folder_weather_meteofrance_raw,
                                 paths.dikt_files['weather.file_year_month'].format(year = year, month = month),
                                 ) + '.csv.gz'
    urllib.request.urlretrieve(gzip_file_url,
                               gz_file_path,
                               )
    csv_file_path = os.path.join(paths.folder_weather_meteofrance_raw,
                                 paths.dikt_files['weather.file_year_month'].format(year = year, month = month),
                                 ) + '.csv'
    with gzip.open(gz_file_path, 'rb') as f_in:
        with open(csv_file_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


def read_raw_weather_data(year  = None,
                          month = None,
                          ):
    """
        Reads the weather data provided by Météo-France.
 
        :param year: The selected year
        :param month: The selected month
        :type year: int
        :type month: int
        :return: The selected weather data
        :rtype: pd.DataFrame
    """
    assert type(year)  == int and year > 2000, year
    assert type(month) == int and month in np.arange(1,13), month
    csv_file_path = os.path.join(paths.folder_weather_meteofrance_raw,
                                 paths.dikt_files['weather.file_year_month'].format(year = year, month = month),
                                 ) + '.csv'    
    df        = pd.read_csv(csv_file_path,
                            sep = ';',
                            na_values = ['mq'],
                            )
    df = df.rename(transcode.columns, 
                   axis = 1,
                   )
    df[global_var.weather_dt_UTC] = pd.to_datetime(df[global_var.weather_dt_UTC], 
                                                   format = '%Y%m%d%H%M%S',
                                                   ).dt.tz_localize('UTC')
    df.drop_duplicates(subset  = [global_var.weather_dt_UTC, global_var.weather_site_id],
                       inplace = True,
                       keep    = 'first',
                       )
    df = df.set_index([global_var.weather_dt_UTC, global_var.weather_site_id])
    df[global_var.weather_temperature_celsius] = df[global_var.weather_temperature_kelvin] - 273.15
    df = df[[global_var.weather_temperature_celsius, global_var.weather_nebulosity, global_var.weather_wind_speed]]
    df = df.astype(float)
    df = df.unstack()
    df = df.swaplevel(0,1, axis = 1)
    df.columns.names = [global_var.weather_site_id, global_var.weather_physical_quantity]
    return df


def correct_filter_weather(df_weather):
    """
        Finds and tries to corrects anomalies in
        the weather data provided by Météo-France.
 
        :param df_weather: The weather data frame
        :type df_weather: pd.DataFrame
        :return: The corrected weather data frame
        :rtype: pd.DataFrame
    """
    # Some series start with a few Nan so correct them or drop them
    length_missing_data_beginning = (1 - pd.isnull(df_weather)).idxmax(axis = 0) - df_weather.index[0]
    dropped_columns               = df_weather.columns[length_missing_data_beginning > pd.to_timedelta(24, unit='h')].remove_unused_levels()#.levels[0]
    df_weather                    = df_weather.drop(columns = dropped_columns)
    trash_weather                 = list(dropped_columns.levels[0])
    df_weather.columns            = df_weather.columns.remove_unused_levels()
    # Drop the stations that do not have all the physical quantities
    for station in (df_weather.columns.levels[0]).copy():
        if df_weather[station].columns.shape[0] < df_weather.columns.levels[1].shape[0]:
            df_weather = df_weather.drop(columns = station, level = 0)
            trash_weather.append(station)
    # Backfill the rest
    df_weather.fillna(method = 'bfill', axis = 0, inplace = True)    
    assert df_weather.shape[1] % df_weather.columns.levels[1].shape[0] == 0, (df_weather.shape[1], df_weather.columns.levels[1].shape[0])
    return df_weather, sorted(set(trash_weather))

###############################################################################

def download_weather_description():
    """
        Downloads the description of the weather data provided by Météo-France.
 
        :return: None
        :rtype: None
    """
    os.makedirs(paths.folder_weather_meteofrance_raw, exist_ok = True)
    csv_file_path = os.path.join(paths.folder_weather_meteofrance_raw,
                                 paths.dikt_files['weather.description'],
                                 ) + '.csv'
    csv_file_url  = urllib.parse.urljoin(url.dikt['weather.stations'],
                                         paths.dikt_files['weather.description'],
                                         ) + '.csv'
    urllib.request.urlretrieve(csv_file_url,
                               csv_file_path,
                               )

def read_weather_description():
    """
        Reads the description of the weather data provided by Météo-France.
 
        :return: The coordinates of the weather stations
        :rtype: pd.DataFrame
    """
    csv_file_path = os.path.join(paths.folder_weather_meteofrance_raw,
                                 paths.dikt_files['weather.description'],
                                 ) + '.csv'
    df        = pd.read_csv(csv_file_path,
                            sep = ';',
                            )
    df = df.rename(transcode.columns,
                   axis = 1,
                   )
    df = df.set_index(global_var.weather_site_id)
    return df

def load_weather_description():
    """
        Downloads and reads the description 
        of the weather data provided by Météo-France.
 
        :return: None
        :rtype: None
    """
    try:
        weather_description = read_weather_description()
    except FileNotFoundError:
        download_weather_description()
        weather_description = read_weather_description()
    return weather_description

###############################################################################

def load(zone     = None,
         date_min = None,
         date_max = None,
         ):
    """
        Loads the weather data provided by Météo-France
        between two dates in a given zone.
 
        :param zone: The selected zone
        :param date_min: The left bound
        :param date_max: The right bound
        :type zone: string
        :type date_min: pd.Timestamp
        :type date_max: pd.Timestamp
        :return: The weather data
        :rtype: pd.DataFrame
    """

    fname_weather = os.path.join(paths.fpath_weather_meteofrance_tmp, 
                                 'df_weather_{0}_{1}.csv'.format(date_min.year,
                                                                 (date_max-pd.DateOffset(nanosecond = 1)).year,
                                                                 )
                                 )
    fname_trash   = os.path.join(paths.fpath_weather_meteofrance_tmp,
                                 'trash_weather_{0}_{1}.pkl'.format(date_min.year,
                                                                    (date_max-pd.DateOffset(nanosecond = 1)).year,
                                                                    )
                                 )
    weather_description = load_weather_description()
    try:
        print('Load weather_data - ', end = '')
        df_weather = pd.read_csv(fname_weather,
                                 sep       = ';',
                                 )
        df_weather.loc[:,global_var.weather_dt_UTC] = pd.to_datetime(df_weather[global_var.weather_dt_UTC])
        with open(fname_trash, 'rb') as f:
            trash_weather = pickle.load(f)
        print('Loaded df_weather and trash_weather')
    except Exception:
        print('fail - has to read raw data')
        dikt_weather = {}
        for year in range(date_min.year,
                          (date_max-pd.DateOffset(nanosecond = 1)).year+1,
                          ):
            for month in range(1,13):
                try:
                    print('\ryear = {0:2} - month = {1:2}'.format(year, month), end = '')
                    try:
                        dikt_weather[year, month] = read_raw_weather_data(year = year, month = month)
                    except FileNotFoundError:
                        download_raw_weather_data(year = year, month = month)
                        dikt_weather[year, month] = read_raw_weather_data(year = year, month = month)
                except Exception as e:
                    print('\n{0}'.format(e))
                    break
            else:
                continue
            break
        else:
            print()
        df_weather = pd.concat([dikt_weather[year,month]
                                for year, month in dikt_weather.keys()
                                ], 
                               axis = 0,
                               )
        df_weather = df_weather.dropna(axis = 1, how = 'all')
        df_weather.columns = df_weather.columns.set_levels([weather_description[global_var.weather_site_name][e] 
                                                            for e in df_weather.columns.levels[0]
                                                            ],
                                                           level = 0,
                                                           ).set_names(global_var.weather_site_name, level=0)
        df_weather = df_weather.sort_index(axis = 1)
        df_weather = df_weather.reindex(pd.date_range(start = df_weather.index.min(),
                                                      end   = df_weather.index.max() +pd.to_timedelta(2, unit='h'),
                                                      freq  = '1H',
                                                      name  = df_weather.index.name, 
                                                      ))
        df_weather                  = df_weather.interpolate(method='linear') 
        df_weather, trash_weather   = correct_filter_weather(df_weather)
        df_weather[global_var.weather_nature] = global_var.weather_nature_observation 
        df_weather                  = df_weather.set_index(global_var.weather_nature, append = True).unstack(global_var.weather_nature)
        df_weather.columns          = df_weather.columns.remove_unused_levels()
        df_weather                  = df_weather.stack([0,1,2])
        df_weather.name             = global_var.quantity_value
        df_weather                  = df_weather.reset_index()
        # Save
        os.makedirs(os.path.dirname(fname_weather), exist_ok = True)
        
        print('Save')
        df_weather.to_csv(fname_weather,
                          index = False,
                          sep   = ';',
                          )
        with open(fname_trash, 'wb') as f:
            pickle.dump(trash_weather, f)

    coordinates_weather = weather_description.set_index(global_var.weather_site_name)[[global_var.geography_latitude, global_var.geography_longitude]]
    if zone == global_var.geography_zone_france:
        coordinates_weather = coordinates_weather.loc[  (pd.Series(True, coordinates_weather.index))
                                                      & (coordinates_weather[global_var.geography_latitude]  > geography.metropolis_latitude_min)
                                                      & (coordinates_weather[global_var.geography_latitude]  < geography.metropolis_latitude_max)
                                                      & (coordinates_weather[global_var.geography_longitude] > geography.metropolis_longitude_min)
                                                      & (coordinates_weather[global_var.geography_longitude] < geography.metropolis_longitude_max)
                                                      ]
    else:
        raise ValueError('Incorrect zone : {0}'.format(zone))
    coordinates_weather.sort_index(axis = 0, inplace = True)
    common_names        = sorted(set(coordinates_weather.index).intersection(df_weather[global_var.weather_site_name]))
    df_weather          = df_weather.loc[df_weather[global_var.weather_site_name].isin(common_names)]
    coordinates_weather = coordinates_weather.loc[common_names]
    
    df_weather          = df_weather.loc[  (df_weather[global_var.weather_dt_UTC] >= date_min)
                                         & (df_weather[global_var.weather_dt_UTC] <  date_max)
                                         ]
    assert df_weather.shape[0] > 0

    return df_weather, coordinates_weather, trash_weather



