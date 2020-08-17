

from termcolor import colored
from distutils.spawn import find_executable


size_txt       = 12
latex_preamble = r"""
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{accents}
\usepackage{bm}
"""

#####
# Set matplotlib so that all graphs look alike
#####

verb = False

def set_mpl(mpl,
            plt,
            fontP,
            ):
    try:
        mpl.verbose.level = 'debug-annoying'
    except AttributeError as e:
        if verb:
            print(colored(e, 'red'))
    if find_executable('latex'):
        ### Latex
        plt.rc('text', usetex=True)
        plt.rc('text.latex', preamble = latex_preamble)
        plt.rc('legend',**{'fontsize' : size_txt})
        # Font 
        plt.rc('font', **{'family' : 'serif', 
                          'serif'  : ['Computer Modern'], 
                          'size'   : size_txt
                          })
        fontP.set_size('small')
    else:
        if verb:
            print("latex not found")