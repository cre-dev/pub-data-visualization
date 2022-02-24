

import pandas as pd
import re
#
from .. import global_var



def compute_delivery_dates(delivery_begin_year   = None,
                           delivery_begin_date   = None,
                           delivery_end_date     = None,
                           frequency             = None,
                           delivery_period_index = None,
                           local_tz              = None,
                           ):
    """
        Computes the localized begin and end dates of a given contract.
 
        :param delivery_begin_year: The year of the delivery
        :param delivery_begin_date: The presumed date of the delivery
        :param delivery_end_date: The presumed date of the delivery
        :param frequency: The type of delivery contract (year, month, etc.)
        :param delivery_period_index: The index of the delivery contract
        :param local_tz: The local timezone
        :type delivery_begin_year: int
        :type delivery_begin_date: pd.Timestamp
        :type delivery_end_date: pd.Timestamp
        :type frequency: string
        :type delivery_period_index: int
        :type local_tz: pytz.tzfile
        :return: The localized beginning date
        :rtype: pd.Timestamp
    """

    if frequency == global_var.contract_frequency_year:
        delivery_begin_date = pd.to_datetime("01/01/{year}".format(year=delivery_begin_year),
                                             format="%d/%m/%Y",
                                             )
        delivery_end_date = delivery_begin_date + pd.DateOffset(years=1)

    elif frequency == global_var.contract_frequency_gas_year:
        delivery_begin_date = pd.to_datetime("01/10/{year}".format(year=delivery_begin_year),
                                             format="%d/%m/%Y",
                                             )
        delivery_end_date = delivery_begin_date + pd.DateOffset(years=1)

    elif frequency == global_var.contract_frequency_boy:
        if bool(delivery_begin_date):
            delivery_end_date = (delivery_begin_date + pd.DateOffset(years = 3)).replace(month = 1, day = 1)
        else:
            delivery_begin_date = pd.NaT
            delivery_end_date   = pd.NaT
        
    elif frequency == global_var.contract_frequency_season:
        delivery_begin_date = pd.to_datetime("01/{month}/{year}".format(month = (4
                                                                                 if delivery_period_index == global_var.contract_delivery_period_index_summer
                                                                                 else
                                                                                 10
                                                                                 ),
                                                                        year  = delivery_begin_year,
                                                                        ),
                                             format = "%d/%m/%Y",
                                             )
        delivery_end_date = delivery_begin_date + pd.DateOffset(months = 6)
            
    elif frequency == global_var.contract_frequency_quarter:
        delivery_begin_date = pd.to_datetime("01/{month}/{year}".format(year  = delivery_begin_year,
                                                                        month = 3*(delivery_period_index - 1) + 1,
                                                                        ),
                                             format = "%d/%m/%Y",
                                             )
        delivery_end_date = delivery_begin_date + pd.DateOffset(months = 3)

    elif frequency == global_var.contract_frequency_boq:
        if bool(delivery_begin_date):
            delivery_end_date = (delivery_begin_date.replace(month = (((delivery_begin_date.month - 1) // 3) * 3) + 1,
                                                             day   = 1,
                                                             )  + pd.DateOffset(months = 3)
                                 )
        else:
            delivery_begin_date = pd.NaT
            delivery_end_date   = pd.NaT
            
    elif frequency == global_var.contract_frequency_months:
        months_match = re.compile(global_var.contract_delivery_period_index_months_pattern).match(str(delivery_period_index))
        delivery_begin_date = pd.to_datetime("01/{month}/{year}".format(year  = delivery_begin_year,
                                                                        month = months_match.group(1),
                                                                        ),
                                             format = "%d/%m/%Y",
                                             )
        delivery_end_date = delivery_begin_date + pd.DateOffset(months = int(months_match.group(2)))

    elif frequency == global_var.contract_frequency_month:
        delivery_begin_date = pd.to_datetime("01/{month}/{year}".format(year  = delivery_begin_year,
                                                                        month = delivery_period_index,
                                                                        ),
                                             format = "%d/%m/%Y",
                                             )
        delivery_end_date = delivery_begin_date + pd.DateOffset(months = 1)

    elif frequency in [global_var.contract_frequency_fr,
                       global_var.contract_frequency_bk,
                       ]:
        assert bool(delivery_begin_date)
        assert bool(delivery_end_date)

    elif frequency == global_var.contract_frequency_bom:
        if bool(delivery_begin_date):
            delivery_end_date = delivery_begin_date.replace(day = 1) + pd.DateOffset(months = 3)
        else:
            delivery_begin_date = pd.NaT
            delivery_end_date   = pd.NaT
            
    elif frequency == global_var.contract_frequency_week:
        week_match = re.compile(global_var.contract_delivery_period_index_week_pattern).match(str(delivery_period_index))
        delivery_begin_date = pd.to_datetime("{day}/{month}/{year}".format(year  = delivery_begin_year,
                                                                           month = week_match.group(1),
                                                                           day   = week_match.group(2),
                                                                           ),
                                             format = "%d/%m/%Y",
                                             )
        delivery_end_date = delivery_begin_date + pd.DateOffset(weeks = 1)

    elif frequency == global_var.contract_frequency_bow:
        if bool(delivery_begin_date):
            delivery_end_date = delivery_begin_date.floor('D') + pd.to_timedelta(7 - delivery_begin_date.dayofweek, unit='d')
        else:
            delivery_begin_date = pd.NaT
            delivery_end_date   = pd.NaT
            
    elif frequency == global_var.contract_frequency_weekend:
        weekend_match = re.compile(global_var.contract_delivery_period_index_weekend_pattern).match(str(delivery_period_index))
        delivery_begin_date = pd.to_datetime("{day}/{month}/{year}".format(year  = delivery_begin_year,
                                                                           month = weekend_match.group(1),
                                                                           day   = weekend_match.group(2),
                                                                           ),
                                             format = "%d/%m/%Y",
                                             )
        delivery_end_date = delivery_begin_date + pd.DateOffset(days = 2)
            
    elif frequency == global_var.contract_frequency_weekbgn:
        weekbgn_match = re.compile(global_var.contract_delivery_period_index_weekbgn_pattern).match(str(delivery_period_index))
        delivery_begin_date = pd.to_datetime("{day}/{month}/{year}".format(year  = delivery_begin_year,
                                                                           month = weekbgn_match.group(1),
                                                                           day   = weekbgn_match.group(2),
                                                                           ),
                                                   format = "%d/%m/%Y",
                                                   )
        delivery_end_date = delivery_begin_date + pd.DateOffset(days = 5)
            
    elif frequency == global_var.contract_frequency_day:
        day_match = re.compile(global_var.contract_delivery_period_index_day_pattern).match(str(delivery_period_index))
        delivery_begin_date = pd.to_datetime("{day}/{month}/{year}".format(year  = delivery_begin_year,
                                                                           month = day_match.group(1),
                                                                           day   = day_match.group(2),
                                                                           ),
                                             format = "%d/%m/%Y",
                                             )
        delivery_end_date = delivery_begin_date + pd.DateOffset(days = 1)
            
    elif frequency == global_var.contract_frequency_days:
        days_match = re.compile(global_var.contract_delivery_period_index_days_pattern).match(str(delivery_period_index))
        delivery_begin_date = pd.to_datetime("{day}/{month}/{year}".format(year  = delivery_begin_year,
                                                                           month = days_match.group(1),
                                                                           day   = days_match.group(2),
                                                                           ),
                                             format = "%d/%m/%Y",
                                             )
        delivery_end_date = delivery_begin_date + pd.DateOffset(days = int(days_match.group(3)))
            
    elif frequency == global_var.contract_frequency_bloc:
        hour_match = re.compile(global_var.contract_delivery_period_index_bloc_pattern).match(str(delivery_period_index))
        delivery_begin_date = pd.to_datetime("{day}/{month}/{year}".format(year  = delivery_begin_year,
                                                                           month = hour_match.group(1),
                                                                           day   = hour_match.group(2),
                                                                           ),
                                             format = "%d/%m/%Y",
                                             )
        delivery_end_date = (  delivery_begin_date
                             + pd.DateOffset(hours = (  int(hour_match.group(3))
                                                      + ((int(hour_match.group(4)) - int(hour_match.group(3))) % 24)
                                                      )
                                             )
                             ).replace(hour   = 0,
                                       minute = 0,
                                       )
            
    elif frequency == global_var.contract_frequency_hour:
        hour_match = re.compile(global_var.contract_delivery_period_index_hour_pattern).match(str(delivery_period_index))
        delivery_begin_date = pd.to_datetime("{day}/{month}/{year}".format(year  = delivery_begin_year,
                                                                           month = hour_match.group(1),
                                                                           day   = hour_match.group(2),
                                                                           ),
                                             format = "%d/%m/%Y",
                                             )
        delivery_end_date = (delivery_begin_date + pd.DateOffset(hours = int(hour_match.group(3)) + 1)).replace(hour = 0, minute = 0) 
            
    elif frequency == global_var.contract_frequency_half_hour:
        half_hour_match = re.compile(global_var.contract_delivery_period_index_half_hour_pattern).match(str(delivery_period_index))
        delivery_begin_date = pd.to_datetime("{day}/{month}/{year}".format(year   = delivery_begin_year,
                                                                           month  = half_hour_match.group(1),
                                                                           day    = half_hour_match.group(2),
                                                                           ),
                                             format = "%d/%m/%Y",
                                             )
        delivery_end_date = (delivery_begin_date + pd.DateOffset(hours  = int(half_hour_match.group(3)) + (int(half_hour_match.group(4)) + 30) // 60,
                                                                 minute = (int(half_hour_match.group(4)) + 30) % 60,
                                                                 )).replace(hour = 0, minute = 0)

    elif frequency == global_var.contract_frequency_unknown:
        delivery_begin_date = pd.NaT
        delivery_end_date   = pd.NaT
        
    else:
        raise NotImplementedError('frequency = {frequency}'.format(frequency = frequency))
    
    if bool(delivery_begin_date) and delivery_begin_date.tz is None:
        delivery_begin_date = delivery_begin_date.tz_localize(local_tz)
    if bool(delivery_end_date) and delivery_end_date.tz   is None:
        delivery_end_date   = delivery_end_date.tz_localize(local_tz)
        
    return pd.Series([delivery_begin_date, delivery_end_date])

