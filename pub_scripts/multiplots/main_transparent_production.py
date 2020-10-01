#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The script allows the user to plot the observed production and 
the production expected from the transpranecy publications 
for a given set of production units.
"""

import pandas as pd
#
from pub_data_visualization import global_var, outages, production, multiplots

###############################################################################
map_code               = global_var.geography_map_code_france
unit_name              = 'DAMPIERRE 4'
date_min               = None
date_max               = None
#
data_source_outages    = global_var.data_source_rte
company_outages        = None
#
data_source_production = global_var.data_source_rte
production_source      = None
production_nature      = global_var.production_nature_observation_mw
###############################################################################
figsize    = global_var.figsize_horizontal_ppt
folder_out = global_var.path_plots
close      = False
###############################################################################

### Production
df_production = production.load(source   = data_source_production,
                                map_code = map_code,
                                )

### Outages
df = outages.load(source    = data_source_outages,
                  map_code  = map_code,
                  company   = company_outages,
                  unit_name = unit_name,
                  production_source = production_source,
                  )
dikt_programs, _   = outages.tools.compute_all_programs(df)
df_program         = dikt_programs[unit_name]
df_awaited_program = outages.tools.cross_section_view(df_program)
    
### Plot program and production
multiplots.transparent_production(df_awaited_program,
                                  df_production,
                                  source_outages    = data_source_outages,
                                  source_production = data_source_production,
                                  map_code          = map_code,
                                  unit_name         = unit_name,
                                  date_min          = date_min, 
                                  date_max          = date_max, 
                                  production_source = production_source,
                                  production_nature = production_nature,
                                  figsize           = figsize,
                                  folder_out        = folder_out,
                                  close             = close,
                                  )  




