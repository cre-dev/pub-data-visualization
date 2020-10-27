

import os
#
from ... import global_tools, global_var

#
import seaborn as sn
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters; register_matplotlib_converters()
from matplotlib.font_manager import FontProperties
global_tools.set_mpl(mpl, plt, FontProperties())
#
from matplotlib.widgets import Slider

def animated_availability(dh,
                          production_dt_min = None,
                          production_dt_max = None,
                          data_source       = None,
                          map_code          = None,
                          producer          = None,
                          production_source = None,
                          unit_name         = None,
                          figsize           = global_var.figsize_horizontal,
                          folder_out        = None, 
                          close             = True,
                          ):
    """
        Plots the expected availability program at two changeable dates
        by creating a figure and filling the animated subplot.
 
        :param dh: The expected availability at different dates
        :param production_dt_min: The left bound
        :param production_dt_max: The right bound
        :param data_source: The data source
        :param map_code: The delivery zone
        :param producer: The operating company
        :param production_source: The energy production source
        :param unit_name: The name of the production asset
        :param figsize: Desired size of the figure
        :param folder_out: The folder where the figure is saved
        :param close: Boolean to close the figure after it is saved
        :type dh: pd.DataFrame
        :type production_dt_min: pd.Timestamp
        :type production_dt_max: pd.Timestamp
        :type data_source: string
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
    gs_top  = plt.GridSpec(3, 3, hspace=0.7, height_ratios = [1,0.02,0.02], width_ratios = [0.1, 0.8, 0.1], top=0.95)
    gs_base = plt.GridSpec(3, 3, hspace=0.2, height_ratios = [1,0.02,0.02], width_ratios = [0.1, 0.8, 0.1], )
    fig = plt.figure(figsize = figsize)
    ax = [fig.add_subplot(gs_top[0,:]),
          fig.add_subplot(gs_base[1,1]),
          fig.add_subplot(gs_base[2,1]),
          ]
        
    ### Subplot
    l1, = ax[0].step(dh.columns,
                     dh.iloc[0],
                     where = 'post',
                     )
    
    v1, = ax[0].plot([dh.columns.min(), dh.columns.min()],
                     [dh.min().min(), dh.max().max()],
                     c = l1.get_color(),
                     ls = ':',
                     )
    l2, = ax[0].step(dh.columns,
                     dh.iloc[0],
                     where = 'post',
                     )
    
    v2, = ax[0].plot([dh.columns.min(), dh.columns.min()],
                     [dh.min().min(), dh.max().max()],
                     c = l2.get_color(),
                     ls = ':',
                     )
    
    h, = ax[0].plot([dh.columns.min(), dh.columns.max()],
                    [0,0],
                    c = 'k',
                    ls = '-',
                    linewidth = 0.3,
                    )

    ### Ticks
    ax[0].xaxis.set_major_formatter(mdates.DateFormatter("%a %d/%m/%Y %H:%M"))
    _ = plt.setp(ax[0].get_xticklabels(), rotation=30, horizontalalignment='right')
    
    ymin = dh.min().min()
    ymax = dh.max().max()
    ax[0].set_ylim(ymin - 0.1*(ymax - ymin),
                   ymax + 0.1*(ymax - ymin),
                   )

    ### Slider 1
    ax[1].grid(False)
    sdate1  = Slider(ax[1],
                     'ViewPoint',
                     0,
                     dh.shape[0],
                     valinit = 0,
                     )
    def update1(val):
        idx = sdate1.val
        dd  = dh.index[int(idx)]
        l1.set_ydata(dh.iloc[int(idx)])
        v1.set_xdata([dd,dd])
        sdate1.valtext.set_text(dd.strftime(format = "%a %d/%m/%Y %H:%M"))
        fig.canvas.draw_idle()
    sdate1.on_changed(update1)
    ### Slider 2
    ax[2].grid(False)
    sdate2  = Slider(ax[2],
                     'ViewPoint',
                     0,
                     dh.shape[0],
                     valinit = 0,
                     )
    def update2(val):
        idx = sdate2.val
        dd  = dh.index[int(idx)]
        l2.set_ydata(dh.iloc[int(idx)])
        v2.set_xdata([dd,dd])
        sdate2.valtext.set_text(dd.strftime(format = "%a %d/%m/%Y %H:%M"))
        fig.canvas.draw_idle()
    sdate2.on_changed(update2)
    
    ### Add legend
    lns01, labs01 = ax[0].get_legend_handles_labels()
    by_label0 = dict(zip(labs01, lns01))
    if bool(by_label0):
        ax[0].legend(by_label0.values(),
                     by_label0.keys(),
                     loc = 0,
                     )
    
    ### labels                
    ax[0].set_ylabel(global_var.outage_expected_availability_mw)
    
                    
    ### Finalize
    title = ' - '.join(filter(None, [
                                     'data_source = {data_source}'             if data_source       else '',
                                     'map_code = {map_code}'                   if map_code          else '',
                                     'company = {producer}'                    if producer          else '',
                                     'production_source = {production_source}' if production_source else '',
                                     'unit_name = {unit_name}'                 if unit_name         else '',
                                     ])).format(data_source       = data_source,
                                                map_code          = map_code,
                                                producer          = producer,
                                                production_source = production_source,
                                                unit_name         = unit_name,
                                                )
    fig.suptitle(global_tools.format_latex(title))


    # Save
    full_path = os.path.join(folder_out,
                             "outages_animated_availability", 
                             "period_{begin}_{end}".format(begin = production_dt_min.strftime('%Y%m%d_%H%M'), 
                                                           end   = production_dt_max.strftime('%Y%m%d_%H%M'), 
                                                           ) if production_dt_min and production_dt_max else '',
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


