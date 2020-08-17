
import itertools
#
import global_var
import global_tools


def incremental_programs(ax,
                        df_programs,
                        diff_init = False,
                        smoother  = None,
                        ):
    
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

