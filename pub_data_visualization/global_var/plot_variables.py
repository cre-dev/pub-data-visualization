
"""
    User defined variables for plotting.
    
"""
from distutils.spawn import find_executable
import matplotlib.cm as cm


if find_executable('latex'):
    dt_formatter    = "%a\ %d/%m/%Y\ %H{:}%M"
    dt_formatter_tz = '%d/%m/%Y\ %H{:}%M %Z'
    date_formatter  = "%a\ %d/%m/%Y"
else:
    dt_formatter    = "%a %d/%m/%Y %H:%M"
    dt_formatter_tz = '%d/%m/%Y %H:%M %Z'
    date_formatter  = "%a %d/%m/%Y"

colors     = cm.tab10.colors
linestyles = ['-', '--', '-.', ':']
markers    = ["o", "^", ">", "<", "v", 'd', 'x']

figsize_horizontal     = (18,10)
figsize_vertical       = (10,18)
figsize_horizontal_ppt = (11.5,6.5)
figsize_vertical_ppt   = (6,10)
figsize_square_ppt     = (10,10)
