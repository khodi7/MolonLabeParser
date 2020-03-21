class Color:
    """A color defined in RGB
    
    Attributes:
        red(int)
        green(int)
        blue(int)
    """
    
    def __init__(self):
        self.red = None
        self.green = None
        self.blue = None
    
    def from_csv(self, csv_string):
        """Modifies self according to csv_string.
        
        Args:
            csv_string: a string from the color column of a csv file generated
            by the create_diplomacy_data_file function in the parser module.
            It has the following format: rgb { R G B }
            R G and B are the values for the intensity of respectively, the red,
            the green and the blue in the color.
            0 <= R, G or B <= 255
        
        Returns:
            None
        """
        pass
    
    def __str__(self):
        pass