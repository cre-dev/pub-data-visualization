
#from .... import global_var
import pandas as pd


def entsog_nominations(date_min=pd.Timestamp.now() - pd.Timedelta(days=2),
                       date_max=pd.Timestamp.now() + pd.Timedelta(days=2),
                       indicator="Nomination",
                       periodType="day",
                       pointDirection="FR-TSO-0003ITP-00526exit",
                       operatorLabel = 'TERÉGA',
                       timeZone='CET',
                       limit=-1,
                       ):
    """
        Writes the API query to load nominations from ENTSOG API

        :param date_min: The left bound
        :param date_max: The right bound
        :type date_min: pd.Timestamp
        :type date_max: pd.Timestamp
        :return: The API query
        :rtype: string
    """

    query = ("https://transparency.entsog.eu/api/v1/operationaldatas.csv?"
             + "&".join(["indicator={}".format(indicator),
                         "pointDirection={}".format(pointDirection),
                         #"operatorLabel={}".format(operatorLabel),
                         "from={}".format(date_min.strftime('%Y-%m-%d')),
                         "to={}".format(date_max.strftime('%Y-%m-%d')),
                         "periodType={}".format(periodType),
                         "timeZone={}".format(timeZone),
                         "limit={}".format(limit),
                         ])
             ).replace(' ', '%20')

    return query
