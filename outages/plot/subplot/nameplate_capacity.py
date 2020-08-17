

#



def nameplate_capacity(ax,
                       df,
                       ):   

    ax.plot([df.index.min(), df.index.max()], 
            [df.values.max() for kk in range(2)], 
            ls = ':', 
            linewidth = 0.5,
            color     = 'k', 
            label     = 'nameplate capacity',
            )
