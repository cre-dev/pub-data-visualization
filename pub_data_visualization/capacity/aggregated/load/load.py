

#
from .... import global_var
from . import entsoe, rte



def load(source   = None,
         map_code = None,
         ):
    """
        Calls the appropriate loader of the capacities
        for the given map_code.
 
        :param source: The data source
        :param map_code: The zone
        :type source: string
        :type map_code: string
        :return: The selected capacities
        :rtype: pd.DataFrame
    """
    
    if source == global_var.data_source_capacity_entsoe:
        df = entsoe.load(map_code = map_code)
    
    elif source == global_var.data_source_capacity_rte:
        df = rte.load(map_code = map_code)
    
    else: 
        raise ValueError('Incorrect source={0} '.format(source))

    return df

