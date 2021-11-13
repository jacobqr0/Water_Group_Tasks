#!/usr/bin/env python
# coding: utf-8

# In[16]:


import os 
import pandas as pd


# In[17]:


cwd = os.path.abspath('')
files = os.listdir(cwd)


# In[18]:


df = pd.DataFrame()
month = 0
for file in files:
    if file.endswith('.xls'):
        sheet = pd.read_excel(file)
        month = month + 1
        sheet['month'] = month
        sheet['year'] = 2017
        df = df.append(sheet.loc[6:36], ignore_index = True)


# In[19]:


list = []
x=0
for i in range(19):
    list.append('a' +str(x))
    x = x + 1


# In[20]:


list[1] = 'day'
list[17] = 'month'
list[18] = 'year'


# In[21]:


#Set column names
df.columns = list


# In[22]:


#make date column
df['date'] = pd.to_datetime(df[['year', 'month', 'day']], format = '%m/%d/%Y')


# In[23]:


#select data of interest
df = df[['date', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11', 'a12', 'a13', 'a14', 'a15', 'a16']]


# In[24]:


#Drop empty rows
final_df = df.dropna(how='all')


# In[25]:


final_df.to_excel('PG3_2017_Combined.xlsx') #write to excel


# In[ ]:




