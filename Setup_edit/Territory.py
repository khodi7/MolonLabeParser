import BuildingGroup as bg
import Modifier as mod
import PopGroup as pg
import pandas as pd


class Territory:
    '''An I:R territory.
    
    Attributes:
        BuildingGroup(list of BuildingGroup): buildings objects composing a
        territory.
        minorities(list of PopGroup): pops with a different culture and/or
        religion than the main culture and/or religion of the territory.
        modifiers(list of Modifier): modifiers of the province.
    '''


    def __init__(self, prov_id, build = [], mins = [], mods = None):
        '''Init method of a Territory object.
        
        Args:
            build(list of BuildingGroup)
            prov_id(the id of the territory)
            mins(list of PopGroup)
            mods(list of Modifier)
        '''
        self.__builds = build
        self.__prov_id = prov_id
        self.__minorities = mins
        self.__modifiers = mods
    
    @property
    def builds(self):
        return self.__builds
    
    @property
    def prov_id(self):
        return self.__prov_id
    
    @property
    def minorities(self):
        return self.__minorities
    
    @property
    def modifiers(self):
        return self.__modifiers
    
    def __str__(self):
        """Returns a string in the format of a setup.txt file of I:R.
        """
        lines = ["{0} = {1}".format(self.prov_id, "{")]
        for build in self.builds:
            line = "\t{0} = {1}".format(build.name, build.amount)
            lines.append(line)
        if self.modifiers is not None:
            if self.modifiers.permanent:
                n = "  always = yes"
            else:
                n = ""
            line = "\tmodifier = {0} modifier = {1}{2} {3}".format("{", self.modifiers.name, n, "}")
            lines.append(line)
        for pop in self.minorities:
            lines.append("\t{0} = {1}".format(pop.type, "{"))
            lines.append("\t\tculture = {0}".format(pop.culture))
            lines.append("\t\treligion = {0}".format(pop.religion))
            lines.append("\t}")
        lines.append("}")
        to_return = ""
        for line in lines:
            to_return += "{0}\n".format(line)
        return to_return
            
    def is_empty(self):
        """Returns whether or not the territory is empty
        
        Returns:
            Boolean: True if the territory contains neither buildings,
            nor minorities, nor modifiers.
        """
        return (self.builds == []
                and self.minorities == []
                and self.modifiers == None)
    
    def reset(self, label):
        self.__builds = []
        self.__prov_id = label
        self.__minorities = []
        self.__modifiers = None
    
    def from_csv(self, ser, pop_df):
        """Modifies self according to ser.
        
        Args:
            pop_df(DataFrame): pop data.
            ser(Series): a Series from a territory DataFrame from
            the Parser module.
            self(Territory): a new Territory object.
        
        Returns:
            None
        """
        builds = ser["buildings"]
        if not pd.isna(builds):
            self.__builds = bg.from_csv(ser["buildings"])
        mods = ser["modifier"]
        if not pd.isna(mods):
            self.__modifiers = mod.from_csv(ser["modifier"])
        pops = ser["pop"]
        if not pd.isna(pops):
            raw_pops = pg.from_csv(ser["pop"], pop_df)
            main_culture = ser["culture"]
            main_religion = ser["religion"]
            for pop in raw_pops:
                if pop.culture != main_culture and pop.religion != main_religion:
                    self.__minorities.append(pop)

    # TODO : create a Province object with the following attributes:
    # buildings (Buildings),
    # minorities (PopGroup),
    # modifier (Modifier), 