

import pandas as pd
import re
#
import global_var


def compute_delivery_end_date(delivery_begin_date_local = None,
                              product                   = None,
                              delivery_period_index     = None,
                              ):


    if (   product == global_var.contract_product_unknown
        or pd.isnull(delivery_begin_date_local)
        ):
        delivery_end_date_local = pd.NaT
    else:
        assert type(delivery_begin_date_local)  == pd.Timestamp
        assert delivery_begin_date_local.minute == 0
        assert delivery_begin_date_local.hour   == 0
        assert type(product)                    == str
        assert type(delivery_period_index)      == int
    
        if product == global_var.contract_product_year:
            delivery_end_date_local = delivery_begin_date_local + pd.DateOffset(years = 1)
    
        elif product == global_var.contract_product_season:
            delivery_end_date_local = delivery_begin_date_local + pd.DateOffset(months = 6)
    
        elif product == global_var.contract_product_quarter:
            delivery_end_date_local = delivery_begin_date_local + pd.DateOffset(months = 3)
    
        elif product == global_var.contract_product_month:
            delivery_end_date_local = delivery_begin_date_local + pd.DateOffset(months = 1)
    
        elif product == global_var.contract_product_bom:
            delivery_end_date_local =(delivery_begin_date_local + pd.DateOffset(months = 1)).replace(day = 1) 
    
        elif product == global_var.contract_product_week:
            delivery_end_date_local = delivery_begin_date_local + pd.DateOffset(weeks = 1)
    
        elif product == global_var.contract_product_bow:
            delivery_end_date_local = delivery_begin_date_local + pd.DateOffset(days = 7 - delivery_begin_date_local.timetuple().tm_wday)
    
        elif product == global_var.contract_product_weekend:
            delivery_end_date_local = delivery_begin_date_local + pd.DateOffset(days = 2)
    
        elif product == global_var.contract_product_days:
            days_match = re.compile(r"^(\d{1,2})(\d{2})(\d{1})$").match(str(delivery_period_index))
            assert delivery_begin_date_local.month == int(days_match.group(1))
            assert delivery_begin_date_local.day   == int(days_match.group(2))
            nb_days = int(days_match.group(3))
            delivery_end_date_local = delivery_begin_date_local + pd.DateOffset(days = nb_days)
    
        elif product == global_var.contract_product_day:
            delivery_end_date_local = delivery_begin_date_local + pd.DateOffset(days = 1)
    
        elif product == global_var.contract_product_hour:
            delivery_end_date_local = (delivery_begin_date_local + pd.DateOffset(hours = delivery_period_index)).replace(hour = 0, minute = 0) 
    
        elif product == global_var.contract_product_unknown:
            delivery_end_date_local = global_var.contract_delivery_end_date_unknown 
    
        else:
            raise NotImplementedError('product = {product}'.format(product = product))
            
    return delivery_end_date_local