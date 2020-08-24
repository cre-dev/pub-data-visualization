
#
from .... import global_var
#

def power(ax,
          df,
          map_code          = None,
          production_nature = None,
          production_source = None,
          unit_name         = None,
          **kwargs,
          ):
    """
        Draws in a subplot the weather data.
 
        :param ax: The ax to fill
        :param df: The production data
        :param map_code: The delivery zone
        :param production_nature: The nature of the data to plot
        :param production_source: The energy source of the production
        :param unit_name: The name of the production asset
        :param kwargs: additional parameter for the plt.plot function
        :type ax: matplotlib.axes._subplots.AxesSubplot
        :type df: pd.DataFrame
        :type map_code: string
        :type production_nature: string
        :type production_source: string
        :type unit_name: string
        :type kwargs: dict
        :return: None
        :rtype: None
    """ 

    if map_code:
        df = df.xs(map_code,
                   level = global_var.geography_map_code,
                   axis  = 1,
                   )
    if production_source:
        df = df.xs(production_source,
                   level = global_var.production_source,
                   axis  = 1,
                   )
    if unit_name:
        df = df.xs(unit_name,
                   level = global_var.unit_name,
                   axis  = 1,
                   )
    if production_nature:
        df = df.xs(production_nature,
                   level = global_var.production_nature,
                   axis  = 1,
                   )

    dg = df.sum(axis = 1)
    dg = dg.dropna()
    assert not dg.empty
    
    ax.plot(dg.index,
            dg,
            **kwargs,
            )
    
    
    
