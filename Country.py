class Country():
    '''An I:R country.
    
        tag(string): the tag of the country. Is a three character string
        composed of (and starting by one) higher case alphabetical letters and
        numbers.
        
        capital(int): the id of the capital territory of the country.
        cores(list of int): the id of the territories with which the country
        starts the game with.
        culture(string)
        government(string)
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
        pass
    
    @centralization.setter
    def centralization(self, ncen):
        # Making sure the new centralization value is valid
        if type(ncen) != int:
            raise TypeError("The centralization attribute must be an integer")
        if ncen < -100:
            ncen = -100
        elif ncen > 100:
            ncen = 100

    def from_csv(self, country_df):
        """Modifies self according to the data in country_df.
        
        Args:
            country_df(DataFrame): a DataFrame containing the country related
            data from a save file. Its labels must be country tags and contain
            self.tag.
        """
        country_data = country_df.loc[self.tag]
        self.capital = int(country_data["capital"])
        