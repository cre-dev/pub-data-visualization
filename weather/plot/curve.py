

import os
#
import global_tools
import global_var
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
                  physical_quantity = physical_quantity,
                  )
    
    ### Ticks
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%a %d/%m/%Y %H:%M"))
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
                                     'physical_quantity = {physical_quantity}' if physical_quantity else '',
                                     ])).format(nature            = nature,
                                                source            = source,
                                                physical_quantity = physical_quantity,
                                                )
    fig.suptitle(global_tools.format_latex(title))
    plt.tight_layout(rect = [0, 0.01, 1, 0.95])
    
    ### Save
    full_path = os.path.join(folder_out, 
                             "weather_curve", 
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
        plt.close(fig)

        
    