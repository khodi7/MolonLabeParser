'''
This objective of this module is to take the DataFrames created by the Parser
module and transform them back into text a save file can read.
'''

def unparse_countries(df):
    """Unparse a country DataFrame
    
    Args:
        df(DataFrame): a DataFrame which columns are the same as the ones
        created by the create_diplomacy_data_file function from the Parser
        module.
    
    Returns:
        String: a string like the one found in the country_database section
        of an I:R save file.
    """
    pass

def unparse_territories(df):
    """Unparse a territory DataFrame
    
    Args:
        df(DataFrame): a DataFrame which columns are the same as the ones
        created by the create_territory_data_file function from the Parser
        module.
    
    Returns:
        String: a string like the one found in the provinces section of an I:R
        save file.
    """
    pass

def unparse_pops(df):
    """Unparse a pop DataFrame
    
    Args:
        df(DataFrame): a DataFrame which columns are the same as the ones
        created by the create_pop_data_file function from the Parser module.
    
    Returns:
        String: a string like the one found in the population section of an I:R
        save file.
    """
    pass

def unparse_IR_DataFrame(df, special_cols, special_args):
    """Opposite of create_IR_DataFrame"""
    pass