# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 15:12:58 2019

@author: ASUS
"""


import pandas as pd
from bs4 import BeautifulSoup

df=pd.read_csv('C:/Users/Louis/Downloads/DoA 2.0 _Revenge of the Greeks_ - Sheet1.csv')
df.dropna(subset=['Tag'],inplace=True)
print(df)

file=open('C:/Users/Louis/Downloads/DoA2.0_input.rome','r')
content=file.readlines()
count=0

for n in range(len(content)):
    if 'tag=' in content[n]:
        for index,row in df.iterrows():
            if pd.notna(row['Max manpower']) and (row['Tag'].upper() in content[n]):
                print(content[n])
                while ('tag=' not in content[n+1]) and  ('state=' not in content[n+1]):
                    if 'manpower' in content[n]:
                        if content[n].find('manpower') ==4:
                            content[n]='\t\t\t\tmanpower='+str(row['Max manpower'])+'\n'
                            print(content[n])
                    n=n+1
            else:
                pass
    
    count+=1
file.close()
outfile=open('C:/Users/Louis/Downloads/DoA2.0_27_December_2019_ManpowerEdited.rome','w')
outfile.writelines(line for line in content)
outfile.close()

#%% Political Influence

import pandas as pd

file=open('C:/Users/Louis/Downloads/DoA2.0_input.rome','r')
content=file.readlines()

df=pd.DataFrame(columns=['tag','PI'])
count_tag=0

for n in range(len(content)):
    if 'tag=' in content[n]:
        df.at[count_tag,'tag']=content[n]
        while ('tag=' not in content[n+1]) and  ('state=' not in content[n+1]):
            if ('political_influence' in content[n]) and ('100' not in content[n]):
                if content[n].find('political_influence')==4:
                    content[n]='\t\t\t\tpolitical_influence=100\n'
                    print(content[n])
            n=n+1
        count_tag=count_tag+1



file.close()
outfile=open('C:/Users/Louis/Downloads/DoA2.0_13th_Labor_of_Hercules_PI_fix.rome','w')
outfile.writelines(line for line in content)Doc
outfile.close()

#%% Gold

import pandas as pd

file=open('C:/Users/Louis/Downloads/DoA2.0_input.rome','r')
content=file.readlines()

df=pd.DataFrame(columns=['tag','PI','gold'])
count_tag=0

for n in range(len(content)):
    if 'tag=' in content[n]:
        df.at[count_tag,'tag']=content[n].replace('\t','').replace('\n','')
        while ('tag=' not in content[n+1]) and  ('state=' not in content[n+1]):
            if ('gold=' in content[n]):
                print(content[n])
                if content[n].find('gold')==4:
#                    content[n]='\t\t\t\tgold=100\n'
                    df.at[count_tag,'gold']=content[n].replace('\t','').replace('\n','').replace('gold=','')
#                    print(content[n])
                    pass
            n=n+1
        count_tag=count_tag+1



file.close()
# outfile=open('C:/Users/Louis/Downloads/DoA2.0_13th_Labor_of_Hercules_PI_fix.rome','w')
# outfile.writelines(line for line in content)
# outfile.close()

#%%

def add_pop(file,territory_ID,Liste_pops,pop_culture,pop_religion):
    
    file=open(file,'r')
    content=file.readlines()
    
    df=pd.DataFrame(columns={'number','type','culture','religion'})
    
    nb_citizen=Liste_pops[0]
    nb_freemen=Liste_pops[1]
    nb_tribesmen=Liste_pops[2]
    nb_slaves=Liste_pops[3]
    for n in range(nb_citizen):
        df=df.append({'type':'citizen','culture':pop_culture,'religion':pop_religion},ignore_index=True)
    for n in range(nb_freemen):
        df=df.append({'type':'freemen','culture':pop_culture,'religion':pop_religion},ignore_index=True)
    for n in range(nb_tribesmen):
        df=df.append({'type':'tribesmen','culture':pop_culture,'religion':pop_religion},ignore_index=True)
    for n in range(nb_slaves):
        df=df.append({'type':'slaves','culture':pop_culture,'religion':pop_religion},ignore_index=True)
    
    df,content=create_pops(df,content)
    
    for n in range(len(content)):
        if content[n]=='\t'+str(territory_ID)+'={\n':
            n_territory=n
    
    n=n_territory
    while content[n]!='\t}\n':
        if '\t\tpop=' in content[n]:
            if '\t\tpop=' not in content[n+1]:
                for i in range(df.shape[0]):
                    content[n]=content[n]+'\t\tpop='+str(df.at[i,'number'])+'\n'
        n=n+1
    
    outfile=open('C:/Users/Louis/Documents/Paradox Interactive/Imperator/save games/out.rome','w')
    outfile.writelines(line for line in content)
    outfile.close() 
    
    return df

def create_pops(df_pops,content):
    
    for n in range(len(content)):
        if 'population={' in content[n]:
            if '\tpopulation={\n' not in content[n]:
                n_pop=n
        if 'provinces={' in content[n]:
            n_prov=n
    
    i=0
    while '={' not in content[n_prov-1+i]:
        i=i-1

    last_pop_nb=int(content[n_prov-1+i].split('=')[0])
    
    for n in range(df_pops.shape[0]):
        df_pops.at[n,'number']=last_pop_nb+1+n
    
    added_pop_string=''
    for n in range(df_pops.shape[0]):
        added_pop_string=added_pop_string+str(df_pops.at[n,'number'])+'={\n\ttype=\"'+str(df_pops.at[n,'type'])+'\"\n\tculture=\"'+str(df_pops.at[n,'culture'])+'\"\n\treligion=\"'+str(df_pops.at[n,'religion'])+'\"\n}\n'
    
    content[n_prov+i+3]=content[n_prov+i+3]+added_pop_string
    
    return df_pops,content

    
    