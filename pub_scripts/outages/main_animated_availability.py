#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The script allows the user to plot interactively the expected availability
of a given set of production units from different temporal viewpoints.
"""

import pandas as pd
#
from pub_data_visualization import global_var, outages

###############################################################################
data_source_outages = global_var.data_source_rte
map_code            = global_var.geography_map_code_france
producer_outages    = None
production_source   = global_var.production_source_nuclear
unit_name           = None
production_dt_min   = pd.Timestamp("2017-09-20").tz_localize(global_var.dikt_tz[map_code])
production_dt_max   = pd.Timestamp("2017-09-30").tz_localize(global_var.dikt_tz[map_code])
publication_dt_min  = pd.Timestamp("2017-09-20").tz_localize(global_var.dikt_tz[map_code])
publication_dt_max  = pd.Timestamp("2017-09-30").tz_localize(global_var.dikt_tz[map_code])
###############################################################################
figsize    = global_var.figsize_horizontal_ppt
folder_out = global_var.path_plots
close      = False
###############################################################################

### Load
df = outages.load(source            = data_source_outages,
                  map_code          = map_code,
                  producer          = producer_outages,
                  unit_name         = unit_name,
                  production_source = production_source,
                  )

### Transform
dikt_programs, _ = outages.tools.compute_all_programs(df)
dh = outages.tools.sum_programs(dikt_programs,
                                production_dt_min  = production_dt_min,
                                production_dt_max  = production_dt_max,
                                publication_dt_min = publication_dt_min,
                                publication_dt_max = publication_dt_max,
                                )

### Plot
outages.plot.animated_availability(dh, 
                                   production_dt_min = production_dt_min,
                                   production_dt_max = production_dt_max,
                                   data_source       = data_source_outages,
                                   map_code          = map_code,
                                   producer          = producer_outages,
                                   production_source = production_source,
                                   unit_name         = unit_name,
                                   figsize           = figsize,
                                   folder_out        = folder_out,
                                   close             = close,
                                   )  

