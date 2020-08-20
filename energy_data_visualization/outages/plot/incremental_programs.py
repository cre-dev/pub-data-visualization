

import os
#
from ... import global_tools, global_var
from . import subplot

#
import seaborn as sn
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters; register_matplotlib_converters()
from matplotlib.font_manager import FontProperties
global_tools.set_mpl(mpl, plt, FontProperties())
#

def incremental_programs(df_programs,
                         date_min          = None,
                         date_max          = None, 
                         diff_init         = False,
                         smoother          = None,
                         source_outages    = None,
                         map_code          = None,
                         company_outages   = None,
                         production_source = None,
                         unit_name         = None,
                         figsize           = global_var.figsize_horizontal,
                         folder_out        = None, 
                         close             = True,
                         ):
    """
    Interactive mode
    """
    if close:
        plt.ioff()
    else:
        plt.ion()


    """
    Plots
    """
    fig, ax = plt.subplots(figsize = figsize,
                           nrows = 1,
                           ncols = 1,
                           )     
    # subplot
    subplot.incremental_programs(ax,
                                 df_programs,
                                 diff_init = diff_init,
                                 smoother  = smoother, 
                                 )
    
    ### Add legend
    lns01, labs01 = ax.get_legend_handles_labels()
    by_label0 = dict(zip(labs01, lns01))
    ax.legend(by_label0.values(),
              by_label0.keys(),
              loc = 0,
              )

    
    ### Ticks
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%a %d/%m/%Y %H:%M"))
    fig.autofmt_xdate()
    if date_min and date_max:
        ax.set_xlim(date_min, date_max)
    
    ### labels                
    ax.set_ylabel(global_var.outage_expected_availability_mw)
    
    
    ### Add legend
    lns01, labs01 = ax.get_legend_handles_labels()
    by_label0 = dict(zip(labs01, lns01))
    ax.legend(by_label0.values(),
              by_label0.keys(),
              loc = 0,
              )
                    
    ### Finalize
    title = ' - '.join(filter(None, [
                                     'source_outages = {source_outages}'       if source_outages    else '',
                                     'map_code = {map_code}'                   if map_code          else '',
                                     'company = {company_outages}'             if company_outages   else '',
                                     'production_source = {production_source}' if production_source else '',
                                     'unit_name = {unit_name}'                 if unit_name         else '',
                                     ])).format(source_outages    = source_outages,
                                                map_code          = map_code,
                                                company_outages   = company_outages,
                                                production_source = production_source,
                                                unit_name         = unit_name,
                                                )
    fig.suptitle(global_tools.format_latex(title))
    plt.tight_layout(rect = [0, 0.01, 1, 0.95])

    # Save
    full_path = os.path.join(folder_out,
                             "outages_incremental_programs", 
                             "period_{begin}_{end}".format(begin = date_min.strftime('%Y%m%d_%H%M'), 
                                                           end   = date_max.strftime('%Y%m%d_%H%M'), 
                                                           ) if date_min and date_max else '',
                             title
                             )
    os.makedirs(os.path.dirname(full_path),
                exist_ok = True, 
                )
    plt.savefig(full_path + ".png",
                format = "png",
                bbox_inches = "tight",
                )

    if close:
        plt.close()


