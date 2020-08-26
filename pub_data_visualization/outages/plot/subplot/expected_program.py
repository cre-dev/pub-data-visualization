

#
from .... import global_tools




def expected_program(ax,
                     ds,
                     **kwargs,
                     ):
    """
        Draws in a subplot the expected availability program
        of a set of production assets.
 
        :param ax: The ax to fill
        :param ds: The expected availability program
        :param kwargs: Additional arugments for the plt.plot function
        :type ax: matplotlib.axes._subplots.AxesSubplot
        :type ds: pd.Series
        :type kwargs: dict
        :return: None
        :rtype: None
    """ 
    
    X, Y = global_tools.piecewise_constant_interpolators(ds.index,
                                                         ds.values,
                                                         )

            
    # Plot program
    ax.plot(X,
            Y, 
            markevery  = 1,
            markersize = 10,
            ls = '-.',
            **kwargs,
            )

    
