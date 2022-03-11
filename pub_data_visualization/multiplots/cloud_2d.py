
import os
#
from .. import global_tools, global_var
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

def cloud_2d(X,
             Y,
             x_label     = None,
             y_label     = None,
             kernel_plot    = False,
             display_linreg = False,
             plot_name   = None,
             date_min    = None,
             date_max    = None, 
             map_code    = None,
             figsize     = global_var.figsize_horizontal,
             folder_out  = None, 
             close       = True,
             ):
    """
        Plots the expected availability of 
        a given set of production assets 
        and the observed production
        by creating a figure and
        calling the function to fill the subplot.
 
        :param ax: The ax to fill
        :param X: X-coordinates of the points
        :param Y: Y-coordinates of the points
        :param kernel_plot: kernel or scatter plot
        :param plot_name: name for the plot
        :param date_min: The left bound
        :param date_max: The right bound
        :type ax: matplotlib.axes._subplots.AxesSubplot
        :type X: np.array
        :type Y: np.array
        :type kernel_plot: bool
        :type plot_name: str
        :type date_min: pd.Timestamp
        :type date_max: pd.Timestamp
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
    ### Subplots
    
    
        
    
    if kernel_plot:
        subplot.kernel()
    else:
        ax.scatter(X, Y)
        if display_linreg:
            xm = X.mean()
            ym = Y.mean()
            x = X - xm
            y = Y - ym
            a = x.T.dot(y)/x.T.dot(x)
            b = ym - a*xm
            def f(t):
                return a*t + b
            ax.plot([X.min(), X.max()],
                    [f(X.min()), f(X.max())],
                    c = 'k',
                    ls = '--',
                    label = 'f(t) = {0:.2f}.t + {1:.2f}'.format(a, b),
                    )

    ### Labels
    ax.set_xlabel(global_tools.format_latex(x_label))
    ax.set_ylabel(global_tools.format_latex(y_label))

    # Legend
    ax.legend()
                    
    ### Finalize
    title = ' - '.join(filter(None, [
                                     'map_code = {map_code}'if map_code else '',
                                     ])).format(map_code       = map_code,
                                                )
    fig.suptitle(global_tools.format_latex(title))
    
    
    plt.tight_layout(rect = [0, 0.01, 1, 0.95])
    
    # Save
    full_path = os.path.join(folder_out,
                             plot_name,
                             "period_{begin}_{end}".format(begin = date_min.strftime(global_var.dt_formatter_file),
                                                           end   = date_max.strftime(global_var.dt_formatter_file),
                                                           ) if date_min and date_max else '',
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


