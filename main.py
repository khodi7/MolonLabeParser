import pandas as pd
import ast

a = pd.read_csv("territory_data.csv", index_col = 'Unnamed: 0')
print(a.columns)
for index in a.index:
    if not pd.isna(a.at[index, "modifier"]):
        print(ast.literal_eval(a.at[index, "modifier"]), index)
        for i in ast.literal_eval(a.at[index, "modifier"]):
            print(i)