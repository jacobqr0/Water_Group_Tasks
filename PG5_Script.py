#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os 


# In[2]:


cwd = os.path.abspath('') #identify path for the current working directory
files = os.listdir(cwd) #create list of files in the current working directory


# In[3]:


df = pd.DataFrame()
month = 0
for file in files:
    if file.endswith('.xls'):
        sheet = pd.read_excel(file)
        month= month+1
        sheet['month'] = month
        sheet['year'] = 2017
        df = df.append(sheet.loc[6:36], ignore_index = True)


# In[4]:


'''make list for column names'''
list = []
for i in range(20):
    list.append('a'+ str(i))


# In[5]:


'''set column names for data of interest'''
list[1] = 'day'
list[19] = 'year'
list[18] = 'month'
list[17] = 'avg_outfall_temp_F'
list[16] = 'min_outfall_temp_F'
list[15] ='max_outfall_temp_F'
print(list)


# In[6]:


#Set the columns names 
df.columns = ['a0', 'day', 'bld_sludge_TS_perc', 'bld_slg_TS_load_ppd', 'bld_slg_TS_75_ppd', 'bld_slg_TS_avg', 
              'bld_slg_TS_GPD', 'TVS_bld_slg', 'TVS_prim_slg', 'TVS_dig1', 'TVS_dg2', 'TVS_cent_feed', 'TVS_VR', 
              'FMB1','FMB2', 'max_outfall_temp_F', 'min_outfall_temp_F', 'avg_outfall_temp_F', 'month', 'year'] 


# In[7]:


'''create a date column'''
df['date'] = pd.to_datetime(df[['year', 'month', 'day']], format = '%m/%d/%Y')


# In[8]:


'''select data of interest'''
df = df[['date', 'bld_sludge_TS_perc', 'bld_slg_TS_load_ppd', 'bld_slg_TS_75_ppd', 'bld_slg_TS_avg', 
              'bld_slg_TS_GPD', 'TVS_bld_slg', 'TVS_prim_slg', 'TVS_dig1', 'TVS_dg2', 'TVS_cent_feed', 'TVS_VR', 
              'FMB1','FMB2', 'max_outfall_temp_F', 'min_outfall_temp_F', 'avg_outfall_temp_F' ]]


# In[9]:


'''drop rows that have null values for every parameter'''
final_df = df.dropna(how='all')


# In[10]:


final_df.to_excel('PG5_2017_combined.xls') #write dataframe to an excel file


# In[ ]:




