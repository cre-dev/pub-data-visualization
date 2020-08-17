

#
import global_tools
import global_var
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

    for col in dg.columns:
        ax.plot(
                dg.index.get_level_values(global_var.contract_delivery_begin_dt_UTC),
                dg[col],
                label = global_tools.format_latex(col),
                **kwargs,
                )
