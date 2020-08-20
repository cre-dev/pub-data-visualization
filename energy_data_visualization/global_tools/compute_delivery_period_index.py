
import pandas as pd
import re
#
from .. import global_var

def compute_delivery_period_index(product                 = None,
                                  delivery_begin_dt_local = None,
                                  delivery_end_date_local = None,
                                  tz_local                = None,
                                  profile                 = None,
                                  ):
    """
        Computes the delivery period index of a given contract.
 
        :param product: The type of delivery contract (year, month, etc.)
        :param delivery_begin_dt_local: The beginning datetime of the delivery
        :param delivery_end_date_local: The end date of the delivery
        :param local_tz: The local timezone
        :param profile: The profile of the contract
        :type product: string
        :type delivery_begin_dt_local: pd.Timestamp
        :type delivery_end_date_local: pd.Timestamp
        :type local_tz: pytz.tzfile
        :type profile: string
        :return: The delivery period index
        :rtype: int
    """
    
    if (   pd.isnull(delivery_begin_dt_local)
        or product == global_var.contract_product_unknown
        or product == global_var.contract_product_spread
        ):
        return global_var.contract_delivery_period_index_unknown
        
    assert tz_local
    assert delivery_begin_dt_local.tz.zone == (tz_local
                                               if type(tz_local) == str
                                               else
                                               tz_local.zone
                                               ), (delivery_begin_dt_local.tz.zone,
                                                   tz_local,
                                                   )

    if product == global_var.contract_product_half_hour:
        ans = int('{0:0>2}{1:0>2}{2:0>2}'.format(delivery_begin_dt_local.month,
                                                 delivery_begin_dt_local.day,
                                                 delivery_begin_dt_local.hour,
                                                 delivery_begin_dt_local.minute,
                                                 ))

    elif product == global_var.contract_product_hour:
        ans = int('{0:0>2}{1:0>2}{2:0>2}'.format(delivery_begin_dt_local.month,
                                                 delivery_begin_dt_local.day,
                                                 delivery_begin_dt_local.hour,
                                                 ))

    elif product == global_var.contract_product_bloc:
        bloc_match = re.compile(global_var.contract_profile_bloc_pattern).match(profile)
        hour1      = int(bloc_match.group(1))
        hour2      = int(bloc_match.group(2))
        assert hour1 < hour2
        ans = int('{0:0>2}{1:0>2}{2:0>2}{3:0>2}'.format(delivery_begin_dt_local.month,
                                                        delivery_begin_dt_local.day,
                                                        hour1,
                                                        hour2,
                                                        ))
    elif product == global_var.contract_product_day:
        ans = int('{0:0>2}{1:0>2}'.format(delivery_begin_dt_local.month,
                                          delivery_begin_dt_local.day,
                                          ))
    elif product == global_var.contract_product_days:
        ans = int('{0:0>2}{1:0>2}{2}'.format(delivery_begin_dt_local.month,
                                             delivery_begin_dt_local.day,
                                             int((  delivery_end_date_local
                                                  - delivery_begin_dt_local.replace(hour = 0, minute = 0)
                                                  ).total_seconds()/(3600*24)),
                                             ))
    elif product == global_var.contract_product_weekend:
        ans = int('{0:0>2}{1:0>2}'.format(delivery_begin_dt_local.month,
                                          delivery_begin_dt_local.day,
                                          ))

    elif product == global_var.contract_product_week:
        ans = int('{0:0>2}{1:0>2}'.format(delivery_begin_dt_local.month,
                                          delivery_begin_dt_local.day,
                                          ))

    elif product == global_var.contract_product_bow:
        ans = int('{0:0>2}{1:0>2}'.format(delivery_begin_dt_local.month,
                                          delivery_begin_dt_local.day,
                                          ))

    elif product == global_var.contract_product_month:
        ans = delivery_begin_dt_local.month

    elif product == global_var.contract_product_bom:
        ans = int('{0:0>2}{1:0>2}'.format(delivery_begin_dt_local.month,
                                          delivery_begin_dt_local.day,
                                          ))

    elif product == global_var.contract_product_quarter:
        ans = (delivery_begin_dt_local.month//3)+1

    elif product == global_var.contract_product_season:
        if delivery_begin_dt_local.month == 4:
            ans = global_var.contract_delivery_period_index_summer
        elif delivery_begin_dt_local.month == 10:
            ans = global_var.contract_delivery_period_index_winter
        else:
            raise ValueError(product, delivery_begin_dt_local)

    elif product == global_var.contract_product_year:
        ans = global_var.contract_delivery_period_index_year

    else:
        raise NotImplementedError(product, delivery_begin_dt_local)

    return ans


