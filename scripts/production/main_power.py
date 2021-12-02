#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The script allows the user to draw the observed production
of a given set of production units.
"""

#
from pub_data_visualization import global_var, production

###############################################################################
data_source_production = global_var.data_source_production_entsoe
map_code               = global_var.geography_map_code_france
production_nature      = global_var.production_nature_observation
production_unit        = global_var.production_power_gw
production_source      = None
unit_name              = None
date_min               = None
date_max               = None
###############################################################################
figsize    = global_var.figsize_horizontal_ppt
folder_out = global_var.path_plots
close      = False
###############################################################################

### Load
df = production.load(source   = data_source_production,
                     map_code = map_code,
                     date_min = date_min,
                     date_max = date_max,
                     )

### plot
production.plot.power(df, 
                      map_code          = map_code,
                      unit_name         = unit_name,
                      production_source = production_source,
                      production_nature = production_nature,
                      production_unit   = production_unit,
                      date_min          = date_min,
                      date_max          = date_max,
                      source            = data_source_production,
                      figsize           = figsize,
                      folder_out        = folder_out,
                      close             = close,
                      )


