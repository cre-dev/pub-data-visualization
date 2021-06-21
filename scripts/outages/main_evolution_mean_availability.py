#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The script allows the user to plot the expected availability of
a given set of production unit during the delivery period
of a given contract.
"""

import pandas as pd
#
from pub_data_visualization import global_tools, global_var, outages

###############################################################################
contract_delivery_begin_year   = 2018
contract_frequency             = global_var.contract_frequency_month
contract_delivery_period_index = 10
contract_profile               = global_var.contract_profile_base
#
date_source_outages = global_var.data_source_outages_rte
map_code            = global_var.geography_map_code_france
producer_outages    = None
production_source   = None
unit_name           = None
date_min            = None
date_max            = None
###############################################################################
figsize    = global_var.figsize_horizontal_ppt
folder_out = global_var.path_plots
close      = False
###############################################################################

### Contract name
contract_name  = global_tools.format_contract_name(contract_delivery_begin_year,
                                                   contract_frequency,
                                                   contract_delivery_period_index,
                                                   contract_profile,
                                                   )

### Load
df = outages.load(source            = date_source_outages,
                  map_code          = map_code,
                  producer          = producer_outages,
                  unit_name         = unit_name,
                  production_source = production_source,
                  )

### Transform
dikt_programs, _ = outages.tools.compute_all_programs(df)
product_delivery_windows = global_tools.compute_delivery_windows(delivery_begin_year_local = contract_delivery_begin_year, 
                                                                 frequency                 = contract_frequency, 
                                                                 delivery_period_index     = contract_delivery_period_index, 
                                                                 profile                   = contract_profile, 
                                                                 tz_local                  = global_var.dikt_tz[map_code],
                                                                 )
nb_hours       = global_tools.compute_nb_hours(product_delivery_windows)
df_energy_tot  = outages.tools.compute_missing_energy(product_delivery_windows,
                                                      dikt_programs,
                                                      )
df_power_tot   = df_energy_tot/nb_hours
### Plot
outages.plot.evolution_mean_availability(df_power_tot,
                                         contract_name     = contract_name,
                                         nb_hours          = nb_hours,
                                         date_min          = date_min,
                                         date_max          = date_max,
                                         source            = date_source_outages,
                                         map_code          = map_code,
                                         producer          = producer_outages,
                                         production_source = production_source,
                                         unit_name         = unit_name,
                                         figsize           = figsize,
                                         folder_out        = folder_out,
                                         close             = close,
                                         )  
    

