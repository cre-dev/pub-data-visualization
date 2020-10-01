
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

def evolution_mean_availability(df_power_tot, 
                                contract_name     = None, 
                                nb_hours          = None,
                                date_min          = None,
                                date_max          = None,
                                source            = None, 
                                map_code          = None,
                                company           = None,
                                production_source = None,
                                unit_name         = None,
                                power_unit        = global_var.quantity_unit_gw,
                                step              = False,
                                figsize           = global_var.figsize_horizontal,
                                folder_out        = None, 
                                close             = True, 
                                ):
    """
        Plots the evolution of the expected availability
        of a set of units during the delivery windows of a given contract
        by creating a figure and
        calling the function to fill the subplot.
 
        :param df_power_tot: The expected availability during the delivery
        :param contract_name: The name of the delivery contract
        :param nb_hours: The number of hours of the delivery
        :param date_min: The left bound
        :param date_max: The right bound
        :param source: The data source
        :param map_code: The delivery zone
        :param company: The operating company
        :param production_source: The energy production source
        :param unit_name: The name of the production asset
        :param power_unit: The power unit for the plot (MW or GW)
        :param step: Boolean to interpolate linearly or piecewise constantly
        :param figsize: Desired size of the figure
        :param folder_out: The folder where the figure is saved
        :param close: Boolean to close the figure after it is saved
        :type df_power_tot: pd.Series
        :type contract_name: string
        :type nb_hours: float
        :type date_min: pd.Timestamp
        :type date_max: pd.Timestamp
        :type source: string
        :type map_code: string
        :type company: string
        :type production_source: string
        :type unit_name: string
        :type power_unit: string
        :type step: bool
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
    fig, ax = plt.subplots(figsize = figsize,
                           nrows = 1, 
                           ncols = 1, 
                           )
  
    ### Subplot
    subplot.evolution_mean_availability(ax,
                                        df_power_tot,
                                        unit = power_unit,
                                        step = step,
                                        )

    ### Ticks
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%a %d/%m/%Y %H:%M"))
    fig.autofmt_xdate()
    if date_min and date_max:
        ax.set_xlim(date_min, date_max)
    
    ### labels                
    ax.set_xlabel('Date')
    ax.set_ylabel('Unavailable Power {0}'.format(power_unit))
    
    ### Add legend
    lns01, labs01 = ax.get_legend_handles_labels()
    by_label0 = dict(zip(labs01, lns01))
    ax.legend(by_label0.values(),
              by_label0.keys(),
              loc = 0,
              )
                    
    ### Finalize
    title = ' - '.join(filter(None, [
                                     'source_outages = {source_outages}'       if source            else '',
                                     'map_code = {map_code}'                   if map_code          else '',
                                     'company = {company}'                     if company           else '',
                                     'production_source = {production_source}' if production_source else '',
                                     'unit_name = {unit_name}'                 if unit_name         else '',
                                     'contract_name = {contract_name}'         if contract_name     else '',
                                     ])).format(source_outages    = source,
                                                map_code          = map_code,
                                                company           = company,
                                                production_source = production_source,
                                                unit_name         = unit_name,
                                                contract_name     = contract_name,
                                                )
    fig.suptitle(global_tools.format_latex(title))
    plt.tight_layout(rect = [0, 0.01, 1, 0.95])
    
    # Save
    full_path = os.path.join(folder_out,
                             "outages_evolution_mean_availability", 
                             "period_{begin}_{end}".format(begin = date_min.strftime('%Y%m%d_%H%M'), 
                                                           end   = date_max.strftime('%Y%m%d_%H%M'), 
                                                           ) if date_min and date_max else '',
                             title
                             )
    os.makedirs(os.path.dirname(full_path),
                exist_ok = True, 
                )
    plt.savefig(full_path + ".png",
                format      = "png",
                bbox_inches = "tight",
                )

    if close:
        plt.close()

