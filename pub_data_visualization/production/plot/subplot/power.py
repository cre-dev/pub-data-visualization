
#
from .... import global_var
#

def power(ax,
          df,
          map_code          = None,
          production_nature = None,
          production_unit   = None,
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
        df = df.loc[df[global_var.geography_map_code] == map_code]
    if production_source:
        df = df.loc[df[global_var.production_source] == production_source]
    if unit_name:
        df = df.loc[df[global_var.unit_name] == unit_name]
    if production_nature:
        df = df.loc[df[global_var.production_nature] == production_nature]

    dg = df.groupby(df.index)[production_unit].sum()
    dg = dg.dropna()
    assert not dg.empty
    
    ax.plot(dg.index,
            dg,
            **kwargs,
            )
    
    
    
