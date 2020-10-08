
import pandas as pd
from pytz.exceptions import NonExistentTimeError


def dt_exists_in_tz(x, tz):
    """
        Tests the existence of a timestamp in a given timezone.
 
        :param x: The time to test
        :param tz: The local timezone
        :type x: pd.Timestamp
        :type tz: pytz.tzfile
        :return: True if the timestamp exists in the timezone
        :rtype: bool
    """        
    assert (   type(x) == pd.Timestamp
            or x is pd.NaT
            )
    try:
        x.tz_localize(tz, ambiguous = True)
        return True
    except NonExistentTimeError:
        return False