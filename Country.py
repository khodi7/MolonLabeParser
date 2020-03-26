import pandas as pd
from Color import Color


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
        self.color = None
        self.__cores = None
        self.__culture = None
        self.__gender_equality = None
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
    def gender_equality(self):
        return self.__gender_equality
    
    @gender_equality.setter
    def gender_equality(self, n):
        if type(n) != bool:
            raise TypeError("The gender_equality attribute must be a boolean")
        self.__gender_equality = n
    
    @property
    def government(self):
        return self.__government
    
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
        try:
            index = int(country_data["Unnamed: 0"])
        # If there are several countries with the same tag,
        # we terminate the function.
        except TypeError:
            return None
            
        raw_cap = country_data["capital"]
        if not pd.isna(raw_cap):
            self.capital = int(raw_cap)
        col = Color()
        col.from_csv(country_data["color"], country_data["color2"])
        self.color = col
        # Getting the territories owned by the country.
        # The following line returns a Series object of the cores id's.
        try:
            raw_cores = ter_df.loc[index]["Unnamed: 0"]
        except KeyError:
            raw_cores = []
        self.cores = []
        try:
            for core in raw_cores:
                self.cores.append(int(core))
        # If there's only one element in raw_cores.
        except TypeError:
            self.cores = [int(raw_cores)]
        # raw_ variables are used when their value can be na.
        raw_cul = country_data["primary_culture"]
        if not pd.isna(raw_cul):
            self.culture = raw_cul
        gen_eq = country_data["gender_equality"]
        if gen_eq == "yes":
            self.gender_equality = True
        elif gen_eq == "no":
            self.gender_equality = False
        raw_gov = country_data["government_key"]
        if not pd.isna(raw_gov):
            self.government = raw_gov
        is_antag = country_data["is_antagonist"]
        if is_antag == "yes":
            self.is_antagonist = True
        elif is_antag == "no":
            self.is_antagonist = False
        self.name = country_data["country_name"]
        raw_rel = country_data["religion"]
        if not pd.isna(raw_rel):
            self.religion = raw_rel
        self.centralization = int(country_data["centralization"])
        
        
    def __str__(self):
        """Returns a string of self in the setup.txt file format"""
        country_string = ""
        changed = False # Value used to know i the brackets contain anything.
        # Checking if the country is valid: if it doesn't have any cores, it
        # musts not have a capital.
        if (self.capital != 0
            and self.cores is not None
            and len(self.cores) == 0):
            return ""
        if self.government is not None:
            country_string += "\tgovernment = {0}\n".format(self.government)
            changed = True
        if self.culture is not None:
            country_string += "\tprimary_culture = {0}\n".format(self.culture)
            changed = True
        if self.religion is not None:
            country_string += "\treligion = {0}\n".format(self.religion)
            changed = True
        if changed:
            country_string += "\n" # Blank line to fit the original patter.
        if self.capital is not None and self.capital != 0:
            country_string += "\tcapital = {0}\n".format(self.capital)
            changed = True
        if changed:
            country_string += "\n"
        # The cores requires some more complex programming because of its shape
        # (I could probably ignore that and write it in one line but it wouldn't
        # look as good so fuck it.
        # No need to write the cores if there isn't any.
        if self.cores is not None and len(self.cores) > 0:
            country_string += "\town_control_core =  {\n"
            country_string += "\t"
            before = ""
            for core in self.cores:
                country_string += "{0}{1}".format(before, core)
                before = " "
            country_string += "\n"
            country_string += "\t}\n"
            changed = True
        # Closing the first bracket and ending the string.
        if changed:
            country_string += "}\n"
            country_string = ("{0} = {1}\n".format(self.tag, "{")
                              + country_string)
        return country_string


def convert_country_df(country_df, ter_df):
    """Returns a dictionary with the countries from country_df sorted by tag.
    
    Args:
        country_df(DataFrame): a DataFrame obtained by reading the csv file
        generated by the create_diplomacy_data_file function from the Parser
        module and using the tag column to sort it.
        ter_df(DataFrame): a DataFrame obtained by reading the csv file
        generated by the create_territory_data_file function from the Parser
        module and using the owner column to sort it.
    
    Returns:
        Dictionary: for each entry of the dictionary, the key is the tag of the
        Country object associated with it (tag : Country).
    """
    to_return = {}
    # We put every country into a dictionnary.
    for tag in country_df.index:
        country = Country(tag)
        country.from_csv(country_df, ter_df)
        to_return[tag] = country
    return to_return


# Test zone.
if __name__ == "__main__":
    country_df = pd.read_csv("diplomacy_data.csv", index_col = "tag")
    ter_df = pd.read_csv("territory_data.csv", index_col = "owner")
    for value in convert_country_df(country_df, ter_df).values():
        print(value)