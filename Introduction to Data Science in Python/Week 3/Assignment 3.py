
# coding: utf-8

# # Question 1

# In[227]:

import pandas as pd
import numpy as np

df = pd.read_excel("Energy Indicators.xls",header=0)
df2 = df[:-38]
energy = df2[16:]
del energy['Unnamed: 0']
del energy['Unnamed: 1']
energy.columns.values[0]='Country'
energy.columns.values[1]='Energy Supply'
energy.columns.values[2]='Energy Supply per Capita'
energy.columns.values[3]='% Renewable'


# In[228]:

energy.replace('...', np.nan,inplace = True)


# In[229]:

energy['Energy Supply'] *= 1000000


# In[230]:

def remove_digit(data):
    newData = ''.join([i for i in data if not i.isdigit()])
    i = newData.find('(')
    if i>-1: newData = newData[:i]
    return newData.strip()


# In[231]:

energy['Country'] = energy['Country'].apply(remove_digit)


# In[234]:

energy.loc[energy["Country"] == "Republic of Korea", 'Country'] = "South Korea"
energy.loc[energy["Country"] == "United States of America", 'Country'] = "United States"
energy.loc[energy["Country"] == "United Kingdom of Great Britain and Northern Ireland", 'Country'] = "United Kingdom"
energy.loc[energy["Country"] == "China", 'Country'] = "Hong Kong"


# In[ ]:

######################################################################


# In[244]:

GDP = pd.read_csv('world_bank.csv', skiprows=4)
GDP.loc[GDP["Country Name"] == "Korea, Rep.", 'Country Name'] = "South Korea"
GDP.loc[GDP["Country Name"] == "Hong Kong SAR, China", 'Country Name'] = "Iran"
GDP.loc[GDP["Country Name"] == "Korea, Rep.", 'Country Name'] = "Hong Kong"


# In[250]:

ScimEn = pd.read_excel('scimagojr-3.xlsx')


# In[252]:

#######################################################################


# In[254]:

dv = pd.merge(pd.merge(energy, GDP, on='Country'), ScimEn, on='Country')


# In[ ]:



