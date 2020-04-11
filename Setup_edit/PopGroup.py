import ast
import pandas as pd


class PopGroup(object):
    '''A group of pops from I:R
    
    A PopGroup is a group of pop of the same type, culture and religion.
    
    Attributes:
        amount(int): the amount of pops in the PopGroup.
        culture(string): the culture of the PopGroup.
        religion(string): the religion of the PopGroup
        type(string): the type of the PopGroup (citizen, slaves,...)
        
    '''


    def __init__(self, n, cul, rel, t):
        '''Init method of a PopGroup object.
        
        Args:
            n(int): the amount.
            cul(string): the culture.
            rel(string): the religion
            t(string): the type
        '''
        self.amount = n
        self.culture = cul
        self.religion = rel
        self.type = t
    
    def __eq__(self, other):
        """Returns whether or not other and self are the same PopGroup
        
        note : two PopGroup are considered to be equal if they have the same
        culture, religion and type attributes (the amount doesn't matter)
        
        Args:
            other(PopGroup): the PopGroup we want to check.
        
        Returns:
            Boolean: whether or not self and other have the same culture,
            religion and type attributes.
        """
        return (self.culture == other.culture
                and self.religion == other.religion
                and self.type == other.type)
    

def from_csv(a, pop_df):
    """Transforms a string into a list of PopGroup.
    
    Args:
        a(string): a string from the pop column of a DataFrame created
        by the create_territory_data_file function in the Parser module.
        pop_file(string): name or path to the .csv file containing the data
        of the pops in a.
        pop_df(DataFrame): the pop DataFrame.
        
    Returns:
        list of PopGroup: a list of the BuildingGroup associated with the a
        string.
    """
    pop_list = ast.literal_eval(a)
    lst = []
    for label in pop_list:
        cul = pop_df.at[label, "culture"]
        rel = pop_df.at[label, "religion"]
        typ = pop_df.at[label, "type"]
        pop = PopGroup(1, cul, rel, typ)
        lst.append(pop)
    # Merging duplicates,
    to_return = []
    while len(lst) > 0:
        group = lst[0]
        del lst[0]
        i = 0
        while i < len(lst):
            if lst[i] == group:
                group.amount += 1
                del lst[i]
            else:
                i += 1
        to_return.append(group)
    return to_return
        