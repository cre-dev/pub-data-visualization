
#
from .... import global_var


def power(ax,
          df,
          map_code    = None,
          load_nature = None,
          **kwargs,
          ):
    
    dg = df.xs((map_code,
                load_nature,
                ),
               level = (global_var.geography_map_code,
                        global_var.load_nature,
                        ),
               axis  = 1,
               )
               
    dg = dg.dropna()
    ax.plot(dg.index,
            dg,
            **kwargs,
            )
