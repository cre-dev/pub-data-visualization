#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The script allows the user to draw the expected availability
of a given set of production units from several temporal viewpoints.
"""

import pandas as pd
#
from pub_data_visualization import global_var, outages

###############################################################################
data_source_outages = global_var.data_source_outages_rte
map_code            = global_var.geography_map_code_france
producer_outages    = None
production_source   = global_var.production_source_nuclear
unit_name           = None
date_min            = pd.Timestamp("2022-01-01 00:00").tz_localize(global_var.dikt_tz[map_code])
date_max            = pd.Timestamp("2024-01-01 00:00").tz_localize(global_var.dikt_tz[map_code])
viewpoint_dt_extrapolate = [pd.Timestamp('2021-12-01 00:00').tz_localize(global_var.dikt_tz[map_code]),
                            pd.Timestamp('2022-01-01 00:00').tz_localize(global_var.dikt_tz[map_code]),
                            pd.Timestamp('2022-02-01 00:00').tz_localize(global_var.dikt_tz[map_code]),
                            ]
###############################################################################
local_tz   = 'CET'
diff_init  = False
smoother   = 'basic'
figsize    = global_var.figsize_horizontal_ppt
folder_out = global_var.path_plots
close      = False
###############################################################################

# Load
df = outages.load(source    = data_source_outages,
                  map_code  = map_code,
                  producer  = producer_outages,
                  unit_name = unit_name,
                  production_source = production_source,
                  )

# Transform
dikt_programs, _ = outages.tools.compute_all_programs(df)
dh = outages.tools.extrapolate_programs(dikt_programs,
                                        viewpoint_dt_extrapolate,
                                        production_dt_min = date_min,
                                        production_dt_max = date_max,
                                        )

# Plot program
outages.plot.incremental_programs(dh,
                                  diff_init = diff_init,
                                  smoother  = smoother,
                                  date_min  = date_min, 
                                  date_max  = date_max, 
                                  #
                                  source_outages    = data_source_outages,
                                  map_code          = map_code,
                                  producer          = producer_outages,
                                  production_source = production_source,
                                  unit_name         = unit_name,
                                  local_tz          = local_tz,
                                  figsize           = figsize,
                                  folder_out        = folder_out,
                                  close             = close,
                                  )  

