

#
from .... import global_tools


def curve(ax,
          df,
          physical_quantity = None,
          **kwargs,
          ):
    """
        Draws in a subplot the weather data.
 
        :param ax: The ax to fill
        :param df: The production data
        :param physical_quantity: The weather quantity to plot
        :param kwargs: additional parameter for the plt.plot function
        :type ax: matplotlib.axes._subplots.AxesSubplot
        :type df: pd.DataFrame
        :type physical_quantity: string
        :type kwargs: dict
        :return: None
        :rtype: None
    """ 
    
    dg = df[physical_quantity]
    assert not dg.empty
    
    ax.plot(dg.index,
            dg,
            label = global_tools.format_latex(dg.name),
            **kwargs,
            )



    
    