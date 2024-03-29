

from .... import global_tools, global_var


def evolution_mean_availability(ax,
                                df,
                                unit  = None,
                                color = None,
                                step  = False,
                                diff_init = False,
                                ):
    """
        Draws in a subplot the evolution of the mean unavailbility 
        of a set of production assets.
 
        :param ax: The ax to fill
        :param df: The expected availability during the delivery
        :param unit: The power unit for the plot (MW or GW)
        :param color: The color to plot the series
        :param step: Boolean to interpolate linearly or piecewise constantly
        :param diff_init: Bool to plot relative differences
        :type ax: matplotlib.axes._subplots.AxesSubplot
        :type df: pd.Series
        :type unit: string
        :type color: string
        :type step: bool
        :type diff_init: bool
        :return: None
        :rtype: None
    """ 
    
    if diff_init:
        df = df - df.iloc[0]
    
    X, Y = global_tools.piecewise_constant_interpolators(df.index, 
                                                         df.values,
                                                         )
    
    if   unit == global_var.capacity_unavailable_gw:
        Y /= 1e3
    elif unit == global_var.capacity_unavailable_mw:
        Y = Y
    else:
        raise ValueError

    if step:
        ax.step(X,
                Y,
                where = 'post',
                label = '{0}mean {1}'.format('$\Delta$ ' if diff_init else '',
                                             unit,
                                             ),
                color = (global_var.colors[9]
                         if color is None
                         else
                         color
                         ),
                )
    else:
        ax.plot(X,
                Y,
                label = 'mean {0}'.format(unit),
                color = (global_var.colors[9]
                         if color is None
                         else
                         color
                         ),
                )

 



