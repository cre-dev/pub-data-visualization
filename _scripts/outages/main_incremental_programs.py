#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
#
import global_var
import outages

###############################################################################
data_source_outages = global_var.data_source_rte
map_code            = global_var.geography_map_code_france
company             = None
production_source   = global_var.production_source_nuclear
unit_name           = None
date_min            = pd.to_datetime("2020-01-01 00:00").tz_localize(global_var.dikt_tz[map_code])
date_max            = pd.to_datetime("2022-01-01 00:00").tz_localize(global_var.dikt_tz[map_code])
publication_dt_extrapolate = [pd.to_datetime('2020-05-01 00:00').tz_localize(global_var.dikt_tz[map_code]),
                              pd.to_datetime('2020-06-01 00:00').tz_localize(global_var.dikt_tz[map_code]),
                              pd.to_datetime('2020-07-01 00:00').tz_localize(global_var.dikt_tz[map_code]),
                              ]
###############################################################################
diff_init  = False
smoother   = 'basic'
figsize    = global_var.figsize_horizontal_ppt
folder_out = global_var.path_plots
close      = False
###############################################################################

# Load
df = outages.load(source    = data_source_outages,
                  map_code  = map_code,
                  company   = company,
                  unit_name = unit_name,
                  production_source = production_source,
                  )

# Transform
dikt_programs, _ = outages.tools.compute_all_programs(df)
dh = outages.tools.extrapolate_programs(dikt_programs,
                                        publication_dt_extrapolate,
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
                                  company_outages   = company,
                                  production_source = production_source,
                                  unit_name         = unit_name,
                                  figsize           = figsize,
                                  folder_out        = folder_out,
                                  close             = close,
                                  )  

