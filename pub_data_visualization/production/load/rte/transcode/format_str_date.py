
import re
import datetime as dt
import pandas as pd
#
from ..... import global_tools


def format_str_date(str_dates):
    """
        Parses the dates provided by RTE in the production data frames.

        :param str_dates: The dates with the format chosen by RTE
        :type str_dates: string
        :return: The formatted timestamp
        :rtype: pd.Timestamp
    """

    # Parse
    dt_match = re.compile(r"^(\d{2})/(\d{2})/(\d{4}) (\d{2}):(\d{2})-(\d{2}):(\d{2})$").match(str_dates)
    assert dt_match, str_dates
    dt_begin = dt.datetime(year   = int(dt_match.group(3)),
                           month  = int(dt_match.group(2)),
                           day    = int(dt_match.group(1)),
                           hour   = int(dt_match.group(4)),
                           minute = int(dt_match.group(5)),
                           )
    dt_end = dt.datetime(year   = int(dt_match.group(3)),
                         month  = int(dt_match.group(2)),
                         day    = int(dt_match.group(1)),
                         hour   = int(dt_match.group(6)) % 24,
                         minute = int(dt_match.group(7)),
                         )
    # Check
    assert (int(dt_match.group(6)) - int(dt_match.group(4))) % 24 == 1
    assert int(dt_match.group(5)) == 0
    assert int(dt_match.group(7)) == 0
    dt_begin = pd.Timestamp(dt_begin)
    dt_end   = pd.Timestamp(dt_end)
    dt_mean  = dt_begin + (dt_end - dt_begin)/2
    # Format
    if global_tools.dt_exists_in_tz(dt_begin, 'CET'):
        dt_begin = pd.to_datetime(dt_begin).tz_localize('CET', ambiguous = True)
        dt_begin = dt_begin.tz_convert('UTC')
        return dt_begin
    else:
        return None
