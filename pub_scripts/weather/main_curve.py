#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    The script allows the user to draw the weather conditions
    observed in a given zone.
"""

import numpy  as np
import pandas as pd
#
from pub_data_visualization import global_var, weather

###############################################################################
data_source_weather = global_var.data_source_meteofrance
weather_nature      = global_var.weather_nature_observation
weather_quantity    = global_var.weather_wind_speed
date_min            = pd.Timestamp('2015-01-01').tz_localize('UTC')
date_max            = pd.Timestamp('2020-01-01').tz_localize('UTC')
###############################################################################
figsize    = global_var.figsize_horizontal_ppt
folder_out = global_var.path_plots
close      = False
###############################################################################

### Load
df = weather.load(source   = data_source_weather,
                  date_min = date_min,
                  date_max = date_max,
                  )
dg = df.groupby(level = global_var.weather_physical_quantity,
                axis  = 1,
                ).agg(np.mean) 

### Plot
weather.plot.curve(dg, 
                   date_min,
                   date_max,
                   source            = data_source_weather,
                   nature            = weather_nature,
                   physical_quantity = weather_quantity,
                   folder_out        = folder_out,
                   close             = close,
                   figsize           = figsize,
                   )