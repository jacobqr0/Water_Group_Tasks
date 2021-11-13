#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd


# In[2]:


cwd = os.path.abspath('') #identify path for the current working directory
files = os.listdir(cwd) #create list of files in the current working directory


# In[3]:


df = pd.DataFrame()# create a blank dataframe object
month = 0  #set month to zero
for file in files: #loop over every file in the cwd
    if file.endswith('.xls'): #only apply functions to excel files
        sheet = pd.read_excel(file) #read the file
        month = month + 1 #value for the month column
        sheet['month'] = month  #create the month column
        sheet['year'] = 2019 #create year column
        df = df.append(sheet.loc[6:36], ignore_index=True) #append the data to the master dataframe


# In[4]:


#Create column names
df.columns = ['empty', 'day', 'inf_TP_mgl', 'inf_TP_ppd', 'eff_TP_mgl', 'eff_TP_ppd', 'prim_eff_TP_mgl', 'cen_TP_mgl', 
             'inf_NH3_mgl', 'inf_NH3_ppd', 'eff_NH3_mgl', 'eff_NH3_ppd', 'prim_eff_NH3_mgl', 'cen_NH3_mgl', 'inf_pH',
             'eff_pH', 'bld_sludge_pH', 'dig1_pH', 'dig2_pH', 'month', 'year']


# In[5]:


#create date column
df['date'] = pd.to_datetime(df[['year', 'month', 'day']], format = '%m/%d/%Y')


# In[6]:


#select the data of interest
df = df[['date','inf_TP_mgl', 'inf_TP_ppd', 'eff_TP_mgl', 'eff_TP_ppd', 'prim_eff_TP_mgl', 'cen_TP_mgl', 
             'inf_NH3_mgl', 'inf_NH3_ppd', 'eff_NH3_mgl', 'eff_NH3_ppd', 'prim_eff_NH3_mgl', 'cen_NH3_mgl', 'inf_pH',
             'eff_pH', 'bld_sludge_pH', 'dig1_pH', 'dig2_pH']]


# In[7]:


final_df = df.dropna(how = 'all') #drop the null records


# In[8]:


final_df.to_excel('PG4_2019_combined.xls') #save to excel file


# In[ ]:




