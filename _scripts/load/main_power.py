#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
#
import global_var
import load

###############################################################################
data_source_load = global_var.data_source_eco2mix
map_code         = global_var.geography_map_code_france
load_nature      = global_var.load_nature_observation_gw
date_min         = pd.to_datetime("2016-01-01 00:00").tz_localize(global_var.dikt_tz[map_code])
date_max         = pd.to_datetime("2019-01-01 00:00").tz_localize(global_var.dikt_tz[map_code])
###############################################################################
figsize    = global_var.figsize_horizontal_ppt
folder_out = global_var.path_plots
close      = False
###############################################################################

### Load
df = load.load(source      = data_source_load,
               map_code    = map_code,
               date_min    = date_min,
               date_max    = date_max,
               )

### Plot
load.plot.power(df,
                load_nature = load_nature,
                source_load = data_source_load,
                map_code    = map_code,
                date_min    = date_min,
                date_max    = date_max,
                figsize     = figsize,
                folder_out  = folder_out,
                close       = close,
                )