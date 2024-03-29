#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The script allows the user to draw 
the expected availability program of
a given set of production units.
"""

import pandas as pd
#
from pub_data_visualization import global_var, outages

###############################################################################
data_source_outages = global_var.data_source_outages_entsoe
map_code            = global_var.geography_map_code_france
producer_outages    = None
production_source   = global_var.production_source_nuclear
unit_name           = 'BELLEVILLE 1'
date_min            = None
date_max            = None
###############################################################################
figsize    = global_var.figsize_horizontal_ppt
folder_out = global_var.path_plots
close      = False
###############################################################################

### Load
df = outages.load(source    = data_source_outages,
                  map_code  = map_code,
                  producer  = producer_outages,
                  unit_name = unit_name,
                  production_source = production_source,
                  )

### Transform
dikt_programs, _    = outages.tools.compute_all_programs(df)
df_program          = dikt_programs[unit_name]
df_expected_program = outages.tools.cross_section_view(df_program)
    
### Plot
outages.plot.expected_program(df_expected_program,
                              date_min          = date_min,
                              date_max          = date_max,
                              source            = data_source_outages,
                              map_code          = map_code,
                              producer          = producer_outages,
                              production_source = production_source,
                              unit_name         = unit_name,
                              figsize           = figsize,
                              folder_out        = folder_out,
                              close             = close,
                              )



