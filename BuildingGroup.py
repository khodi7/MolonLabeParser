from pandas._libs.algos import groupsort_indexer
class BuildingGroup(object):
    '''A group of a building type from I:R
    
    Attributes:
        amount(int)
        name(string)
    '''


    def __init__(self, a, n):
        '''Init method of a BuidingGroup object.
        
        Args:
            a(int): the amount
            n(string): the name of the buildings in the group
        '''
        pass
    
    def from_csv(self, a):
        """Transforms a string into a list of building groups
        
        Args:
            a(string): a string from the building column of a DataFrame created
            by the create_territory_data_file function in the Parser module.
            
        Returns:
            list of BuildingGroup: a list of the BuildingGroup associated with
            the a string.