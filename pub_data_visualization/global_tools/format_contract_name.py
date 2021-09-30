
import re
#
from .. import global_var

def format_contract_name(year,
                         frequency,
                         delivery_period,
                         profile   = None,
                         map_code  = None,
                         commodity = None,
                         ):
    """
        Returns a generic name for a given contract.
 
        :param year: The year of the delivery
        :param frequency: The type of delivery contract (year, month, etc.)
        :param delivery_period: The index of the delivery contract
        :param profile: profile of the delivery contract
        :type year: int
        :type frequency: string
        :type delivery_periodx: int
        :type profile: string
        :return: The formatted name of the contract
        :rtype: string
    """
    assert len(str(year)) == 4
    assert str(year).isdigit()
    assert type(frequency) == str
    assert (   re.compile(global_var.contract_profile_bloc_pattern).match(profile)
            or profile in {global_var.contract_profile_gas,
                           global_var.contract_profile_base,
                           global_var.contract_profile_ofpk,
                           global_var.contract_profile_peak,
                           global_var.contract_profile_hour,
                           global_var.contract_profile_half_hour,
                           }
            )
    
    return '.'.join(filter(None, [map_code,
                                  commodity,
                                  '{year}{frequency}{delivery_period}'.format(year            = year,
                                                                              frequency       = frequency,
                                                                              delivery_period = delivery_period,
                                                                              ),
                                  (profile
                                   if profile not in [global_var.contract_profile_gas,
                                                      global_var.contract_profile_hour,
                                                      global_var.contract_profile_half_hour,
                                                      global_var.contract_profile_bloc,
                                                      ]
                                   else
                                   None
                                   ),
                                  ]))
    
