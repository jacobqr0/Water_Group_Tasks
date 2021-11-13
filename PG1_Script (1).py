#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os 


# In[2]:


cwd = os.path.abspath('')
files = os.listdir(cwd)


# In[3]:


df = pd.DataFrame()
month = 0
for file in files:
    if file.endswith('.xls'):
        sheet = pd.read_excel(file)
        month= month+1
        sheet['month'] = month
        sheet['year'] = 2020
        df = df.append(sheet.loc[6:36], ignore_index = True)


# In[4]:


'''change column names'''
df.columns = ['empty', 'day', 'precip', 'inf_flow', 'eff_flow', 'max_temp', 'min_temp', 'chamber_cl', 'final_cl', 'fecal_coli',
             'PBL1', 'PBL2', 'PBL3', 'PBL4', 'SBL1', 'SBL2', 'SBL3', 'SBL4', '3MS1', '3MS2', 'SVI1', 'SVI2', 'month', 'year']


# In[5]:


'''create a date column'''
df['date'] = pd.to_datetime(df[['year', 'month', 'day']], format='%m/%d/%Y')


# In[6]:


'''select data of interest'''
df = df[['date', 'precip', 'inf_flow', 'eff_flow', 'max_temp', 'min_temp', 'chamber_cl', 'final_cl', 'fecal_coli',
        'PBL1', 'PBL2', 'PBL3', 'PBL4', 'SBL1', 'SBL2', 'SBL3', 'SBL4', '3MS1', '3MS2', 'SVI1', 'SVI2']]


# In[7]:


'''drop empty rows'''
final_df = df.dropna(how='all')


# In[8]:


final_df.to_excel('PG1_2020_Combined.xls')


# In[ ]:





# In[ ]:




