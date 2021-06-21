

#
from .... import global_var
from . import rte


def load(source   = None,
         map_code = None,
         ):
    """
        Calls the appropriate loader of the unit
        capacities for the given map_code.
 
        :param source: The data source
        :param map_code: The zone
        :type source: string
        :type map_code: string
        :return: The selected unit capacities
        :rtype: pd.DataFrame
    """
    
    if source == global_var.data_source_capacity_rte:
        df = rte.load(map_code = map_code)
    
    else: 
        raise ValueError('Incorrect source={0} '.format(source))

    return df
