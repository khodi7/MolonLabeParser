import ast


class Modifier(object):
    '''A territory modifier from I:R
    
    Attributes:
        name(string): the name of the modifier.
        permanent(boolean): whether or not the modifier is permanent.
    '''


    def __init__(self, n, p = False):
        '''Init method of a Modifier object.
        
        Args:
            n(int): the name.
            p(boolean): whether or not the modifier is permanent.
        '''
        self.name = n
        self.permanent = p
    

def from_csv(a):
    """Transforms a string into a Modifier.
    
    Args:
        a(string): a string from the modifier column of a DataFrame created
        by the create_territory_data_file function in the Parser module.
        
    Returns:
        Modifier associated with the string. None if there isn't any.
    """
    raw_mods = ast.literal_eval(a)
    nraw_mods = []
    # Removing useless elements,
    for i in range(len(raw_mods)):
        part = raw_mods[i].strip()
        if part not in ["{","}"]\
        and part.split("=")[0] not in ["start_date", "date"]:
            nraw_mods.append(part)
    # Checking if the modifier is relevant for the setup file (it is
    # permanent or a barbarian spawn place).
    if "always=yes" in nraw_mods:
        name = nraw_mods[0].split("=")[1].strip('"')
        return Modifier(name, True)
    elif "barbarian" in nraw_mods[0].split("_"):
        name = nraw_mods[0].split("=")[1].strip('"')
        return Modifier(name)
    return None