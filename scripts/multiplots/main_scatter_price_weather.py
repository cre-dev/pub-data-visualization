#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The script allows the user to draw 
a scatterplot of national production and day-ahead prices.
"""

import os
import numpy  as np
import pandas as pd
#
from pub_data_visualization import global_var, global_tools, weather, auctions, multiplots
#
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters; register_matplotlib_converters()
from matplotlib.font_manager import FontProperties
global_tools.set_mpl(mpl, plt, FontProperties())
import matplotlib.patches as mpatches

###############################################################################
map_code          = global_var.geography_map_code_france
date_min          = pd.Timestamp('2017-01-01 00:00').tz_localize(global_var.dikt_tz[map_code])
date_max          = pd.Timestamp('2018-01-01 00:00').tz_localize(global_var.dikt_tz[map_code])
#
data_source_weather = global_var.data_source_weather_meteofrance
weather_quantity    = global_var.weather_temperature_celsius
#
data_source_auctions = global_var.data_source_auctions_entsoe
map_code_auctions    = [global_var.geography_map_code_france,
                        global_var.geography_map_code_germany_luxembourg,
                        global_var.geography_map_code_spain,
                        ] 
#
kernel_plot = False
###############################################################################
figsize    = global_var.figsize_horizontal_ppt
folder_out = global_var.path_plots
close      = False
###############################################################################

### Weather
df = weather.load(source   = data_source_weather,
                  date_min = date_min,
                  date_max = date_max,
                  )
dg = df.groupby(level = global_var.weather_physical_quantity,
                axis  = 1,
                ).agg(np.mean)
df_weather = dg.loc[:,weather_quantity]

### Auctions
df_auctions = auctions.load(date_min = date_min,
                            date_max = date_max,
                            source   = data_source_auctions,
                            map_code = map_code_auctions,
                            )
dg_auctions = df_auctions.pivot_table(values = global_var.auction_price_euro_mwh, 
                                      index = [global_var.contract_delivery_begin_year_local,
                                               global_var.contract_frequency,
                                               global_var.contract_delivery_begin_date_local, 
                                               global_var.contract_delivery_period_index, 
                                               global_var.contract_delivery_begin_dt_local,
                                               global_var.contract_delivery_begin_dt_UTC,
                                               global_var.contract_profile,
                                               ],
                                      columns = [global_var.geography_map_code,
                                                 ],
                                      )
dg_auctions = dg_auctions.sort_index()

### Plot
common_index = dg_auctions.index.get_level_values(global_var.contract_delivery_begin_dt_UTC).intersection(df_weather.index)
X = dg_auctions.loc[(slice(None), slice(None), slice(None), slice(None), slice(None), common_index),:]
Y = df_weather.loc[common_index]
x_label   = global_var.auction_price_euro_mwh
y_label   = weather_quantity
plot_name = 'scatter_price_weather'

multiplots.cloud_2d(X,
                    Y,
                    x_label     = x_label,
                    y_label     = y_label,
                    kernel_plot = kernel_plot,
                    plot_name   = plot_name,
                    date_min    = date_min,
                    date_max    = date_max,
                    map_code    = map_code,
                    figsize     = figsize,
                    folder_out  = folder_out, 
                    close       = close,
                    )

