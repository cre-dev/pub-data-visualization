
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
import matplotlib.patches as mpatches



###############################################################################    

def regression_delays(df,
                      source            = None,
                      company           = None,
                      production_source = None,
                      unit_name         = None,
                      figsize           = global_var.figsize_horizontal,
                      folder_out        = None,
                      close             = True,
                      ):   
    """
        Plots the announced and finally observed lengths of the outages
        with a regression line
        of a set of units by creating a figure and
        calling the function to fill the subplot.
 
        :param df: The outages dataframe
        :param source: The data source
        :param company: The operating company
        :param production_source: The energy production source
        :param unit_name: The name of the production asset
        :param figsize: Desired size of the figure
        :param folder_out: The folder where the figure is saved
        :param close: Boolean to close the figure after it is saved
        :type df: pd.DataFrame
        :type source: string
        :type company: string
        :type production_source: string
        :type unit_name: string
        :type figsize: (int,int)
        :type folder_out: string
        :type close: bool
        :return: None
        :rtype: None
    """                                         
    
    ### Interactive mode
    if close:
        plt.ioff()
    else:
        plt.ion()
            
    ### Figure
    fig, ax = plt.subplots(figsize = figsize)   

    ### Subplots
    subplot.regression_delays(ax,
                              df,
                              )

    ### Labels
    ax.set_xlabel('initial outage length (hours)')
    ax.set_ylabel('final outage length (hours)')
    
    ### Add legend
    lns01, labs01 = ax.get_legend_handles_labels()
    by_label0 = dict(zip(labs01, lns01))
    ax.legend(by_label0.values(),
              by_label0.keys(),
              loc = 0,
              )
    
    ### Finalize 
    title = ' - '.join(filter(None, [
                                     'source_outages = {source_outages}' if source else '',
                                     'company = {company}' if company else '',
                                     'production_source = {production_source}' if production_source else '',
                                     'unit_name = {unit_name}' if unit_name else '',
                                     ])).format(source_outages = source,
                                                company        = company,
                                                production_source = production_source,
                                                unit_name      = unit_name,
                                                )
    fig.suptitle(global_tools.format_latex(title))
    plt.tight_layout(rect = [0, 0.01, 1, 0.95])
    
    full_path = os.path.join(folder_out,
                             "outages_regression_delays",
                             title,
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

