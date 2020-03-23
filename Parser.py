import pandas as pd


# Write here the path to the save file you want to parse,
# You can only put its name if it is in the same repository as this program,
save_filename = "DoA debug.rome"


def create_pop_data_file(file, progress = False, csv_name = "pop_data.csv"):
    """Creates a .csv of the pops in an IR save file.
    
    Args:
        file(str): file is a file name or path to an IR save file made while the game was in debug mode.
        progress(boolean): indicates wheter or not the progress of the function should be shown in the console
        csv_name(string): the name of the file in wich the data will be saved. Please use a .csv extension if you decide to change the default name.
    
    Returns:
        None
    """
    # Creating the DataFrame
    cols = ["type", "culture", "religion"]
    df = create_IR_DataFrame(file, progress, opening_line = "\tpopulation={\n",
                             cols = cols)
    df.to_csv(csv_name)

        

def create_territory_data_file(file, progress = False,
                               csv_name = "territory_data.csv"):
    """Creates a .csv of the territories in an IR save file.
    
    Args:
        file(str): file is a file name or path to an IR save file made while the
        game was in debug mode.
        progress(boolean): indicates wheter or not the progress of the function
        should be shown in the console
        csv_name(string): the name of the file in wich the data will be saved.
        Please use a .csv extension if you decide to change the default name.
    
    Returns:
        None
    """
    cols = ['state', 'owner', 'controller', 'last_owner_change',
            'last_controller_change', 'claim', 'original_culture',
            'original_religion', 'culture', 'religion', 'population_ratio',
            'pop', 'civilization_value', 'trade_goods', 'num_of_roads',
            'num_foreign_culture', 'num_other_religion', 'blockaded',
            'blockaded_percent_per_navy', 'province_rank', 'buildings',
            'fort', 'looted', 'plundered', 'unit', 'possible_migrant',
            'garrison', 'port', 'province_name', 'variables', 'growing_pop',
            'migrant', 'assimilate', 'convert', 'promote', 'demote', 'modifier']
    df = create_IR_DataFrame(file, progress,
                             opening_line = "provinces={\n",
                             cols = cols, special_cols = "pop")
    df.to_csv(csv_name)


def create_diplomacy_data_file(file, progress = False,
                               csv_name = "diplomacy_data.csv"):
    """Creates a .csv of the diplomatic relations in an IR save file.
    
    Args:
        file(str): file is a file name or path to an IR save file made while the
        game was in debug mode.
        progress(boolean): indicates whether or not the progress of the function
        should be shown in the console
        csv_name(string): the name of the file in which the data will be saved.
        Please use a .csv extension if you decide to change the default name.
    
    Returns:
        None
    """
    # Creating the DataFrame
    cols = ['tag', 'historical', 'country_name', 'flag', 'coat_of_arms',
            'country_type', 'family', 'minor_family', 'variables',
            'graphical_culture', 'gender_equality', 'num_stance_changes',
            'currency_data', 'is_antagonist', 'capital', 'original_capital',
            'current_regnal_number', 'historical_regnal_numbers',
            'has_senior_ally', 'primary_culture', 'religion',
            'military_tradition', 'diplomatic_stance', 'heritage',
            'military_tradition_levels', 'sub_unit', 'sub_unit_access',
            'sub_unit_construction_count', 'combat_tactics', 'laws',
            'unit_counts', 'ideas', 'not_supporting_primary_heir', 'technology',
            'recovery_motivation', 'starting_population', 'monthly_manpower',
            'current_income', 'estimated_monthly_income', 'averaged_income',
            'economy', 'religious_unity', 'foreign_religion_pops',
            'total_population', 'succession', 'diplomatic_action',
            'possible_inventions_packed', 'government_key', 'civic_party',
            'military_party', 'mercantile_party', 'religious_party',
            'populist_party', 'succession_law', 'monarchy_military_reforms',
            'monarchy_maritime_laws', 'monarchy_economic_law',
            'monarchy_citizen_law', 'monarchy_religious_laws',
            'monarchy_legitimacy_laws', 'monarchy_contract_law',
            'monarchy_divinity_statutes', 'monarchy_subject_laws',
            'republic_military_recruitment_laws', 'republic_election_reforms',
            'corruption_laws', 'republican_mediterranean_laws',
            'republican_religious_laws', 'republic_integration_laws',
            'republic_citizen_laws', 'republican_land_reforms',
            'republic_military_recruitment_laws_rom',
            'republic_election_reforms_rom', 'corruption_laws_rom',
            'republican_mediterranean_laws_rom',
            'republican_religious_laws_rom', 'republic_integration_laws_rom',
            'republic_citizen_laws_rom', 'republican_land_reforms_rom',
            'tribal_religious_law', 'tribal_currency_laws',
            'tribal_centralization_law', 'tribal_authority_laws',
            'tribal_autonomy_laws', 'tribal_domestic_laws',
            'tribal_decentralized_laws', 'tribal_centralized_laws',
            'tribal_super_decentralized_laws', 'tribal_super_centralized_laws',
            'max_manpower', 'blockaded_percent',
            'blockaded_percent_per_province', 'units',
            'active_inventions', 'export', 'economic_policies', 'monarch',
            'ruler_term', 'country_characters_packed', 'successors',
            'last_trade_route_creation_date', 'governorship', 'total_holdings',
            'possible_holdings', 'total_power_base', 'non_loyal_power_base',
            'total_cohorts', 'num_ships_under_construction',
            'num_regs_under_construction', 'num_forts_under_construction',
            'loyal_cohorts', 'disloyal_cohorts', 'loyal_pops', 'defect_pops',
            'centralization', 'legitimacy', 'primary', 'second', 'flank',
            'last_war', 'last_battle_won', 'cached_happiness_for_owned',
            'cached_pop_count_for_owned', 'pooled_army_power', 'ai', 'host_ai',
            'color', 'color2', 'modifier']
    special_args = ["color"]
    df = create_IR_DataFrame(file, progress,
                             opening_line = "\tcountry_database={\n",
                             cols = cols, special_args=special_args)
    df.to_csv(csv_name)


