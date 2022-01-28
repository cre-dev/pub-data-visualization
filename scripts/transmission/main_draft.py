#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The script allows the user to load
the transmission capacity.
"""

import pandas as pd
#
from pub_data_visualization import global_var, transmission

###############################################################################
data_source_transmission = global_var.data_source_transmission_entsog_nominations
transmission_dt_min      = pd.Timestamp('2019-01-10').tz_localize('CET')
transmission_dt_max      = pd.Timestamp('2019-01-14').tz_localize('CET')
###############################################################################
figsize    = global_var.figsize_horizontal_ppt
folder_out = global_var.path_plots
close      = False
###############################################################################

### Load
df = transmission.load(date_min = transmission_dt_min,
                       date_max = transmission_dt_max,
                       source   = data_source_transmission,
                       )

