"""

Todo:
    * Create a province class
"""
import pandas as pd
import ast
from Parser import index_finder, closing_brackets


def province_setup_edit(pop_file = "pop_data.csv", ter_file = "territory_data.csv"):
    """Modifies the province_setup.csv file
    
    Requires the province_setup.csv file to be in the same directory as the one
    in which this function is executed.
    This file will be modified according to the data contained in pop_file and
    ter_file.
    
    Args:
        pop_file(string): the name or path of the file containing the population
        related data extracted from an I:R save.
        ter_file(string): the name or path of the file containing the territory 
        related data extracted from an I:R save.
    
    Returns:
        None
    """
    ter_df = pd.read_csv(ter_file, index_col = "Unnamed: 0")
    pop_df = pd.read_csv(pop_file, index_col = "Unnamed: 0")
    setup_df = pd.read_csv("province_setup.csv", index_col = "#ProvID")
    dic = {" Culture" : "culture", " Religion" : "religion",
           " TradeGoods" : "trade_goods", " Citizen" : "pop",
           " Freedmen" : "pop", " Slaves" : "pop", " Tribesmen" : "pop",
           " Civilization" : "civilization_value",
           "City Status" : "province_rank"}
    for label in setup_df.index:
        for key in dic:
            if dic[key] == "pop":
                pops = {" Citizens" : 0, " Freedmen" : 0, " Slaves" : 0,
                        " Tribesmen" : 0}
                converter = {"citizen" : " Citizens", "freemen" : " Freedmen",
                            "slaves" : " Slaves", "tribesmen" : " Tribesmen"}
                print(label)    # 652
                try:
                    lst = ast.literal_eval(ter_df.at[label, "pop"])
                except ValueError:
                    if not pd.isna(ter_df.at[label, "pop"]):
                        raise ValueError
                    lst = []
                    for pop_id in lst:
                        ptype = pop_df.at[pop_id, "type"]
                        ptype = converter[ptype]
                        pops[ptype] += 1
                        for nkey in pops:
                            setup_df.at[label, nkey]
                
            elif dic[key] == "province_rank":
                if ter_df.at[label, dic[key]] != "settlement":
                    setup_df.at[label, key] = ter_df.at[label, dic[key]]
            else:
                try:
                    setup_df.at[label, key] = ter_df.at[label, dic[key]]
                except ValueError:
                    if not pd.isna(ter_df.at[label, dic[key]]):
                        raise ValueError
    setup_df.to_csv("province_setup_test.csv")
    with open("province_setup_test.csv") as file:
        content = file.readlines()
    content[0] = content[0][:len(content[0]) - 12] + "\n"
    with open("province_setup_test.csv", "w") as file:
        file.writelines(content)


def edit_provinces(pop_file, ter_file, original_file):
    """Modifies original_file according to other files
    
    Args:
        pop_file(string): the name or path of the file containing the population
        related data extracted from an I:R save.
        ter_file(string): the name or path of the file containing the
        territory related data extracted from an I:R save.
        original_file(string):the name or path of the file to be modified.
    
    Returns:
        None
    """
    with open(original_file):
        content = original_file.readlines()
    first_line = "provinces = { #Any entry must contain a comment with city "\
                 "name.\n"
    # Deleting the old content,
    start_index = index_finder(content, first_line)
    end_index = closing_brackets(content, start_index)
    del content[start_index : end_index + 1]