def create_IR_DataFrame(file, progress, opening_line, cols,
                        special_cols=[], special_args=[]):
    """Creates a .csv of the diplomatic relations in an IR save file.
    
    Note: need to be optimized for pops.
    
    Args:
        file(str): file is a file name or path to an IR save file made while the
        game was in debug mode.
        progress(boolean): indicates whether or not the progress of the function
        should be shown in the console
        csv_name(string): the name of the file in which the data will be saved.
        Please use a .csv extension if you decide to change the default name.
        opening_line(str): the first line of the data.
        cols(list of strings): the columns of the dataframe.
        special_cols(list of strings): the columns for which several values are
        affected to for a same label.
    
    Returns:
        DataFrame: a DataFrame containing the data linked with the opening_line
        wich columns are defined by cols
    """
    with open(file) as file:
        content = file.readlines()
    index = index_finder(content, opening_line)
    # Finding the biggest country ID
    start_index = index
    end_index = closing_brackets(content, index)
    lenght = end_index - start_index
    # Creating the DataFrame
    before_ei = end_index - 1
    while content[before_ei].count("}") == 0:
        before_ei -= 1
    last_index = opening_brackets(content, before_ei)
    last_id = int(content[last_index].split("=")[0].strip())
    df = pd.DataFrame(index=range(0, last_id), columns = cols) 
    index += 1
    while index < end_index:
        if progress:
            prog = ((index-start_index)*100) // lenght
            print("{0}%".format(prog))
        try:
            label = int(content[index].split("=")[0].strip())
        except ValueError:
            label = None
        if label is not None:
            end_prov = closing_brackets(content, index)
            index += 1
            # Entering a province data
            while index < end_prov:
                try:
                    value = content[index].split("=")[1].strip()
                except IndexError:
                    value = None
                key = content[index].split("=")[0].strip()
                if value is not None:
                    if value == "{":
                        value_end = closing_brackets(content, index)
                        ml_value = ["{\n"] + content[index + 1 : value_end + 1]
                        df.at[label, key] = ml_value
                        index = closing_brackets(content, index)
                    elif key in special_cols:
                        try:
                            df.at[label, key].append(int(value))
                            index += 1
                        except AttributeError:
                            df.at[label, key] = [int(value)]
                            index += 1
                    elif key in special_args:
                        df.at[label, key] = value.strip('"')
                        # Next color.
                        key = content[index].split("=")[1].split()[-1]
                        value = content[index].split("=")[2].strip()
                        df.at[label, key] = value.strip('"')
                        index += 1

                    else:
                        df.at[label, key] = value.strip('"')
                        index += 1
                else:
                    index += 1
        else:
            index += 1
    return df
                        

def index_finder(lst, line):
    """Finds the index of line in file
    
    Args:
        lst(list): a list of strings.
        line(str): the line we're looking for.
        
    Returns:
        int: the index of line in file
    """
    i = 0
    found = False
    index = None
    while not found and i < len(lst):
        if lst[i] == line:
            found = True
            index = i
        i+=1
    return index


def closing_brackets(lst, index):
    """Finds the closing bracket associated with the one in lst[index]
    
    Args:
        lst(list): a list of string.
        index(int): index such as list[index] contains only one opening bracket
        and no closing bracket after it.
    
    Returns:
        int: a value(i) like lst[i] contains the closing bracket.
    """
    opened = 0
    line = lst[index].split("}")
    opened += 1
    for closing in line:
        opened -= 1
        opened += closing.count("{")
    while opened > 0:
        index += 1
        line = lst[index].split("}")
        opened += 1
        for closing in line:
            opened -= 1
            opened += closing.count("{")
    return index


def opening_brackets(lst, index):
    """Finds the opening bracket associated with the one in lst[index]
    
    Args:
        lst(list): a list of string.
        index(int): index such as list[index] contains only one closing bracket
        and no opening bracket before it.
    
    Returns:
        int: a value(i) like lst[i] contains the opening bracket.
    """
    to_open = 1
    while to_open > 0:
        index -= 1
        line = lst[index].split("{")
        to_open += 1
        for i in range(len(line)):
            j = len(line) - 1 - i
            to_open -= 1
            to_open += line[j].count("}")
    return index


if __name__ == "__main__":
    create_territory_data_file(save_filename, progress = True)
    create_diplomacy_data_file(save_filename, progress = True)