

import calendar
import numpy as np
#
from .... import global_var
#


def distribution(ax, 
                 df,
                 figsize,
                 nature            = None,
                 source            = None,
                 physical_quantity = None,
                 ):

    data = (df.xs(key   = nature,
                  axis  = 1,
                  level = global_var.weather_nature,
                  )
            .xs(key   = physical_quantity,
                axis  = 1,
                level = global_var.weather_physical_quantity,
                )
            ).mean(axis = 1)
    
    MONTHS = np.unique(data.index.month)
    YEARS  = np.unique(data.index.year)

    df_grouped = data.groupby(by = [data.index.year, data.index.month])
     
    interspace_years = 8   
    slice_order = slice(None, None,  ( 1
                                      if figsize[0] > figsize[1]
                                      else
                                      -1
                                      ))
    
    positions = [
                 (month - data.index.month.min())*interspace_years + (year - data.index.year.min())
                 for year, month in df_grouped.groups.keys()
                 ] [slice_order]
    
    labels    = [
                 calendar.month_abbr[month]
                 if year == YEARS.min()
                 else 
                 ''
                 for year, month in df_grouped.groups.keys()
                 ]
    
    
    widths    = [0.9
                 for key in df_grouped.groups.keys()
                 ]
    
    flierprops = dict(marker          = '.', 
                      markerfacecolor = 'k', 
                      markersize      = 2,
                      linestyle       = 'none', 
                      markeredgecolor = 'k',
                      )
    
    b_plot = ax.boxplot([df_grouped.get_group(e) for e in df_grouped.groups.keys()], 
                        vert         = figsize[0] > figsize[1], 
                        positions    = positions, 
                        labels       = labels, 
                        notch        = True,
                        patch_artist = True,
                        widths       = widths,
                        flierprops   = flierprops,
                        whis         = [1,99],
                        )
    
    
    colors = ['pink',
              'lightblue',
              'lightgreen',
              'yellow',
              'orange',
              ]
    for ii, patch in enumerate(b_plot['boxes']):
        patch.set_facecolor(colors[ii//len(MONTHS)])
        patch.set(linewidth=0.25)
      
    if figsize[0] > figsize[1]: 
        ax.yaxis.grid(True)
        ax.set_xlim(-1, interspace_years*(len(MONTHS)-1) + len(YEARS) + 1)
        ax.set_ylabel(physical_quantity)
    else:
        ax.xaxis.grid(True)
        ax.set_ylim(-1, interspace_years*(len(MONTHS)-1) + len(YEARS) + 1)
        ax.set_xlabel(physical_quantity)
    
    
    _ = ax.legend(
                  [pp for pp in b_plot['boxes'][::len(MONTHS)]],
                  YEARS, 
                  ncol = 1,
                  )