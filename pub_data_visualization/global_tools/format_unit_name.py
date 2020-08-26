



def format_unit_name(unit):
    """
        Formats the name of a production unit 
        so that different date sources coincide.
 
        :param unit: The name of the unit
        :type unit: string
        :return: The formatted name of the unit
        :rtype: string
    """
        
    ans = (unit.title()
               .replace("'", ' ')
               .replace('-', ' ')
               .replace('(Le) ','')
               .replace('(L ) ','')
               .replace('(La) ', '')
               .replace(' B ', '')
               .replace(' ( Sur Seine)', '')
               .replace('St Maurice ', '')
               .replace('Des Eaux', '')
               .replace('Spem Ccg', 'Spem')
               .replace('Combigolfe Ccg', 'Combigolfe')
               .replace('Provence 4 Biomasse', 'Provence 4')
               .replace('Lucy 3', 'Lucy')
               .replace('Porcheville', 'Porcheville ')
               .replace('Chooz', 'Chooz ')
               .replace('Chinon', 'Chinon ')
               .upper()
               .lstrip()
               .replace('  ', ' ')
               )
    return ans

                