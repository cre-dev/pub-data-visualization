#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
#
import global_tools
import global_var
import outages

###############################################################################
contrat_delivery_begin_year    = 2018
contract_product               = global_var.contract_product_month
contract_delivery_period_index = 10
contract_profile               = global_var.contract_profile_base
#
date_source_outages = global_var.data_source_rte
map_code            = global_var.geography_map_code_france
company_outages     = None
production_source   = None
unit_name           = None
date_min            = None
date_max            = None
###############################################################################
figsize    = global_var.figsize_horizontal_ppt
folder_out = global_var.path_plots
close      = False
###############################################################################


### Load
df = outages.load(source    = date_source_outages,
                  map_code  = map_code,
                  company   = company_outages,
                  unit_name = unit_name,
                  production_source = production_source,
                  )

### Transform
dikt_programs, _ = outages.tools.compute_all_programs(df)
product_delivery_windows = global_tools.compute_delivery_windows(delivery_begin_year_local = contrat_delivery_begin_year, 
                                                                 product                   = contract_product, 
                                                                 delivery_period_index     = contract_delivery_period_index, 
                                                                 profile                   = contract_profile, 
                                                                 tz_local                  = global_var.dikt_tz[map_code],
                                                                 )
nb_hours       = global_tools.compute_nb_hours(product_delivery_windows)
df_energy_tot  = outages.tools.compute_missing_energy(product_delivery_windows,
                                                      dikt_programs,
                                                      )
df_power_tot   = df_energy_tot/nb_hours
contract_name  = global_tools.format_contract_name(contrat_delivery_begin_year,
                                                   contract_product,
                                                   contract_delivery_period_index,
                                                   contract_profile,
                                                   )
### Plot
outages.plot.evolution_mean_availability(df_power_tot,
                                         contract_name     = contract_name,
                                         nb_hours          = nb_hours,
                                         date_min          = date_min,
                                         date_max          = date_max,
                                         source            = date_source_outages,
                                         map_code          = map_code,
                                         company           = company_outages,
                                         production_source = production_source,
                                         unit_name         = unit_name,
                                         figsize           = figsize,
                                         folder_out        = folder_out,
                                         close             = close,
                                         )  
    

