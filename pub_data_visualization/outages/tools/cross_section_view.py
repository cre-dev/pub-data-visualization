
import pandas as pd

def cross_section_view(df_program,
                       tolerated_delay = pd.Timedelta(minutes = 0),
                       ):
    """
        Computes the expected production at all times t given 
        the information available at times t + tolerated_delay.
        
        :param df_program: The expected availabilty programs
        :param tolerated_delay: The tolerated delay for publication
        :type df_program: pd.DataFrame
        :type program: pd.Timedelta
        :return: The expected availability given the publications
        :rtype: pd.Series
    """
    
    assert type(tolerated_delay) == pd.Timedelta
    
    publications_dt = df_program.index
    publications_minus_delay_dt = [d - tolerated_delay
                                   for d in publications_dt
                                   ]
        
    new_production_steps = sorted(set(df_program.columns).union(publications_minus_delay_dt))
    new_production_steps = pd.Index(list(filter(lambda x : x >= df_program.columns.min(),
                                                new_production_steps,
                                                )),
                                    name = df_program.columns.name,
                                    )
    index_delays  = pd.Index(tolerated_delay
                             if type(tolerated_delay) == list
                             else
                             ['final']
                             )
    
    viewed_series = pd.DataFrame(data    = 0,
                                 index   = new_production_steps,
                                 columns = index_delays,
                                 )
    
    for timestamp in viewed_series.index:
        if tolerated_delay:
            publi_idx = df_program.index.get_loc(timestamp + tolerated_delay,
                                                 'ffill',
                                                 )
        else:
            publi_idx = -1
        prod_idx  = df_program.columns.get_loc(timestamp,
                                               'ffill',
                                               )
        viewed_series.loc[timestamp] = df_program.iloc[publi_idx,
                                                       prod_idx,
                                                       ] 
            
    return viewed_series

