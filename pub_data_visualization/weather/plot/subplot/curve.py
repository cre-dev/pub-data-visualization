

#
from .... import global_tools, global_var


def curve(ax,
          df,
          nature            = None,
          physical_quantity = None,
          **kwargs,
          ):
    """
        Draws in a subplot the weather curve.
 
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
    
    ds = df.loc[  (df[global_var.weather_nature] == nature)
                & (df[global_var.weather_physical_quantity] == physical_quantity)
                ][global_var.weather_physical_quantity_value]
    assert not ds.empty
    
    ax.plot(ds.index,
            ds,
            label = global_tools.format_latex(physical_quantity),
            **kwargs,
            )



    
    