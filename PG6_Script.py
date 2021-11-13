#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import pandas as pd


# In[ ]:


cwd = os.path.abspath('')
files = os.listdir(cwd)


# In[ ]:


df = pd.DataFrame()
month = 0
for file in files:
    if file.endswith('.xls'):
        sheet = pd.read_excel(file)
        month = month + 1
        sheet['month'] = month
        sheet['year'] = 2017
        df = df.append(sheet.loc[6:36], ignore_index = True)


# In[ ]:


list = []
x = 0
for i in range (19):
    list.append('b'+str(x))
    x = x + 1


# In[10]:


list[1] = 'day'
list[17] = 'month'
list[18] = 'year' 
df.columns = list 


# In[13]:


df['date'] = pd.to_datetime(df[['year', 'month', 'day']], format = '%m/%d/%Y') 


# In[14]:


df = df[[ 'date', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'b10', 'b11', 'b12', 'b13', 'b14', 
         'b15', 'b16']]


# In[15]:


final_df = df.dropna(how='all')
final_df.to_excel('PG6_2017_Combined.xlsx')


# In[ ]:




