
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

        
def power(df,
          source_load = None,
          load_nature = None,
          map_code    = None,
          date_min    = None,
          date_max    = None,
          folder_out  = None,
          close       = True,
          figsize     = global_var.figsize_horizontal,
          ):
    
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
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%a %d/%m/%Y %H:%M"))
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

        
    