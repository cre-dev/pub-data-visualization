
"""
Visualization module for public energy data with Python
=======================================================

See https://github.com/cre-os/energy-data-visualization for a presentation of this project.

All the subpackages have a similar structure : 

TypeOfData/ |
├── __init__.py |
├── load/ |
│  ├── __init__ |
│  ├── load.py |
│  ├── dataSource1/ |
│  ├── dataSource2/ |
│  ├── ... |
├── plot/ |
│  ├── __init__.py |
│  ├── plotFunction1.py |
│  ├── plotFunction2.py |
│  ├── subplot/ |
│  ├── ... |
├── tools/ |
│  ├── __init__.py |
│  ├── tool1.py |
│  ├── tool2.py |
│  ├── ... |

"""


from . import auctions
from . import capacity
from . import global_tools
from . import global_var
from . import load
from . import multiplots
from . import outages
from . import production
from . import weather
