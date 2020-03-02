class Province(object):
    '''An I:R province.
    
    Attributes:
        BuildingGroup(list of BuildingGroup): buildings objects composing a province.
        minorities(list of PopGroup): pops with a different culture and/or
        religion than the main culture and/or religion of the province.
        modifiers(list of Modifier): modifiers of the province.
    '''


    def __init__(self, build = [], mins = [], mods = []):
        '''Init method of a Province object.
        
        Args:
            build(list of BuildingGroup)
            mins(list of PopGroup)
            mods(list of Modifier)
        '''
        self.__builds = build
        self.__minorities = mins
        self.__modifiers = mods
    
    @property
    def builds(self):
        return self.__builds
    
    @property
    def minorities(self):
        return self.__minorities
    
    @property
    def modifiers(self):
        return self.__modifiers
    
    def __str__(self):
        """Returns a string in the format of a setup.txt file of I:R
        """
        pass

    # TODO : create a Province object with the following attributes:
    # buildings (Buildings),
    # minorities (PopGroup),
    # modifier (Modifier), 