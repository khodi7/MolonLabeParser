"""

Todo:
    * Create a province class
"""
import pandas as pd
import ast
from Parser import index_finder, closing_brackets
from Territory import Territory


def province_setup_edit(pop_file = "pop_data.csv",
                        ter_file = "territory_data.csv"):
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
                    setup_df.at[label, nkey] = pops[nkey]
                
            elif dic[key] == "province_rank":
                if ter_df.at[label, "province_rank"] != "settlement":
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
    # Remove the unwanted column.
    content[0] = content[0][:len(content[0]) - 12] + "\n"
    with open("province_setup_test.csv", "w") as file:
        file.writelines(content)


def edit_territories(original_file, pop_file = "pop_data.csv",
                     ter_file = "territory_data.csv", progress = False):
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
    with open(original_file) as file:
        content = file.readlines()
    ter_df = pd.read_csv(ter_file, index_col = "Unnamed: 0")
    first_line = "provinces = { #Any entry must contain a comment with city "\
                 "name.\n"
    ncontent = [first_line]
    # Creating a file in which the new content will be stocked before being
    # added to the main file,
    # This is done to avoid using to much ram.
    temp_content = "temp.txt"
    with open(temp_content, "w") as file:
        file.writelines([""])
    # Adding the needed territories to the new content,
    pop_df = pd.read_csv(pop_file, index_col = "Unnamed: 0")
    ter = Territory(0)
    for label in ter_df.index:
        if progress == True:
            print(label)
        ter.reset(label)
        ter.from_csv(ter_df.loc[label], pop_df)
        if not ter.is_empty():
            ind_ter = indent(str(ter))
            ncontent.append(ind_ter)
        # Saving ncontent into a separate file to avoid surcharging the RAM,
        if len(ncontent) > 2000:
            with open(temp_content, "r") as file:
                old_ncontent = file.readlines()
            ncontent = old_ncontent + ncontent
            with open(temp_content, "w") as file:
                file.writelines(ncontent)
            ncontent = []
    ncontent.append("}\n")
    with open(temp_content, "r") as file:
        old_ncontent = file.readlines()
    ncontent = old_ncontent + ncontent
    # Deleting the old content,
    start_index = index_finder(content, first_line)
    end_index = closing_brackets(content, start_index)
    content = content[:start_index] + ncontent + content[end_index + 1:]
    with open("setup_test.txt", "w") as file:
        file.writelines(content)


def indent(string):
    """Create an indented version of string.
    
    Args:
        string(string): a multi-line string
    
    Returns:
        string: the indented version of string.
    """
    lst = string.split("\n")
    nlst = []
    for string in lst:
        nlst.append("\t" + string + "\n")
    to_return = ""
    for string in nlst:
        to_return += string
    return to_return



if __name__ == "__main__":
    edit_territories("setup_orig.txt", progress=True)