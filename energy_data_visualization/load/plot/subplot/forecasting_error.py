
import matplotlib as mpl
#
from .... import global_var


def forecasting_error(ax,
                      df,
                      load_observation_nature = None,
                      load_forecast_nature    = None,
                      **kwargs
                      ):
    forecasting_error = (  df.xs(load_observation_nature, level = global_var.load_nature, axis = 1)
                         - df.xs(load_forecast_nature,    level = global_var.load_nature, axis = 1)
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

    
    
    
