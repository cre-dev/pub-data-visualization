

import pandas as pd
import re
#
from .. import global_var
from . import compute_delivery_dates


def compute_delivery_windows(frequency                 = None,
                             delivery_begin_year_local = None,
                             delivery_period_index     = None,
                             profile                   = None,
                             delivery_begin_date_local = None,
                             tz_local                  = None,
                             ):
    """
        Computes the delivery windows of a given contract.
 
        :param frequency: The type of delivery contract (year, month, etc.)
        :param delivery_begin_year_local: The year of the delivery
        :param delivery_period_index: The index of the delivery contract
        :param profile: The profile of the delivery
        :param delivery_begin_date_local: The beginning date of the delivery
        :param tz_local: The local timezone
        :type frequency: string
        :type delivery_begin_year_local: int
        :type delivery_period_index: int
        :type profile: string
        :type delivery_begin_date_local: pd.Timestamp
        :type tz_local: pytz.tzfile
        :return: The delivery windows as list of intervals
        :rtype: list of pairs of pd.Timestamp
    """
    bloc_match = re.compile(global_var.contract_profile_bloc_pattern).match(profile)
    if not (   profile in [global_var.contract_profile_base,
                           global_var.contract_profile_peak,
                           global_var.contract_profile_ofpk,
                           global_var.contract_profile_hour,
                           global_var.contract_profile_half_hour,
                           global_var.contract_profile_wday2024,
                           global_var.contract_profile_wday1620,
                           global_var.contract_profile_wend2024,
                           ]
            or bloc_match
            ):
        raise NotImplementedError('profile = {0}'.format(profile))
        
    if not delivery_begin_date_local:
        delivery_begin_date_local, delivery_end_date_local = compute_delivery_dates(delivery_begin_year   = delivery_begin_year_local,
                                                                                    frequency             = frequency,
                                                                                    delivery_period_index = delivery_period_index,
                                                                                    local_tz              = tz_local,
                                                                                    )
    else:
        dd, delivery_end_date_local = compute_delivery_dates(delivery_begin_year   = delivery_begin_year_local,
                                                             delivery_begin_date   = delivery_begin_date_local,
                                                             frequency             = frequency,
                                                             delivery_period_index = delivery_period_index,
                                                             local_tz              = tz_local,
                                                             )
        if not dd == delivery_begin_date_local:
            assert profile == global_var.contract_profile_peak, 'Incorrect begin_date, profile : {0}, {1}'.format(delivery_begin_date_local,
                                                                                                                  profile,
                                                                                                                  )   
        
    if   profile == global_var.contract_profile_base:
        return [(delivery_begin_date_local,
                 delivery_end_date_local,
                 )]

    elif profile == global_var.contract_profile_peak:
        return [(delivery_begin_date_local + pd.DateOffset(days = ii_day) + pd.DateOffset(hours = 8),
                 delivery_begin_date_local + pd.DateOffset(days = ii_day) + pd.DateOffset(hours = 20),
                 )
                for ii_day in range((  delivery_end_date_local.tz_localize(None)
                                     - delivery_begin_date_local.tz_localize(None)
                                     ).days)
                if (  (delivery_begin_date_local + pd.DateOffset(days = ii_day)).weekday() not in [5, 6]
                    or (delivery_end_date_local - delivery_begin_date_local).days <= 2 # Il semble que les contrats week peak n'incluent pas les we mais les produits we peak existent
                    )
                ]

    elif profile == global_var.contract_profile_ofpk:
        return [(delivery_begin_date_local + pd.DateOffset(days = ii_day) + pd.DateOffset(hours = begin_hour),
                 delivery_begin_date_local + pd.DateOffset(days = ii_day) + pd.DateOffset(hours = end_hour),
                 )
                for ii_day in range((  delivery_end_date_local.tz_localize(None)
                                     - delivery_begin_date_local.tz_localize(None)
                                     ).days)
                for begin_hour, end_hour in ([(0,8), (20,24)]
                                             if
                                             (delivery_begin_date_local + pd.DateOffset(days = ii_day)).weekday() not in [5,6]
                                             else
                                             [(0,24)]
                                             )
                ]

    elif profile == global_var.contract_profile_hour:
        hour_match = re.compile(global_var.contract_delivery_period_index_hour_pattern).match(str(delivery_period_index))
        hour       = int(hour_match.group(3))
        return [(delivery_begin_date_local + pd.DateOffset(hours = hour),
                 delivery_begin_date_local + pd.DateOffset(hours = hour + 1),
                 )]

    elif profile == global_var.contract_profile_half_hour:
        half_hour_match = re.compile(global_var.contract_delivery_period_index_half_hour_pattern).match(str(delivery_period_index))
        hour            = int(half_hour_match.group(3))
        minute          = int(half_hour_match.group(4))
        return [(delivery_begin_date_local + pd.DateOffset(hours = hour, minutes = minute),
                 delivery_begin_date_local + pd.DateOffset(hours = hour, minutes = minute + 30),
                 )]

    elif bool(bloc_match):
        hour_begin = int(bloc_match.group(1))
        hour_end   = int(bloc_match.group(2))
        return [(delivery_begin_date_local + pd.DateOffset(hours = hour_begin),
                 delivery_begin_date_local + pd.DateOffset(hours = hour_end),
                 )]
    
    elif profile == global_var.contract_profile_wday2024:
        begin_hour = 20
        end_hour   = 24
        return [(delivery_begin_date_local + pd.DateOffset(days = ii_day) + pd.DateOffset(hours = begin_hour),
                 delivery_begin_date_local + pd.DateOffset(days = ii_day) + pd.DateOffset(hours = end_hour),
                 )
                for ii_day in range(5)
                ]

    elif profile == global_var.contract_profile_wday1620:
        begin_hour = 16
        end_hour   = 20
        return [(delivery_begin_date_local + pd.DateOffset(days = ii_day) + pd.DateOffset(hours = begin_hour),
                 delivery_begin_date_local + pd.DateOffset(days = ii_day) + pd.DateOffset(hours = end_hour),
                 )
                for ii_day in range(5)
                ]
    
    elif profile == global_var.contract_profile_wend2024:
        begin_hour = 20
        end_hour   = 24
        return [(delivery_begin_date_local + pd.DateOffset(days = ii_day) + pd.DateOffset(hours = begin_hour),
                 delivery_begin_date_local + pd.DateOffset(days = ii_day) + pd.DateOffset(hours = end_hour),
                 )
                for ii_day in range(2)
                ]
    

    else:
        raise NotImplementedError('Incorrect profile : {0}'.format(profile))