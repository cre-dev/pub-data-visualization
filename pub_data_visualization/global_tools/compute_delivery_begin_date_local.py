

import pandas as pd
#
from .. import global_var



def compute_delivery_begin_date_local(delivery_begin_year_local = None,
                                      delivery_begin_date_local = None,
                                      frequency                 = None,
                                      delivery_period_index     = None,
                                      local_tz                  = None,
                                      ):
    """
        Computes the localized beginning date of a given contract.
 
        :param delivery_begin_year_local: The year of the delivery
        :param delivery_begin_date_local: The presumed date of the delivery
        :param frequency: The type of delivery contract (year, month, etc.)
        :param delivery_period_index: The index of the delivery contract
        :param local_tz: The local timezone
        :type delivery_begin_year_local: int
        :type delivery_begin_date_local: pd.Timestamp
        :type frequency: string
        :type delivery_period_index: int
        :type local_tz: pytz.tzfile
        :return: The localized beginning date
        :rtype: pd.Timestamp
    """

    if frequency == global_var.contract_frequency_year:
        delivery_begin_date_local = pd.to_datetime("01/01/{year}".format(year = delivery_begin_year_local), 
                                                   format = "%d/%m/%Y",
                                                   )
        
    elif frequency == global_var.contract_frequency_season:
        delivery_begin_date_local = pd.to_datetime("01/{month}/{year}".format(month = (4
                                                                                       if delivery_period_index == global_var.contract_delivery_period_index_summer
                                                                                       else
                                                                                       10
                                                                                       ),
                                                                              year  = delivery_begin_year_local,
                                                                              ),
                                                   format = "%d/%m/%Y",
                                                   )
            
    elif frequency == global_var.contract_frequency_quarter:
        delivery_begin_date_local = pd.to_datetime("01/{month}/{year}".format(year  = delivery_begin_year_local,
                                                                              month = 3*(delivery_period_index - 1) + 1,
                                                              ),
                                                   format = "%d/%m/%Y",
                                                   )
            
    elif frequency == global_var.contract_frequency_month:
        delivery_begin_date_local = pd.to_datetime("01/{month}/{year}".format(year  = delivery_begin_year_local,
                                                                              month = delivery_period_index,
                                                                              ),
                                                   format = "%d/%m/%Y",
                                                   )
            
    elif frequency in [global_var.contract_frequency_week,
                       global_var.contract_frequency_weekend,
                       global_var.contract_frequency_day,
                       ]:
        delivery_begin_date_local = pd.to_datetime("{day}/{month}/{year}".format(year  = delivery_begin_year_local,
                                                                                 month = str(delivery_period_index)[:-2],
                                                                                 day   = str(delivery_period_index)[-2:],
                                                                                 ),
                                                   format = "%d/%m/%Y",
                                                   )
            
    elif frequency in [global_var.contract_frequency_days,
                     ]:
        if delivery_begin_date_local is None:
            delivery_begin_date_local = pd.to_datetime("{day}/{month}/{year}".format(year  = delivery_begin_year_local,
                                                                                     month = str(delivery_period_index)[:-3],
                                                                                     day   = str(delivery_period_index)[-3:-1],
                                                                                     ),
                                                       format = "%d/%m/%Y",
                                                       )
        else:
            assert bool(delivery_begin_date_local), delivery_begin_date_local
            
    elif frequency in [global_var.contract_frequency_boy,
                       global_var.contract_frequency_boq,
                       global_var.contract_frequency_bom,
                       global_var.contract_frequency_bow,
                       ]:
        if delivery_begin_date_local is None:
            delivery_begin_date_local = pd.NaT
        else:
            assert bool(delivery_begin_date_local), delivery_begin_date_local
        
    else:
        raise NotImplementedError('frequency = {frequency}'.format(frequency = frequency))
        
    if delivery_begin_date_local.tz is None:
        delivery_begin_date_local = delivery_begin_date_local.tz_localize(local_tz)
    else:
        assert delivery_begin_date_local.tz == local_tz, (delivery_begin_date_local, local_tz)
        
    return delivery_begin_date_local

