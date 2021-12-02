
"""
    Correspondances between the map_code
    used by ENTSO-E and the user defined names.
    
"""

from ..... import global_var

dikt = {'AT': global_var.geography_map_code_austria,
        'BE': global_var.geography_map_code_belgium,
        'BG': global_var.geography_map_code_bulgaria,
        'CH': global_var.geography_map_code_swiss,
        'CZ': global_var.geography_map_code_czech,
        'DK': global_var.geography_map_code_denmark,
        'ES': global_var.geography_map_code_spain,
        'FI': global_var.geography_map_code_finland,
        'FR': global_var.geography_map_code_france,
        'GB': global_var.geography_map_code_great_britain,
        'HU': global_var.geography_map_code_hungary,
        'LT': global_var.geography_map_code_latvia,
        'NL': global_var.geography_map_code_netherlands,
        'PL': global_var.geography_map_code_poland,
        'PT': global_var.geography_map_code_portugal,
        'RO': global_var.geography_map_code_romania,
        'SK': global_var.geography_map_code_slovakia,
        }

def map_code(ss):
    ans = dikt.get(ss, ss)
    return ans


