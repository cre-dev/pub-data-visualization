
"""
    Visualization module for public energy data with Python.
    
    See https://github.com/cre-os/energy-data-visualization for a presentation of this project.
    
    All the subpackages have a similar structure : 
    
    | TypeOfData/
    |     __init__.py
    |     load/
    |         __init__.py
    |         dataSource1/
    |         dataSource2/
    |         ...
    |     tools/
    |         __init__.py
    |         tool1.py
    |         tool2.py
    |         ...
    |     plot/
    |         __init__.py
    |         plotFunction1.py
    |         plotFunction2.py
    |         ...
    |         subplot/
    |             subplotFunction1.py
    |             subplotFunction2.py
    |             ...

"""


from . import global_tools
from . import global_var
from . import indices
from . import load
from . import multiplots
from . import outages
from . import production
from . import production_capacity
from . import weather
