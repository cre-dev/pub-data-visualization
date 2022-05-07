
import os
#
from ... import global_tools, global_var
from . import subplot
#
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters; register_matplotlib_converters()
from matplotlib.font_manager import FontProperties
global_tools.set_mpl(mpl, plt, FontProperties())
#

        
def forecasting_error(df,
                      source_load             = None,
                      load_unit               = None,
                      load_nature_forecast    = None,
                      map_code                = None,
                      date_min                = None,
                      date_max                = None,
                      folder_out              = None,
                      close                   = True,
                      figsize                 = global_var.figsize_horizontal,
                      ):
    """
        Plots the load and the forecasts by creating a figure and
        calling the function to fill the subplot.
 
        :param df: The load data
        :param source_load: The data source
        :param load_observation_nature: The nature of the observation data
        :param load_forecast_nature: The nature of the forecasts
        :param map_code: The delivery zone
        :param date_min: The left bound
        :param date_max: The right bound
        :param folder_out: The folder where the figure is saved
        :param close: Boolean to close the figure after it is saved
        :param figsize: Desired size of the figure
        :type df: pd.DataFrame
        :type source_load: string
        :type load_observation_nature: string
        :type load_forecast_nature: string
        :type map_code: string
        :type date_min: pd.Timestamp
        :type date_max: pd.Timestamp
        :param folder_out: string
        :param close: bool
        :param figsize: (int,int)
        :return: None
        :rtype: None
    """
    
    ### Interactive mode
    if close:
        plt.ioff()
    else:
        plt.ion()
    
    ### Plots
    fig, ax = plt.subplots(figsize = figsize, 
                           nrows   = 1,
                           ncols   = 1,
                           )
    
    ### Subplots
    subplot.power(ax,
                  df,
                  map_code    = map_code,
                  load_unit   = load_unit,
                  load_nature = global_var.load_nature_observation,
                  label       = global_tools.format_latex(' - '.join([e
                                                                      for e in [map_code,
                                                                                global_var.load_nature_observation,
                                                                                ]
                                                                      if bool(e)
                                                                      ])),
                  )
    subplot.forecasting_error(ax,
                              df,
                              load_unit = load_unit,
                              load_observation_nature = global_var.load_nature_observation,
                              load_forecast_nature    = load_nature_forecast,
                              color     = 'b',
                              linewidth = 0.5,
                              label     = global_tools.format_latex(' - '.join([e
                                                                                for e in [map_code,load_nature_forecast]
                                                                                if bool(e)
                                                                                ]) + ' error'),
                               )

    ### Labels
    ax.set_xlabel(global_tools.format_latex(df.index.name))
    ax.set_ylabel(global_tools.format_latex(load_unit))
            
    ### Ticks
    ax.xaxis.set_major_formatter(mdates.DateFormatter(global_var.dt_formatter))
    fig.autofmt_xdate()
    if date_min and date_max:
        ax.set_xlim(date_min, date_max)
    
    ### Add legend
    lns01, labs01 = ax.get_legend_handles_labels()
    by_label0 = dict(zip(labs01, lns01))
    ax.legend(by_label0.values(),
              by_label0.keys(),
              loc = 0,
              )
                    
    ### Finalize
    title = ' - '.join(filter(None, ['source_load = {source_load}',
                                     'map_code = {map_code}',
                                     ])).format(map_code    = map_code,
                                                source_load = source_load,
                                                )
    fig.suptitle(global_tools.format_latex(title))
    
    ### Save
    full_path = os.path.join(folder_out, 
                             "load_forecasting_error",
                             "period_{begin}_{end}".format(begin = date_min.strftime(global_var.dt_formatter_file),
                                                           end   = date_max.strftime(global_var.dt_formatter_file),
                                                           ) if date_min and date_max else '',
                             title,
                             )
    os.makedirs(os.path.dirname(full_path), 
                exist_ok = True, 
                )
    plt.savefig(
                full_path + ".png",
                format = "png",
                bbox_inches = "tight",
                )
    if close:
        plt.close()

        
    