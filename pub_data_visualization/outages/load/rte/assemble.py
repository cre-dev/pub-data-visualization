
import pandas as pd
import numpy as np
from termcolor import colored
#
from .... import global_var
 

def assemble(df):
    """
        Merges the outages data provided by RTE
        in different files and discards duplicates and anomalies.
 
        :param df: The outages data frame
        :type df: pd.DataFrame
        :return: The corrected outages data frame
        :rtype: pd.DataFrame
    """
    
    ### Drop NaT values
    print('Drop NaT values')
    nan_dates     = df[global_var.outage_end_dt_utc].apply(pd.isnull)
    if bool(nan_dates.sum()):
        print(colored("""Due to NaT in outage_end_dt columns, 
                      {0} publications in years {1} 
                      and concerning years {2} 
                      are dropped""".format(len(nan_dates),
                                            df.loc[nan_dates][global_var.publication_dt_utc].dt.year.unique(),
                                            df.loc[nan_dates][global_var.outage_begin_dt_utc].dt.year.unique(),
                                            ),
                      'red',
                      ))
        df = df.loc[np.logical_not(nan_dates)].copy()
        
    ### Search for incoherences
    print('Search for incoherences')
    dikt_incoherences = {}
    df_check = df[[col
                   for col in df.columns
                   if col not in [global_var.file_name,
                                  global_var.outage_period_begin_dt_utc,
                                  global_var.outage_period_end_dt_utc,
                                  ]
                   ]]
    groups_df_check = df_check.groupby([global_var.publication_id,
                                        global_var.publication_version, 
                                        global_var.publication_dt_utc,
                                        ])
    dikt_groups = {k:v
                   for k, v in groups_df_check.groups.items()
                   if len(v) >= 2
                   }
    for ii, ((publication_id, publication_version, publication_dt), value) in enumerate(dikt_groups.items()):
        print('\r{0:6}/{1:6} - len(dikt_incoherences) = {2}'.format(ii, len(dikt_groups), len(dikt_incoherences)), end = '')
        df_tmp = df_check.loc[value]
        for jj in range(df_tmp.shape[0]):
            col_diff = np.logical_and(df_tmp.iloc[0]  == df_tmp.iloc[0], # To check for NaN
                                      df_tmp.iloc[jj] != df_tmp.iloc[0],
                                      )
            if col_diff.any():
                dikt_incoherences[publication_id, publication_version, publication_dt, jj] = df_tmp.iloc[[0,jj], col_diff.values]
    print()
    
    ### Extract
    print('Extract')
    # Only keep the last publications       
    df = df.groupby([global_var.publication_id,
                     global_var.publication_version, 
                     global_var.publication_dt_utc,
                     ],
                    axis = 0,
                    ).tail(1)
    
    ### Sort rows
    print('Sort rows')
    df = df.sort_values(by = [
                              global_var.publication_creation_dt_utc,
                              global_var.publication_id,
                              global_var.publication_version,
                              global_var.publication_dt_utc,
                              global_var.outage_status,
                              global_var.outage_begin_dt_utc,
                              ], 
                        ascending = [True,
                                     True,
                                     True,
                                     True,
                                     False,
                                     True,
                                     ]
                        )
                            
    ### Checks
    print('Checks')
    assert not pd.isnull(df.index.values).any()        
    assert df[df[global_var.outage_status] == global_var.outage_status_finished].index.is_unique
    
    return df, dikt_incoherences
        