

import pandas as pd
import re
#
from .. import global_var


def compute_delivery_end_date(delivery_begin_date_local = None,
                              frequency                 = None,
                              delivery_period_index     = None,
                              ):
    """
        Computes the localized end date of a given contract.
 
        :param delivery_begin_date_local: The beginning date of the delivery
        :param frequency: The type of delivery contract (year, month, etc.)
        :param delivery_period_index: The index of the delivery contract
        :type delivery_begin_date_local: pd.Timestamp
        :type frequency: string
        :type delivery_period_index: int
        :return: The localized end date
        :rtype: pd.Timestamp
    """

    if (   frequency == global_var.contract_frequency_unknown
        or pd.isnull(delivery_begin_date_local)
        ):
        delivery_end_date_local = pd.NaT
    else:
        assert type(delivery_begin_date_local)  == pd.Timestamp
        assert delivery_begin_date_local.minute == 0
        assert delivery_begin_date_local.hour   == 0
        assert type(frequency)                  == str
        assert type(delivery_period_index)      == int
    
        if frequency == global_var.contract_frequency_year:
            delivery_end_date_local = delivery_begin_date_local + pd.DateOffset(years = 1)
    
        elif frequency == global_var.contract_frequency_season:
            delivery_end_date_local = delivery_begin_date_local + pd.DateOffset(months = 6)
    
        elif frequency == global_var.contract_frequency_quarter:
            delivery_end_date_local = delivery_begin_date_local + pd.DateOffset(months = 3)
    
        elif frequency == global_var.contract_frequency_month:
            delivery_end_date_local = delivery_begin_date_local + pd.DateOffset(months = 1)
    
        elif frequency == global_var.contract_frequency_bom:
            delivery_end_date_local =(delivery_begin_date_local + pd.DateOffset(months = 1)).replace(day = 1) 
    
        elif frequency == global_var.contract_frequency_week:
            delivery_end_date_local = delivery_begin_date_local + pd.DateOffset(weeks = 1)
    
        elif frequency == global_var.contract_frequency_bow:
            delivery_end_date_local = delivery_begin_date_local + pd.DateOffset(days = 7 - delivery_begin_date_local.timetuple().tm_wday)
    
        elif frequency == global_var.contract_frequency_weekend:
            delivery_end_date_local = delivery_begin_date_local + pd.DateOffset(days = 2)
    
        elif frequency == global_var.contract_frequency_days:
            days_match = re.compile(global_var.contract_delivery_period_index_days_pattern).match(str(delivery_period_index))
            month   = int(days_match.group(1))
            day     = int(days_match.group(2))
            nb_days = int(days_match.group(3))
            assert delivery_begin_date_local.month == month
            assert delivery_begin_date_local.day   == day
            delivery_end_date_local = delivery_begin_date_local + pd.DateOffset(days = nb_days)
    
        elif frequency == global_var.contract_frequency_day:
            delivery_end_date_local = delivery_begin_date_local + pd.DateOffset(days = 1)
    
        elif frequency == global_var.contract_frequency_hour:
            delivery_end_date_local = (delivery_begin_date_local + pd.DateOffset(hours = 1)).replace(hour = 0, minute = 0) 
    
        elif frequency == global_var.contract_frequency_half_hour:
            delivery_end_date_local = (delivery_begin_date_local + pd.DateOffset(minutes = 30)).replace(hour = 0, minute = 0) 
    
        elif frequency == global_var.contract_frequency_unknown:
            delivery_end_date_local = global_var.contract_delivery_end_date_unknown 
    
        else:
            raise NotImplementedError('frequency = {frequency}'.format(frequency = frequency))
            
    return delivery_end_date_local