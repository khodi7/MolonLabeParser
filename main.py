"""

Run this file to generate a new setup.
Please do not modify anything in this file apart from the variable in the
module level variables block.
The directory you are executing this program from shouldn't contain any
directories names "countries".

Attributes:
    original_countries_file(string): name of or path to a copy of the
    countries.txt file from the common directory of the I:R game files.
    original_pronvince_file(string): name of or path to a copy of the
    province_setup.csv file from the common directory of the I:R game files.
    original_setup_file(string): name of or path to a copy of the setup.txt file
    from the common directory of the I:R game files.
    progress(boolean): indicates whether or not the progress of the program
    is shown.
    save_file(string): name of or path to the save file you want to create a new
    setup from.
"""
from Parser import (create_pop_data_file, create_territory_data_file,
                    create_diplomacy_data_file)
from Setup_editor import (province_setup_edit, edit_territories, edit_countries)


#---Start of the module level variables---#
original_countries_file = "countries.txt"
original_province_file = "province_setup.csv"
original_setup_file = "setup.txt"
progress = True
save_file = "DoA debug.rome"
#---End of the module level variables---#

# Parsing part
file = save_file
create_pop_data_file(file, progress)
create_territory_data_file(file, progress)
create_diplomacy_data_file(file, progress)
# Updating the province setup csv file.
province_setup_edit(original_province_file=original_province_file)
# Updating the territory part of the setup file.
edit_territories(original_setup_file, progress=progress)
# Adding new countries.
edit_countries(save_file, original_setup_file, original_countries_file,
               original_setup_file)