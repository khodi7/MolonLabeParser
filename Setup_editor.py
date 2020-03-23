import pandas as pd
import ast
import os
from pathlib import Path
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


def edit_countries():
#     Todo :
#         - update localization for each country (can just add it at the end off
#         the file) : need country name and tag
#         - update the setup file
#             - update the old countries(change territories owned) : need cores
#             and capital
#             - add new countries in setup file: need tag, government, culture,
#             religion, cores, capital, centralization if tribe.
#         - add the path to the new files of those countries and their id
#         in the countries.txt file: need id and name
#         - create new country files problem : names and colors
    pass


def edit_setup_countries(filename, country_dic):
    """Changes the data related to countries in the file filename.
    
    Args:
        filename(string): path to the setup file we want to edit.
        country_dic(dictionary): obtained by the convert_country_df function
        from the Country module.
    
    Returns:
        None
    """
    pass


def edit_countries_file(filename, country_dic):
    """Modifies the countries txt file according to the data in country_dic.
    
    This function modifies the countries file by adding a line in it for each
    new tag in country_dic and creates the file associated with it (storing it
    at the right place relative to this program's repository.
    
    Note: the countries file is a .txt file in the common repository of I:R.
    It contains every nation's tag associated with the path (from the repository
    in which countries.txt is located) to a txt in which are located information
    relating to the name of the ship or the color of this country.
    The format of the lines of this file is as follow:
    <tag> = "<path/to/the/file/of/this/country>"
    i.e: THE = "countries/greece/thebes.txt"
    
    Args:
        filename(string): path to the countries file to be modified
        country_dic(dictionary): obtained by the convert_country_df function
        from the Country module.
    
    Returns:
        None
    """
    pass


def new_country_file(country, path_to_new_file):
    """Creates a new single country file at a given path.
    
    The new file has the same format as the other .txt files from the countries
    folder.
    
    Args:
        country(Country): the country we want to create a file for.
        path_to_new_file(string): the path from the directory the program is
        to the directory we want the file to be created in.
    """
    # Creating the content of the file.
    content = str(country.color)
    content += "\n"
    print(country.gender_equality)
    if country.gender_equality:
        content += "gender_equality = yes\n"
        content += "\n"
    content += "ship_names = {\n"
    content += "\t#\n"
    content += "}"
    # Creating the path to the file.
    prog_file = Path.cwd()
    path = str(prog_file) + "\\" + path_to_new_file
    print(path)
    # Creating the folders needed.
    Path(path).mkdir(parents=True, exist_ok=True)
    name = "{}.txt".format(country.tag)
    Path(path+name).touch(exist_ok=True)
    os.chdir(path)
    with open(name, "w") as file:
        file.writelines(content)
    os.chdir(prog_file)

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
    province_setup_edit()