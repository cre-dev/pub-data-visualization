

import os
#
from ... import global_tools, global_var
from . import subplot
#
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters; register_matplotlib_converters()
from matplotlib.font_manager import FontProperties
global_tools.set_mpl(mpl, plt, FontProperties())
#


def distribution(df,
                 nature            = None,
                 source            = None,
                 physical_quantity = None,
                 folder_out        = None,
                 close             = True,
                 figsize           = global_var.figsize_vertical,
                 ):
    """
        Plots the boxplots of the weather data by creating a figure and
        calling the function to fill the subplot.
 
        :param df: The weather data
        :param nature: The nature of the weather data to plot
        :param source: The source of the weather data to plot
        :param physical_quantity: The weather quantity to plot
        :param folder_out: The folder where the figure is saved
        :param close: Boolean to close the figure after it is saved
        :param figsize: Desired size of the figure
        :type df: pd.DataFrame
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
    subplot.distribution(ax, 
                         df,
                         figsize,
                         nature            = nature,
                         source            = source,
                         physical_quantity = physical_quantity,
                         )
    
    ### Finalize
    title = ' - '.join(filter(None, [
                                     'source = {source}' if source else '',
                                     'nature = {nature}' if nature else '',
                                     'physical_quantity = {physical_quantity}' if physical_quantity else '',
                                     ])).format(source            = source,
                                                nature            = nature,
                                                physical_quantity = physical_quantity,
                                                )    
    fig.suptitle(global_tools.format_latex(title))
    
    ### Save
    full_path = os.path.join(folder_out, 
                             "weather_distribution", 
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

    
