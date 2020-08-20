

#
from .. import global_var

def format_contract_name(year,
                         product,
                         delivery_period,
                         profile,
                         ):
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
    
