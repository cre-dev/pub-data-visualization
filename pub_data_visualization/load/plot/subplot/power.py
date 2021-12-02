
#
from .... import global_var


def power(ax,
          df,
          map_code    = None,
          load_nature = None,
          load_unit   = None,
          **kwargs,
          ):
    """
        Draws in a subplot the load data.
 
        :param ax: The ax to fill
        :param df: The load data
        :param map_code: The delivery zone
        :param load_nature: The nature of the data to plot
        :param kwargs: additional parameter for the plt.plot function
        :type ax: matplotlib.axes._subplots.AxesSubplot
        :type df: pd.DataFrame
        :type map_code: string
        :type load_nature: string
        :type kwargs: dict
        :return: None
        :rtype: None
    """ 
    
    # dg = df.xs((map_code,
    #             load_nature,
    #             ),
    #            level = (global_var.geography_map_code,
    #                     global_var.load_nature,
    #                     ),
    #            axis  = 1,
    #            )
    dg = df.loc[  (df[global_var.geography_map_code] == map_code)
                & (df[global_var.load_nature] == load_nature)
                ]
               
    dg = dg.dropna()
    ax.plot(dg.index,
            dg[load_unit],
            **kwargs,
            )
