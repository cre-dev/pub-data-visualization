
import numpy as np
import pandas as pd
#
import global_tools
#
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters; register_matplotlib_converters()
from matplotlib.font_manager import FontProperties
global_tools.set_mpl(mpl, plt, FontProperties())
#

plt.ioff()

###############################################################################

def histogram_publications_volume(ax, volume_publications, volumes_weight = True, legend = False, title = None):
    
    if volumes_weight:
        grp_sum = volume_publications.groupby(pd.Grouper(freq='D')).sum()
    else:
        grp_sum = volume_publications.groupby(pd.Grouper(freq='D')).count()
    ax.bar(grp_sum.index,
           grp_sum,
           )

    ax.set_xlabel('Date')
    #ax.set_ylabel('Available capacity (MW)')
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m/%Y %H:%M"))

    if legend:
        ax.legend()
        
    if not title is None:
        _ = ax.set_title(title)
