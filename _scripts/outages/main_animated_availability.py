#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
#
from energy_data_visualization import global_var, outages

###############################################################################
data_source_outages = global_var.data_source_entsoe
map_code            = global_var.geography_map_code_belgium
company_outages     = None
production_source   = global_var.production_source_nuclear
unit_name           = None
date_min            = pd.to_datetime("2020-01-01 00:00").tz_localize(global_var.dikt_tz[map_code])
date_max            = pd.to_datetime("2021-01-01 00:00").tz_localize(global_var.dikt_tz[map_code])
publication_dt_min  = pd.to_datetime("2020-01-01 00:00").tz_localize(global_var.dikt_tz[map_code])
publication_dt_max  = pd.to_datetime("2021-01-01 00:00").tz_localize(global_var.dikt_tz[map_code])
###############################################################################
figsize    = global_var.figsize_horizontal_ppt
folder_out = global_var.path_plots
close      = False
###############################################################################

### Load
df = outages.load(source            = data_source_outages,
                  map_code          = map_code,
                  company           = company_outages,
                  unit_name         = unit_name,
                  production_source = production_source,
                  )

### Transform
dikt_programs, _ = outages.tools.compute_all_programs(df)
dh = outages.tools.sum_programs(dikt_programs,
                                production_dt_min  = date_min,
                                production_dt_max  = date_max,
                                publication_dt_min = publication_dt_min,
                                publication_dt_max = publication_dt_max,
                                )

### Plot
outages.plot.animated_availability(dh, 
                                   production_dt_min = date_min,
                                   production_dt_max = date_max,
                                   source_outages    = data_source_outages,
                                   map_code          = map_code,
                                   company_outages   = company_outages,
                                   production_source = production_source,
                                   unit_name         = unit_name,
                                   figsize           = figsize,
                                   folder_out        = folder_out,
                                   close             = close,
                                   )  

