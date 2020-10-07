#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The script allows the user to draw the empirical boxplots
of the weather conditions for the different months and different years.
"""

#
from pub_data_visualization import global_var, weather

###############################################################################
data_source_weather = global_var.data_source_meteofrance
weather_nature      = global_var.weather_nature_observation
weather_quantity    = global_var.weather_temperature_celsius
###############################################################################
figsize    = global_var.figsize_horizontal_ppt
folder_out = global_var.path_plots
close      = False
###############################################################################

### Load
df = weather.load(source = data_source_weather)

### Plot
weather.plot.distribution(df, 
                          source            = data_source_weather,
                          nature            = weather_nature,
                          physical_quantity = weather_quantity,
                          folder_out        = folder_out,
                          close             = close,
                          figsize           = figsize,
                          )
