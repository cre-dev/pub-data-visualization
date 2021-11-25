
import numpy as np
import pandas as pd
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

def expected_program(df,
                     date_min   = None,
                     date_max   = None,
                     source     = None,
                     map_code   = None,
                     producer   = None,
                     production_source = None,
                     unit_name  = None,
                     figsize    = global_var.figsize_horizontal,
                     folder_out = None,
                     close      = True,
                     ):
    """
        Plots the expected availability program
        of a set of units by creating a figure and
        calling the function to fill the subplot.
 
        :param df: The expected availability program
        :param date_min: The left bound
        :param date_max: The right bound
        :param source: The data source
        :param map_code: The delivery zone
        :param producer: The operating producer
        :param production_source: The energy production source
        :param unit_name: The name of the production asset
        :param figsize: Desired size of the figure
        :param folder_out: The folder where the figure is saved
        :param close: Boolean to close the figure after it is saved
        :type df: pd.Series
        :type date_min: pd.Timestamp
        :type date_max: pd.Timestamp
        :type source: string
        :type map_code: string
        :type producer: string
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
    fig, ax = plt.subplots(figsize = figsize,
                           nrows   = 1, 
                           ncols   = 1, 
                           )
    
    ### Subplots  
    subplot.nameplate_capacity(ax,
                               df,
                               )
    for dd, date_update in enumerate(df.columns):
        subplot.expected_program(ax,
                                 df.loc[:,date_update],
                                 label = global_tools.format_latex(date_update),
                                 )  


    ### Ticks
    ax.xaxis.set_major_formatter(mdates.DateFormatter(global_var.dt_formatter))
    fig.autofmt_xdate()
    if date_min and date_max:
        ax.set_xlim(date_min, date_max)
    
    ### labels                
    ax.set_ylabel(global_tools.format_latex(global_var.production_power_mw))
    
    ### Add legend
    lns01, labs01 = ax.get_legend_handles_labels()
    by_label0 = dict(zip(labs01, lns01))
    ax.legend(by_label0.values(),
              by_label0.keys(),
              loc = 0,
              )
                    
    ### Finalize
    title = global_tools.format_latex((  ('source = {source}'          if source    else '')
                                       + (' - map_code = {map_code}'   if map_code  else '')
                                       + (' - producer = {producer}'   if producer  else '')
                                       + (' - unit_name = {unit_name}' if unit_name else '')
                                       ).format(source            = source,
                                                map_code          = map_code,
                                                producer          = producer,
                                                production_source = production_source,
                                                unit_name         = unit_name,
                                                ))
    fig.suptitle(title)

    # Save
    full_path = os.path.join(folder_out,
                             "outages_expected_program", 
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

