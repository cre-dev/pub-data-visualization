
import pandas as pd
from pytz.exceptions import NonExistentTimeError


def dt_exists_in_tz(x, tz):
    assert (   type(x) == pd.Timestamp
            or x is pd.NaT
            )
    try:
        x.tz_localize(tz, ambiguous = True)
        return True
    except NonExistentTimeError:
        return False