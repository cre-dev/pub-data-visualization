

#



def nameplate_capacity(ax,
                       df,
                       ): 
    """
        Draws in a subplot the nameplate capacity
        of a set of production assets
        as a horizontal line.
 
        :param ax: The ax to fill
        :param df: The nameplate capacity at different dates
        :type ax: matplotlib.axes._subplots.AxesSubplot
        :type df: pd.Series
        :return: None
        :rtype: None
    """   

    ax.plot([df.index.min(), df.index.max()], 
            [df.values.max() for kk in range(2)], 
            ls = ':', 
            linewidth = 0.5,
            color     = 'k', 
            label     = 'nameplate capacity',
            )
