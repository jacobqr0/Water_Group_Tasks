#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd


# In[2]:


cwd = os.path.abspath('') #identify path for the current working directory
files = os.listdir(cwd) #create list of files in the current working directory


# In[3]:


df = pd.DataFrame() # create a blank dataframe object
month = 0 #set month to zero
for file in files: #loop over every file in the cwd
    if file.endswith('xls'): #only apply functions to excel files
        sheet = pd.read_excel(file) #read the file 
        month = month +1 #value for the month column
        sheet['month'] = month #create the month column 
        sheet['year'] = 2017 #create year column
        df = df.append(sheet.loc[6:36], ignore_index = True) #append the data to the master dataframe


# In[4]:


#set column names
df.columns = ['empty', 'day', 'inf_bod_mgl', 'inf_bod_ppd', 'inf_CBOD_mgl', 'inf_CBOD_ppd', 'prim_bod_mgl', 'eff_cbod_mgl', 'eff_cbod_ppd',
             'cen_bod_mgl', 'inf_TSS_mgl', 'inf_TSS_ppd', 'prim_TSS_mgl', 'prim_load_ppd', 'eff_TSS_mgl', 'eff_TSS_ppd',
             'cen_TSS_mgl', 'MLSS1', 'MLSS2', 'RAS_TSS1', 'RAS_TSS2', 'WAS_TSS1', 'WAS_TSS2', 'MLVSS1', 'MLVSS2','month', 'year']


# In[5]:


#create date column
df['date'] = pd.to_datetime(df[['year', 'month', 'day']], format = '%m/%d/%Y')


# In[6]:


#selet data of interest
df = df[['date','inf_bod_mgl', 'inf_bod_ppd', 'inf_CBOD_mgl', 'inf_CBOD_ppd', 'prim_bod_mgl', 'eff_cbod_mgl', 'eff_cbod_ppd',
             'cen_bod_mgl', 'inf_TSS_mgl', 'inf_TSS_ppd', 'prim_TSS_mgl', 'prim_load_ppd', 'eff_TSS_mgl', 'eff_TSS_ppd',
             'cen_TSS_mgl', 'MLSS1', 'MLSS2', 'RAS_TSS1', 'RAS_TSS2', 'WAS_TSS1', 'WAS_TSS2', 'MLVSS1', 'MLVSS2']]


# In[7]:


final_df = df.dropna(how='all') #drop all null records


# In[8]:


final_df.to_excel('PG2_2017_combined.xls') #save to excel file


# In[ ]:




