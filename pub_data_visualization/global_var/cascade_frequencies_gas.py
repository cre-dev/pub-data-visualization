"""
    Definition of the cascade effect between different WEPs.

"""

from . import user_defined_names as global_var

cascade_frequencies_gas = [
    global_var.contract_frequency_gas_year,
    global_var.contract_frequency_season,
    global_var.contract_frequency_quarter,
    global_var.contract_frequency_month,
    global_var.contract_frequency_week,
    global_var.contract_frequency_day,
    global_var.contract_frequency_within_day,
]
