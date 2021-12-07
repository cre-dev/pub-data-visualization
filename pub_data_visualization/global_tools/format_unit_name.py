


def format_unit_name(unit):
    """
        Formats the name of a production unit 
        so that different date sources coincide.
 
        :param unit: The name of the unit
        :type unit: string
        :return: The formatted name of the unit
        :rtype: string
    """

    name = unit.upper() # UPPER CASES
    name = name.lstrip() # Remove left blank spaces
    name = name.rstrip() # Remove right blank spaces
    name = ' '.join(name.split()) # Remove multiple blank spaces
    name = name.replace("'", ' ')
    name = name.replace('-', ' ')
    name = name.replace('_', ' ')

    for key, value in dikt.items():
        name = name.replace(key, value)

    return name


dikt = {

    # Country
    # locally_used_name   : standardized_name,

    # FR
    "AIGLE (L )"          : "AIGLE",
    "AMFARD14"            : "AMFARD 14",
    "AMFARD15"            : "AMFARD 15",
    "BAYET MORANT 1"      : "BAYET",
    "BLAYAIS (LE)"        : "BLAYAIS",
    "BUGEY (LE)"          : "BUGEY",
    "CHASTANG (LE)"       : "CHASTANG",
    "CHEYLAS (LE)"        : "CHEYLAS",
    "CHINON B"            : "CHINON",
    "CHOOZ B"             : "CHOOZ",
    "COMBIGOLFE CCG"      : "COMBIGOLFE",
    "CYCOFOS PL"          : "CYCOFOS ",
    "DAMPIERRE EN BURLY"  : "DAMPIERRE",
    "FR GA MORANT1"       : "BAYET",
    "FR CPCU COGEVITRY"   : "COGEVITRY",
    "FR CPCU SAINT OUEN"  : "ST OUEN",
    "FR LA STPIERRE G"    : "ST PIERRE",
    "FR MAREGES"          : "MAREGES",
    "FR SAINT PIERRE"     : "ST PIERRE",
    "HAVRE (LE)"          : "HAVRE",
    "LUCY 3"              : "LUCY",
    "MARTIGUES PONTEAU"   : "MARTIGUES",
    "MAXE (LA)"           : "MAXE",
    "NOGENT SUR SEINE"    : "NOGENT",
    "PORCHEVILLE B"       : "PORCHEVILLE",
    "POUGET (LE)"         : "POUGET",
    "PROVENCE 4 BIOMASSE" : "PROVENCE 4",
    "SPEM CCG"            : "SPEM",
    "SAINT CHAMAS"        : "ST CHAMAS",
    "SAINT ESTEVE"        : "ST ESTEVE",
    "SAINT GUILLERME"     : "ST GUILLERME",
    "SAINT PIERRE"        : "ST PIERRE",
    "SAINT PIERRE COGNET" : "ST PIERRE",
    "SAINTE CROIX"        : "STE CROIX",
    "SPEM POINTE TG"      : "SPEM POINTE",
    "ST ALBAN ST MAURICE" : "ST ALBAN",
    "ST LAURENT DES EAUX" : "ST LAURENT",
    "ST LAURENT B"        : "ST LAURENT",
    "TRICASTIN (LE)"      : "TRICASTIN",
    "VITRY ( SUR SEINE)"  : "VITRY",

}
                