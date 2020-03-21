class Country():
    '''An I:R country.
    
        tag(string): the tag of the country. Is a three character string
        composed of (and starting by one) higher case alphabetical letters and
        numbers.
        
        capital(int): the id of the capital territory of the country.
        color(Color): the color of the country #New
        cores(list of int): the id of the territories with which the country
        starts the game with.
        culture(string)
        gender_equality(boolean)
        government(string)
        is_antagonist(boolean)
        name(string)
        religion(string)
        
        centralization(int): only needed if tribe. Comprised between -100 and 100.
    '''

    def __init__(self, tag):
        '''Init method of a Country object
        
        Args:
            tag(string): tag.
        '''
        self.__tag = tag
        self.__capital = None
        self.__cores = None
        self.__culture = None
        self.__government = None
        self.__name = None
        self.__religion = None
        
        self.__centralization = None
        self.__is_antagonist = None
    
    @property
    def tag(self):
        return self.__tag
    
    @property
    def capital(self):
        return self.__capital

    @capital.setter
    def capital(self, ncap):
        if type(ncap) != int:
            raise TypeError("capital attribute must be an integer.")
        self.__capital = ncap
    
    @property
    def cores(self):
        return self.__cores
    
    @cores.setter
    def cores(self, ncores):
        if type(ncores) != list:
            raise TypeError("cores attribute must be a list of integers.")
        for core in ncores:
            if type(core) != int:
                raise TypeError("The list assigned to the cores attribute "\
                                "may not contain anything else than integers.")
        self.__cores = ncores
    
    @property
    def culture(self):
        return self.__culture
    
    @culture.setter
    def culture(self, ncul):
        if type(ncul) != str:
            raise TypeError("The culture attribute must be a string")
        self.__culture = ncul
    
    @property
    def government(self):
        return self.__culture
    
    @government.setter
    def government(self, ngov):
        if type(ngov) != str:
            raise TypeError("The government attribute must be a string")
        self.__government = ngov
    
    @property
    def is_antagonist(self):
        return self.__is_antagonist
    
    @is_antagonist.setter
    def is_antagonist(self, n):
        if type(n) == bool:
            self.__is_antagonist = n
        else:
            raise TypeError("The is_antagonist attribute must be a boolean")
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, n):
        if type(n) != str:
            raise TypeError("The name attribute must be a string")
        self.__name = n

    @property
    def religion(self):
        return self.__religion
    
    @religion.setter
    def religion(self, nrel):
        if type(nrel) != str:
            raise TypeError("The religion attribute must be a string")
        self.__religion = nrel

    @property
    def centralization(self):
        return self.centralization
    
    @centralization.setter
    def centralization(self, ncen):
        # Making sure the new centralization value is valid
        if type(ncen) != int:
            raise TypeError("The centralization attribute must be an integer")
        if ncen < -100:
            ncen = -100
        elif ncen > 100:
            ncen = 100

    def from_csv(self, country_df, ter_df):
        """Modifies self according to the data in country_df.
        
        Country_df contains all the data needed to update self apart from the
        data concerning the cores. This one is located in the ter_df file.
        It is good to note that, in ter_df each countries are referred to by
        their id (an integer) and not by their tag (a three character string).
        The id of a certain country can be obtained when we only know its tag by
        using the country_df file.
        
        Args:
            country_df(DataFrame): a DataFrame containing the country related
            data from a save file. Its labels must be country tags and contain
            self.tag.
            ter_df(DataFrame): a DataFrame containing the territory related
            information from a save file.
        """
        country_data = country_df.loc[self.tag]
        # The index is the integer given by the save to each country. It is used
        # as an index in the territory DataFrame made by the parser module.
        index = int(country_data["Unnamed: 0"])
        self.capital = int(country_data["capital"])
        # Getting the territories owned by the country
        raw_cores = ter_df.at[index, ]
    
    def __str__(self):
        """Returns a string of self in the setup.txt file format"""
        pass


def convert_country_df(country_df, ter_df):
    """Returns a dictionary with the countries from country_df sorted by tag.
    
    Args:
        country_df(DataFrame): a DataFrame obtained by reading the csv file
        generated by the create_diplomacy_data_file function from the Parser
        module and using the tag column to sort it.
        ter_df(DataFrame): a DataFrame obtained by reading the csv file
        generated by the create_territory_data_file function from the Parser
        module and using the tag column to sort it.
    
    Returns:
        Dictionary: for each entry of the dictionary, the key is the tag of the
        Country object associated with it (tag : Country).
    """
    pass