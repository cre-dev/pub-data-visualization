#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    The script allows the user to draw
    the auction prices for a given bidding zone.
"""

#
from pub_data_visualization import auctions, global_var

###############################################################################
data_source_auctions = global_var.data_source_entsoe
map_code_auctions    = [global_var.geography_map_code_france,
                        global_var.geography_map_code_gb,
                        global_var.geography_map_code_belgium,
                        ]
date_min             = None 
date_max             = None
###############################################################################
figsize    = global_var.figsize_horizontal_ppt
folder_out = global_var.path_plots
close      = False
###############################################################################

### Load
df = auctions.load(date_min = date_min,
                   date_max = date_max,
                   source   = data_source_auctions,
                   map_code = map_code_auctions,
                   )

### Pivot
dg = df.pivot_table(values = global_var.auction_price_euro_mwh, 
                    index = [global_var.contract_delivery_begin_year_local,
                             global_var.contract_product,
                             global_var.contract_delivery_begin_dt_UTC,
                             global_var.contract_profile,
                             ],
                    columns = [global_var.geography_map_code,
                               ],
                    )
dg = dg.sort_index()

### Plot
auctions.plot.price(dg,
                    source     = data_source_auctions,
                    map_code   = map_code_auctions,
                    date_min   = date_min, 
                    date_max   = date_max,
                    figsize    = figsize,
                    folder_out = folder_out,
                    close      = close,
                    )

