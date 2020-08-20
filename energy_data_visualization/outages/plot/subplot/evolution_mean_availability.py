

#
from .... import global_tools, global_var
#


###############################################################################

def evolution_mean_availability(ax,
                                df_power_tot,
                                unit  = None,
                                color = None,
                                step  = False,
                                ):
    X, Y = global_tools.piecewise_constant_interpolators(df_power_tot.index, 
                                                         df_power_tot.values,
                                                         )
    if   unit == 'GW':
        Y /= 1e3
    elif unit == 'MW':
        Y = Y
    else:
        raise ValueError

    if step:
        ax.step(X,
                Y,
                where = 'post',
                label = 'mean unavailable power ({0})'.format(unit),
                color = (global_var.colors[9]
                         if color is None
                         else
                         color
                         ),
                )
    else:
        ax.plot(X,
                Y,
                label = 'mean unavailable power ({0})'.format(unit),
                color = (global_var.colors[9]
                         if color is None
                         else
                         color
                         ),
                )

 



