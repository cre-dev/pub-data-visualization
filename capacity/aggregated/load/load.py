

#
import global_var
from . import rte
from . import entsoe


def load(source   = None,
         map_code = None,
         ):
    
    if source == global_var.data_source_entsoe:
        df = entsoe.load(map_code = map_code)
    
    elif source == global_var.data_source_rte:
        df = rte.load(map_code = map_code)
    
    else: 
        raise ValueError('Incorrect source={0} '.format(source))

    return df

