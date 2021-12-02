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
data_source_weather = global_var.data_source_weather_meteofrance
weather_nature      = global_var.weather_nature_observation
weather_quantity    = global_var.weather_wind_speed
date_min            = None
date_max            = None
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

### Plot
weather.plot.curve(df,
                   date_min,
                   date_max,
                   source            = data_source_weather,
                   nature            = weather_nature,
                   physical_quantity = weather_quantity,
                   folder_out        = folder_out,
                   close             = close,
                   figsize           = figsize,
                   )