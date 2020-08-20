

#
from .. import global_var

def format_contract_name(year,
                         product,
                         delivery_period,
                         profile,
                         ):
    """
        Returns a generic name for a given contract.
 
        :param year: The year of the delivery
        :param product: The type of delivery contract (year, month, etc.)
        :param delivery_period: The index of the delivery contract
        :param profile: profile of the delivery contract
        :type year: int
        :type product: string
        :type delivery_periodx: int
        :type profile: string
        :return: The formatted name of the contract
        :rtype: string
    """
    assert len(str(year)) == 4
    assert str(year).isdigit()
    assert type(product) == str
    assert profile in {global_var.contract_profile_base,
                       global_var.contract_profile_ofpk,
                       global_var.contract_profile_peak,
                       }
    return '{year}.{product}{delivery_period}.{profile}'.format(year            = year,
                                                                product         = product,
                                                                delivery_period = delivery_period,
                                                                profile         = profile,
                                                                )
    
