

import itertools
#
from .... import global_tools, global_var



def incremental_programs(ax,
                         df_programs,
                         diff_init = False,
                         smoother  = None,
                         ):
    """
        Draws in a subplot the expected availability programs
        of a set of production assets.
 
        :param ax: The ax to fill
        :param df: The expected availability programs
        :param diff_init: Boolean to plot relative differences
                          with the initial date
        :param smoother: Boolean to draw oblique instead of vertical steps
        :type ax: matplotlib.axes._subplots.AxesSubplot
        :type df: pd.DataFrame
        :type diff_init: bool
        :type smoother: bool
        :return: None
        :rtype: None
    """ 
    
    ### Plot init
    if diff_init:
        df_programs = df_programs - df_programs.iloc[:,[0]].values
        dd = df_programs.columns[0]
        ds_program = df_programs.loc[:,dd]
        X, Y = global_tools.piecewise_constant_interpolators(ds_program.index, 
                                                             ds_program,
                                                             smoother  = smoother,
                                                             )
        ax.plot(X,
                Y, 
                label = global_tools.format_latex('init - {0}'.format(dd.strftime(format = '%Y-%m-%d %H:%M %Z'))),
                color = 'k',
                ls    = ':',
                )
    
    ### Plot programs
    for ii, (dd, ds_program) in itertools.islice(enumerate(df_programs.items()), int(diff_init), None):
        X, Y = global_tools.piecewise_constant_interpolators(ds_program.index, 
                                                             ds_program,
                                                             smoother  = smoother,
                                                             )
        ax.plot(X,
                Y, 
                label = global_tools.format_latex(dd.strftime(format = '%Y-%m-%d %H:%M %Z')),
                color = global_var.colors[ii],
                )
    
    ### Plot nameplate capacity
    if not diff_init:
        ax.plot([df_programs.index.min(), df_programs.index.max()], 
                [df_programs.values.max() for kk in range(2)], 
                ls = ':', 
                linewidth = 0.5,
                color = 'k', 
                label = 'nameplate capacity',
                )    

