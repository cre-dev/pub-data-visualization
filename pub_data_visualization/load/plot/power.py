
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

        
def power(df,
          source_load = None,
          load_nature = None,
          map_code    = None,
          date_min    = None,
          date_max    = None,
          figsize     = global_var.figsize_horizontal,
          folder_out  = None,
          close       = True,
          ):
    """
        Plots the load data by creating a figure and
        calling the function to fill the subplot.
 
        :param df: The load data
        :param source_load: The data source
        :param load_nature: The nature of the data to plot
        :param map_code: The delivery zone
        :param date_min: The left bound
        :param date_max: The right bound
        :param figsize: Desired size of the figure
        :param folder_out: The folder where the figure is saved
        :param close: Boolean to close the figure after it is saved
        :type df: pd.DataFrame
        :type source_load: string
        :type load_nature: string
        :type map_code: string
        :type date_min: pd.Timestamp
        :type date_max: pd.Timestamp
        :param figsize: (int,int)
        :param folder_out: string
        :param close: bool
        :return: None
        :rtype: None
    """
    
    ### Interactive mode
    if close:
        plt.ioff()
    else:
        plt.ion()
    

    ### Checks
    assert df.index.is_unique
    
    ### Figure
    fig, ax = plt.subplots(figsize = figsize,
                           nrows   = 1,
                           ncols   = 1,
                           )
    
    ### Subplot
    subplot.power(ax,
                  df,
                  map_code    = map_code,
                  load_nature = load_nature,
                  label       = global_tools.format_latex(' - '.join([e
                                                                      for e in [map_code,load_nature]
                                                                      if bool(e)
                                                                      ])),
                  )
        
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
    title = global_tools.format_latex(' - '.join(filter(None, ['map_code = {map_code}',
                                                               'source_load = {source_load}',
                                                               ])).format(map_code    = map_code,
                                                                          source_load = source_load,
                                                                          ))
    fig.suptitle(title)
    plt.tight_layout(rect = [0.01, 0.01, 0, 0.03])
    
    ### Save
    full_path = os.path.join(folder_out, 
                             "load_power",
                             "period_{begin}_{end}".format(begin = date_min.strftime('%Y%m%d_%H%M'), 
                                                           end   = date_max.strftime('%Y%m%d_%H%M'), 
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

        
    