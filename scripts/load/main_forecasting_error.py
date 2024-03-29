#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The script allows the user to draw the load
and the forecasting errors for a given zone.
"""

import pandas as pd
#
from pub_data_visualization import global_var, load

###############################################################################
data_source_load     = global_var.data_source_load_eco2mix
load_power_unit      = global_var.load_power_gw
load_nature_forecast = global_var.load_nature_forecast_day1
map_code             = global_var.geography_map_code_france
date_min             = pd.Timestamp("2018-01-01 00:00").tz_localize(global_var.dikt_tz[map_code])
date_max             = pd.Timestamp("2019-01-01 00:00").tz_localize(global_var.dikt_tz[map_code])
###############################################################################
figsize    = global_var.figsize_horizontal_ppt
folder_out = global_var.path_plots
close      = False
###############################################################################

if (   data_source_load != global_var.data_source_load_eco2mix
    or map_code         != global_var.geography_map_code_france
    ):
    raise NotImplementedError

### Load
dg = load.load(source      = data_source_load,
               map_code    = map_code,
               date_min    = date_min,
               date_max    = date_max,
               )

### Plot
load.plot.forecasting_error(dg,
                            source_load          = data_source_load,
                            load_unit            = load_power_unit,
                            load_nature_forecast = load_nature_forecast,
                            map_code             = map_code,
                            date_min             = date_min,
                            date_max             = date_max,
                            figsize              = figsize,
                            folder_out           = folder_out,
                            close                = close,
                            )