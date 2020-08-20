

#
from .... import global_tools




def expected_program(ax,
                     ds,
                     **kwargs,
                     ):
    X, Y = global_tools.piecewise_constant_interpolators(ds.index,
                                                         ds.values,
                                                         )

            
    # Plot program
    ax.plot(X,
            Y, 
            markevery  = 1,
            markersize = 10,
            ls = '-.',
            **kwargs,
            )

    
