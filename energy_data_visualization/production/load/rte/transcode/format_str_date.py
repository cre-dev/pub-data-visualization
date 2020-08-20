
import re
import datetime as dt
import pandas as pd
#
from ..... import global_tools


def format_str_date(str_dates):
    # Parse
    dt_match = re.compile(r"^(\d{2})/(\d{2})/(\d{4}) (\d{2}):(\d{2})-(\d{2}):(\d{2})$").match(str_dates)
    assert dt_match, str_dates
    dt_begin = dt.datetime(year   = int(dt_match.group(3)),
                           month  = int(dt_match.group(2)),
                           day    = int(dt_match.group(1)),
                           hour   = int(dt_match.group(4)),
                           minute = int(dt_match.group(5)),
                           )
    # Check
    assert (int(dt_match.group(6)) - int(dt_match.group(4))) % 24 == 1
    assert int(dt_match.group(5)) == 0
    assert int(dt_match.group(7)) == 0
    dt_begin = pd.Timestamp(dt_begin)
    # Format
    if global_tools.dt_exists_in_tz(dt_begin, 'CET'):
        dt_begin = pd.to_datetime(dt_begin).tz_localize('CET', ambiguous = True)
        dt_begin = dt_begin.tz_convert('UTC')
        return dt_begin
    else:
        return None
