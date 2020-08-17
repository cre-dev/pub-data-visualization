
import os
#
import global_var


folder_weather_meteofrance_raw = os.path.join(global_var.path_public_data,
                                              '20_MeteoFrance',
                                              'synop',
                                              )
fpath_weather_meteofrance_tmp = os.path.join(global_var.path_transformed,
                                             'MeteoFrance',
                                             'synop',
                                             )


dikt_files = {'weather.file_year_month' : 'synop.{year:d}{month:02d}',
              'weather.description'     : 'postesSynop',
              }