
import matplotlib as mpl
#
from .... import global_var


def forecasting_error(ax,
                      df,
                      load_unit = None,
                      load_observation_nature = None,
                      load_forecast_nature    = None,
                      **kwargs
                      ):
    """
        Draws in a subplot the forecasting error.
 
        :param ax: The ax to fill
        :param df: The load data
        :param load_observation_nature: The nature of the observation data to plot
        :param load_forecast_nature: The nature of the forecasts to plot
        :param kwargs: additional parameter for the plt.plot function
        :type ax: matplotlib.axes._subplots.AxesSubplot
        :type df: pd.DataFrame
        :type load_observation_nature: string
        :type load_forecast_nature: string
        :type kwargs: dict
        :return: None
        :rtype: None
    """

    forecasting_error = (  df.loc[df[global_var.load_nature] == load_observation_nature][load_unit]
                         - df.loc[df[global_var.load_nature] == load_forecast_nature][load_unit]
                         )
    forecasting_error = forecasting_error.squeeze().dropna()
    
    ax.plot(forecasting_error.index,
            forecasting_error, 
            **kwargs,
            )
    ax.fill_between(
                    forecasting_error.index,
                    forecasting_error, 
                    where = (forecasting_error) > 0,
                    label = 'Positive errors', 
                    color = mpl.colors.cnames['deepskyblue'],
                    )
    ax.fill_between(
                    forecasting_error.index,
                    forecasting_error, 
                    where = (forecasting_error) < 0,
                    label = 'Negative errors', 
                    color = mpl.colors.cnames['firebrick'],
                    )
    ax.plot(
            [forecasting_error.index.min(),
             forecasting_error.index.max(),
             ],
            [0,0], 
            color = 'k', 
            ls    = ':',
            )            

    
    
    
