
"""
    Definition of the cascade effect between different maturities.
    
"""

from . import user_defined_names as global_var

h_max = 20

cascade_maturities = [
                      *[global_var.maturity_year.format(nb_years = ii) for ii in range(h_max,-1,-1)],
                      *[global_var.maturity_gas_year.format(nb_years = ii) for ii in range(h_max,-1,-1)],
                      *[global_var.maturity_season.format(nb_seasons = ii) for ii in range(h_max,-1,-1)],
                      *[global_var.maturity_quarter.format(nb_quarters = ii) for ii in range(h_max,-1,-1)],
                      *[global_var.maturity_month.format(nb_months = ii) for ii in range(h_max,-1,-1)],
                      *[global_var.maturity_week.format(nb_weeks = ii) for ii in range(h_max,-1,-1)],
                      *[global_var.maturity_weekend.format(nb_weeks = ii) for ii in range(h_max,-1,-1)],
                      *[global_var.maturity_day.format(nb_days = ii) for ii in range(h_max,-1,-1)],
                      ]
                      
