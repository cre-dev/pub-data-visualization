

from .... import global_var


def regression_delays(ax,
                      df,
                      ):
    """
        Plots the announced and finally observed lengths of the outages
        of a set of units with a regression line in a subplot.
        
        Permanent plant shutdowns are a problem for the regression.
 
        :param ax: The ax to fill
        :param df: The outages dataframe
        :type ax: matplotlib.axes._subplots.AxesSubplot
        :type df: pd.DataFrame
        :return: None
        :rtype: None
    """ 
    
    dg_grouped = df.reset_index().groupby(global_var.publication_id)
    
    X = (  dg_grouped[global_var.outage_end_dt_UTC].head(1)
         - dg_grouped[global_var.outage_begin_dt_UTC].head(1)
         ).reset_index(drop = True).dt.total_seconds()/3600
    Y = (  dg_grouped[global_var.outage_end_dt_UTC].tail(1)
         - dg_grouped[global_var.outage_begin_dt_UTC].tail(1)
         ).reset_index(drop = True).dt.total_seconds()/3600
    
    ax.scatter(X,
               Y,
               )
    
    ax.plot([min(min(X),min(Y)),max(max(X),max(Y))],
            [min(min(X),min(Y)),max(max(X),max(Y))],
            color = 'k', 
            ls    = '--',
            label = 'first bisector'
            )
    
    ### regression
    a = (1/(X.T@X))*(X.T@Y)
    ax.plot([min(min(X),min(Y)),max(max(X),max(Y))],
            [a*min(min(X),min(Y)),a*max(max(X),max(Y))],
            color = 'g', 
            ls    = ':',
            label = 'linear fit a = {0:.2f}'.format(a),
            )
    
    