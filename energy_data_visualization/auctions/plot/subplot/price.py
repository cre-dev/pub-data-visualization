

#
from .... import global_tools, global_var
#
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters; register_matplotlib_converters()
from matplotlib.font_manager import FontProperties
global_tools.set_mpl(mpl, plt, FontProperties())
#


def price(ax,
          dg,
          **kwargs,
          ):
    """
        Draws in a subplot the auction prices.
 
        :param ax: The ax to fill
        :param dg: The auction prices
        :param kwargs: additional parameter for the plt.plot function
        :type ax: matplotlib.axes._subplots.AxesSubplot
        :type dg: pd.DataFrame
        :type kwargs: dict
        :return: None
        :rtype: None
    """  

    for col in dg.columns:
        ax.plot(
                dg.index.get_level_values(global_var.contract_delivery_begin_dt_UTC),
                dg[col],
                label = global_tools.format_latex(col),
                **kwargs,
                )
