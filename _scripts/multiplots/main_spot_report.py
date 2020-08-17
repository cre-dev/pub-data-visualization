#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy  as np
import pandas as pd
#
import global_var
import weather
import production
import load
import outages
import auctions
import multiplots

###############################################################################
map_code          = global_var.geography_map_code_france
date_min          = pd.to_datetime('2017-12-01 00:00').tz_localize(global_var.dikt_tz[map_code])
date_max          = pd.to_datetime('2018-02-01 00:00').tz_localize(global_var.dikt_tz[map_code])
#
data_source_weather = global_var.data_source_meteofrance
weather_nature      = global_var.weather_nature_observation
#
production_nature      = global_var.production_nature_observation_gw
data_source_production = global_var.data_source_eco2mix
#
data_source_load = global_var.data_source_eco2mix
load_nature      = global_var.load_nature_observation_gw
#
company_outages            = None
data_source_outages        = global_var.data_source_rte
publication_dt_extrapolate = [date_min,
                              date_max,
                              ]
#
data_source_auctions = global_var.data_source_entsoe
map_code_auctions    = [global_var.geography_map_code_france,
                        global_var.geography_map_code_germany_luxembourg,
                        global_var.geography_map_code_spain,
                        ] 
###############################################################################
figsize    = global_var.figsize_vertical_ppt
folder_out = global_var.path_plots
close      = False
###############################################################################

### Weather
df_weather = weather.load(source   = data_source_weather,
                          date_min = date_min,
                          date_max = date_max,
                          )
dg_weather          = df_weather.groupby(level = global_var.weather_physical_quantity,
                                         axis  = 1,
                                         ).agg(np.mean)

### Production
df_production = production.load(source   = data_source_production,
                                map_code = map_code,
                                )

### Load
dg_load = load.load(source   = data_source_load,
                    map_code = map_code,
                    date_min = date_min,
                    date_max = date_max,
                    )

### Outages
df_outages = outages.load(source    = data_source_outages,
                          map_code  = map_code,
                          company   = company_outages,
                          )
dikt_programs, _ = outages.tools.compute_all_programs(df_outages)
df_extrapolated_programs = outages.tools.extrapolate_programs(dikt_programs,
                                                              publication_dt_extrapolate,
                                                              production_dt_min = date_min,
                                                              production_dt_max = date_max,
                                                              )

### Auctions
df_auctions = auctions.load(date_min = date_min,
                            date_max = date_max,
                            source   = data_source_auctions,
                            map_code = map_code_auctions,
                            )
dg_auctions = df_auctions.pivot_table(values = global_var.auction_price_euro_mwh, 
                                      index = [global_var.contract_delivery_begin_year_local,
                                               global_var.contract_product,
                                               global_var.contract_delivery_begin_date_local, 
                                               global_var.contract_delivery_period_index, 
                                               global_var.contract_delivery_begin_dt_local,
                                               global_var.contract_delivery_begin_dt_UTC,
                                               global_var.contract_profile,
                                               ],
                                      columns = [global_var.geography_map_code,
                                                 ],
                                      )
dg_auctions = dg_auctions.sort_index()


### Plot
multiplots.spot_report(dg_weather,
                       df_production,
                       dg_load,
                       df_extrapolated_programs,
                       dg_auctions,
                       map_code   = map_code,
                       date_min   = date_min,
                       date_max   = date_max,
                       figsize    = figsize,
                       folder_out = folder_out, 
                       close      = close,
                       )
