class BuildingGroup(object):
    '''A group of a building type from I:R
    
    Attributes:
        amount(int)
        name(string)
    '''


    def __init__(self, a, n):
        '''Init method of a BuidingGroup object.
        
        Args:
            a(int): the amount.
            n(string): the name of the buildings in the group.
        '''
        self.amount = a
        self.name = n
    
    def from_csv(self, a):
        """Transforms a string into a list of BuildingGroup
        
        Note : this function is not able to create BuildingGroup of the
        following building types : foundry, granary, forum, theater,
        tribal settlement and provincial legation.
        
        Args:
            a(string): a string from the building column of a DataFrame created
            by the create_territory_data_file function in the Parser module.
            Such a string looks like this:
            { 2 1 0 0 1 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 }
            
        Returns:
            list of BuildingGroup: a list of the BuildingGroup associated with
            the a string.
        """
        a = a.strip(" {}")
        builds = a.split()
        lst = []
        builds_dic = {0 : "military_building", 1 : "fortress_building",
                      2 : "barracks_building", 3 : None,
                      4 : "commerce_building", 5 : "town_hall_building",
                      6 : "court_building", 7 : "academy_building", 8 : None,
                      9 : "library_building", 10 : None,
                      11 : "workshop_building", 12 : "temple_building",
                      13 : None, 14 : "aqueduct_building",
                      15 : "latifundia_building", 16 : "slave_mine_building",
                      17 : "basic_settlement_infratructure_building", 18 : None,
                      19 : None}
        for i in range(len(builds)):
            amount = int(builds[i])
            if amount > 0:
                name = builds_dic[i]
                if name is not None:
                    build = BuildingGroup(amount, name)
                    lst.append(build)
        return lst

# In game name      .csv string                                 Name in setup file
# training camp     { 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 } military_building
# fortress          { 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 } fortress_building
# barracks          { 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 } barracks_building
# foundry           { 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 } ???
# marketplace       { 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 } commerce_building
# tax office        { 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 } town_hall_building
# law court         { 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 } court_building
# academy           { 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 } academy_building
# granary           { 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 } ???
# library           { 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 } library_building
# forum             { 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 } ???
# mill              { 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 } workshop_building only in Tyre
# temple            { 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 } temple_building
# theater           { 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 } ???
# acqueduct         { 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 } aqueduct_building
# slave estate      { 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 } latifundia_building
# mine              { 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 } slave_mine_building
# farming settl     { 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 } basic_settlement_infratructure_building
# trib settm        { 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 } ???
# province legation { 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 } ???