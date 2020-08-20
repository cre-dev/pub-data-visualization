
import os
#
from .. import global_tools, global_var
from ..weather.plot    import subplot as weather_subplot
from ..load.plot       import subplot as load_subplot
from ..auctions.plot   import subplot as auctions_subplot
from ..production.plot import subplot as prod_subplot
from ..outages.plot    import subplot as outages_subplot
#
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters; register_matplotlib_converters()
from matplotlib.font_manager import FontProperties
global_tools.set_mpl(mpl, plt, FontProperties())
#

def spot_report(dg_weather,
                df_production,
                dg_load,
                df_extrapolated_programs_mw,
                dg_auctions,
                map_code   = None,
                date_min   = None,
                date_max   = None,
                diff_init  = False,
                smoother   = 'basic',
                figsize    = global_var.figsize_horizontal,
                folder_out = None, 
                close      = True,
                ):

    ### Interactive mode
    if close:
        plt.ioff()
    else:
        plt.ion()

    ### Figure
    fig, ax = plt.subplots(figsize     = figsize,
                           nrows       = 5, 
                           ncols       = 1,
                           sharex      = True,
                           gridspec_kw = {'hspace' : 0.15},
                           )
    
    ### Subplot 0
    load_subplot.power(ax[0],
                       dg_load,
                       map_code    = map_code,
                       load_nature = global_var.load_nature_observation_gw,
                       label       = global_tools.format_latex(global_var.load_nature_observation_gw),
                       color       = 'tab:purple',
                       )
    prod_subplot.power(ax[0],
                       df_production,
                       map_code          = map_code,
                       production_nature = global_var.production_nature_observation_gw,
                       label             = global_tools.format_latex(global_var.production_nature_observation_gw),
                       color             = 'tab:pink',
                       )
    ### Subplot 1
    load_subplot.forecasting_error(ax[1],
                                   dg_load,
                                   load_observation_nature = global_var.load_nature_observation_mw,
                                   load_forecast_nature    = global_var.load_nature_forecast_day1_mw,
                                   color = 'b',
                                   linewidth = 0.5,
                                   )
    ### Subplot 2
    outages_subplot.incremental_programs(ax[2],
                                         df_extrapolated_programs_mw/1e3,
                                         diff_init = diff_init,
                                         smoother  = smoother, 
                                         )
    
    ### Subplot 3
    auctions_subplot.price(ax[3],
                           dg_auctions,
                           )
    ### Subplot 4
    weather_subplot.curve(ax[4],
                          dg_weather,
                          physical_quantity = global_var.weather_temperature_celsius,
                          color = 'tab:blue',
                          )
    ax42 = ax[4].twinx()
    weather_subplot.curve(ax42,
                          dg_weather,
                          physical_quantity = global_var.weather_wind_speed,
                          color = 'tab:green',
                          )


    ### Ticks
    ax[3].xaxis.set_major_formatter(mdates.DateFormatter("%a %d/%m/%Y %H:%M"))
    fig.autofmt_xdate()
    if date_min and date_max:
        ax[3].set_xlim(date_min, date_max)
    
    ### labels                
    ax[0].set_ylabel(global_tools.format_latex(global_var.quantity_unit_gw))
    ax[1].set_ylabel(global_tools.format_latex(global_var.load_nature_forecast_day1_error_mw))
    ax[2].set_ylabel(global_tools.format_latex(global_var.outage_expected_availability_gw))
    ax[3].set_ylabel(global_tools.format_latex(global_var.auction_price_euro_mwh))
    ax[4].set_ylabel(global_tools.format_latex(global_var.weather_temperature_celsius))
    ax42 .set_ylabel(global_tools.format_latex(global_var.weather_wind_speed))
    
    ### Add legend
    for aa in [ax[0],
               ax[1],
               ax[2],
               ax[3],
               ]:
        lns, labs = aa.get_legend_handles_labels()
        by_label  = dict(zip(labs,
                             lns,
                             ))
        aa.legend(by_label.values(),
                  by_label.keys(),
                  loc = 0,
                  )

    lns41, labs41 = ax[4].get_legend_handles_labels()
    lns42, labs42 = ax42 .get_legend_handles_labels()
    by_label4 = dict(zip(labs41+labs42,
                         lns41+lns42,
                         ))
    ax[4].legend(by_label4.values(),
                 by_label4.keys(),
                 loc = 0,
                 )
                    
    ### Finalize
    title = 'Spot report'
    fig.suptitle(global_tools.format_latex(title))
    plt.tight_layout(rect = [0, 0.01, 1, 0.95])
    
    # Save
    full_path = os.path.join(folder_out,
                             "multiplots_spot_report",
                             "period_{begin}_{end}".format(begin = date_min.strftime('%Y%m%d_%H%M'), 
                                                           end   = date_max.strftime('%Y%m%d_%H%M'), 
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


