

import pandas as pd
#
from .. import global_var



def compute_delivery_begin_date_local(delivery_begin_year_local = None,
                                      product                   = None,
                                      delivery_period_index     = None,
                                      local_tz                  = None,
                                      ):

    if product == global_var.contract_product_year:
        delivery_begin_date_local = pd.to_datetime("01/01/{year}".format(year = delivery_begin_year_local), 
                                                   format = "%d/%m/%Y",
                                                   )
        
    elif product == global_var.contract_product_season:
        delivery_begin_date_local = pd.to_datetime("01/{month}/{year}".format(month = (4
                                                                                       if delivery_period_index == global_var.contract_delivery_period_index_summer
                                                                                       else
                                                                                       10
                                                                                       ),
                                                                              year  = delivery_begin_year_local,
                                                                              ),
                                                   format = "%d/%m/%Y",
                                                   )
            
    elif product == global_var.contract_product_quarter:
        delivery_begin_date_local = pd.to_datetime("01/{month}/{year}".format(year  = delivery_begin_year_local,
                                                                              month = 3*(delivery_period_index - 1) + 1,
                                                              ),
                                                   format = "%d/%m/%Y",
                                                   )
            
    elif product == global_var.contract_product_month:
        delivery_begin_date_local = pd.to_datetime("01/{month}/{year}".format(year  = delivery_begin_year_local,
                                                                              month = delivery_period_index,
                                                                              ),
                                                   format = "%d/%m/%Y",
                                                   )
            
    elif product in [global_var.contract_product_week,
                     global_var.contract_product_weekend,
                     global_var.contract_product_day,
                     ]:
        delivery_begin_date_local = pd.to_datetime("{day}/{month}/{year}".format(year  = delivery_begin_year_local,
                                                                                 month = str(delivery_period_index)[:-2],
                                                                                 day   = str(delivery_period_index)[-2:],
                                                                                 ),
                                                   format = "%d/%m/%Y",
                                                   )
            
    elif product in [global_var.contract_product_bom,
                     global_var.contract_product_bow,
                     ]:
        delivery_begin_date_local = pd.NaT
        
    else:
        raise NotImplementedError('product = {product}'.format(product = product))
        
    return delivery_begin_date_local.tz_localize(local_tz)