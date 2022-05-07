

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
    

def curve(df,
          date_min   = None,
          date_max   = None,
          nature     = None,
          source     = None,
          physical_quantity = None,
          folder_out = None,
          close      = True,
          figsize    = global_var.figsize_horizontal,
          ):
    """
        Plots the weather data by creating a figure and
        calling the function to fill the subplot.
 
        :param df: The weather data
        :param date_min: The left bound
        :param date_max: The right bound
        :param nature: The nature of the weather data to plot
        :param source: The source of the weather data to plot
        :param physical_quantity: The weather quantity to plot
        :param folder_out: The folder where the figure is saved
        :param close: Boolean to close the figure after it is saved
        :param figsize: Desired size of the figure
        :type df: pd.DataFrame
        :type date_min: pd.Timestamp
        :type date_max: pd.Timestamp
        :type nature: string
        :type source: string
        :type physical_quantity: string
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
    
    ### Figure
    fig, ax = plt.subplots(figsize = figsize, 
                           nrows   = 1, 
                           ncols   = 1, 
                           )
    
    ### Subplot
    subplot.curve(ax,
                  df,
                  nature            = nature,
                  physical_quantity = physical_quantity,
                  )
    
    ### Ticks
    ax.xaxis.set_major_formatter(mdates.DateFormatter(global_var.dt_formatter))
    fig.autofmt_xdate()
    if date_min and date_max:
        ax.set_xlim(date_min, date_max)
    
    ### labels                
    ax.set_ylabel(global_tools.format_latex(physical_quantity))
    ax.set_xlabel(global_tools.format_latex(df.index.name))
    
    ### Add legend
    lns01, labs01 = ax.get_legend_handles_labels()
    by_label0 = dict(zip(labs01, lns01))
    ax.legend(by_label0.values(),
              by_label0.keys(),
              loc = 0,
              )
                    
    ### Finalize
    title = ' - '.join(filter(None, ['source = {source}'if source else '',
                                     'nature = {nature}' if nature else '',
                                     ])).format(nature            = nature,
                                                source            = source,
                                                physical_quantity = physical_quantity,
                                                )
    fig.suptitle(global_tools.format_latex(title))
    plt.tight_layout(rect = [0, 0.01, 1, 0.95])
    
    ### Save
    full_path = os.path.join(folder_out, 
                             "weather_curve", 
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
        plt.close(fig)

        
    