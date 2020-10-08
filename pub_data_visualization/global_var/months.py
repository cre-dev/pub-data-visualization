
"""
    Correspondances between dates and written months.

    Correspondances between the months written in different sources
    and their indices (from 1 to 12).
    
"""

import calendar

month_str_int = {**{month.upper() : ii 
                    for ii, month in list(enumerate(calendar.month_abbr))[1:]
                    },
                 'JANV'  : 1,
                 'FÉVR'  : 2,
                 'MARS'  : 3,
                 'AVR'   : 4,
                 'MAI'   : 5,
                 'JUNE'  : 6,
                 'JUIN'  : 6,
                 'JULY'  : 7,
                 'JUIL'  : 7,
                 'AOÛT'  : 8,
                 'SEPT'  : 9,
                 'DÉC'   : 12,
                 }