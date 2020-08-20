

#
from .... import global_tools


def curve(ax,
          df,
          physical_quantity = None,
          **kwargs,
          ):
    
    dg = df[physical_quantity]
    assert not dg.empty
    
    ax.plot(dg.index,
            dg,
            label = global_tools.format_latex(dg.name),
            **kwargs,
            )



    
    