

import pandas as pd
#
from .. import global_var


def compute_maturity(dt                  = None,
                     frequency           = None,
                     delivery_begin_date = None,
                     commodity           = None,
                     ):
    
    """
        Computes the maturity for a pair (contract, trade/order).
 
        :param dt: The datetime of the trade/order
        :param frequency: The type of delivery contract (year, month, etc.)
        :param delivery_begin_date: The beginning date of the delivery
        :type dt: pd.Timestamp
        :type frequency: string
        :type delivery_begin_date: pd.Timestamp
        :return: The maturity for the pair (contract, trade/order)
        :rtype: string
    """
        
    delivery_date = delivery_begin_date.floor('D')
    if commodity == global_var.commodity_gas:
        action_date = (dt.floor('D') - pd.Timedelta(hours = 6)).floor('D')
    elif commodity == global_var.commodity_electricity:
        action_date = dt.floor('D')
    else:
        raise ValueError
    
    ### D+X
    if frequency in [global_var.contract_frequency_bloc,
                     global_var.contract_frequency_day,
                     global_var.contract_frequency_days,
                     global_var.contract_frequency_half_hour,
                     global_var.contract_frequency_hour,
                     ]:
        nb_days = int((delivery_date - action_date).total_seconds()//(3600*24))
        assert nb_days >= 0
        return global_var.maturity_day.format(nb_days = nb_days)
    
    ### WE+X
    elif frequency in [global_var.contract_frequency_weekend,
                       ]:
        action_floor   = action_date - pd.DateOffset(days = action_date.timetuple().tm_wday)
        delivery_floor = delivery_date - - pd.DateOffset(days = action_date.timetuple().tm_wday)
        nb_weeks = int(round((delivery_floor - action_floor).total_seconds()//(3600*24*7)))
        if nb_weeks >= 0:
            return global_var.maturity_weekend.format(nb_weeks = nb_weeks)
        else:
            return global_var.maturity_unknown
    
    ### W+X
    elif frequency in [global_var.contract_frequency_bow,
                       global_var.contract_frequency_week,
                       global_var.contract_frequency_weekbgn,
                       ]:
        action_floor   = action_date - pd.DateOffset(days = action_date.timetuple().tm_wday)
        delivery_floor = delivery_date - - pd.DateOffset(days = action_date.timetuple().tm_wday)
        nb_weeks = int(round((delivery_floor - action_floor).total_seconds()//(3600*24*7)))
        assert nb_weeks >= 0
        return global_var.maturity_week.format(nb_weeks = nb_weeks)
    
    ### M+X
    elif frequency in [global_var.contract_frequency_fr,
                       global_var.contract_frequency_bk,
                       global_var.contract_frequency_bom,
                       global_var.contract_frequency_month,
                       global_var.contract_frequency_months,
                       ]:
        action_floor   = action_date.replace(day = 1)
        delivery_floor = delivery_date.replace(day = 1)
        nb_months      = delivery_floor.month - action_floor.month + (delivery_floor.year - action_floor.year)*12
        assert nb_months >= 0
        return global_var.maturity_month.format(nb_months = nb_months)

    ### Q+X
    elif frequency in [global_var.contract_frequency_boq,
                       global_var.contract_frequency_quarter,
                       ]:
        action_floor   = action_date.replace(day = 1, month = 1 + 3*((action_date.month - 1)//3))
        delivery_floor = delivery_date.replace(day = 1, month = 1 + 3*((delivery_date.month - 1)//3))
        nb_quarters    = (delivery_floor.month - action_floor.month)//3 + 4*(delivery_floor.year - action_floor.year)
        assert nb_quarters >= 0
        return global_var.maturity_quarter.format(nb_quarters = nb_quarters)
    
    ### S+X
    elif frequency in [global_var.contract_frequency_bos,
                       global_var.contract_frequency_season,
                       ]:
        action_floor   = action_date.replace(day = 1, month = 4 + 6*((action_date.month - 4)//6) % 12) - pd.DateOffset(years = int(action_date.month <= 3))
        delivery_floor = delivery_date.replace(day = 1, month = 4 + 6*((delivery_date.month - 4)//6) % 12) - pd.DateOffset(years = int(delivery_date.month <= 3))
        nb_seasons     = (delivery_floor.month - action_floor.month)//6 + 2*(delivery_floor.year - action_floor.year)
        assert nb_seasons >= 0
        return global_var.maturity_season.format(nb_seasons = nb_seasons)
    
    ### Y+X
    elif frequency in [global_var.contract_frequency_boy,
                       global_var.contract_frequency_year,
                       global_var.contract_frequency_years,
                       ]:
        action_floor   = action_date.replace(day = 1, month = 1)
        delivery_floor = delivery_date.replace(day = 1, month = 1)
        nb_years       = delivery_floor.year - action_floor.year
        assert nb_years >= 0
        return global_var.maturity_year.format(nb_years = nb_years)    
        
        
    ### GY+X
    elif frequency in [global_var.contract_frequency_gas_year,
                       ]:
        action_floor   = action_date.replace(day = 1, month = 10) - pd.DateOffset(years = 1)*int(action_date.month <= 10)
        delivery_floor = delivery_date.replace(day = 1, month = 10) - pd.DateOffset(years = 1)*int(delivery_date.month <= 10)
        nb_years       = (delivery_floor.year - action_floor.year)
        assert nb_years >= 0
        return global_var.maturity_gas_year.format(nb_years = nb_years)
    
    elif frequency in [global_var.contract_frequency_unknown,
                       global_var.contract_frequency_spread,
                       ]:
        return global_var.maturity_unknown
    
    else:
        raise NotImplementedError 
