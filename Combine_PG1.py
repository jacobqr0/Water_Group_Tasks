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
for file in files:
    if file.endswith('.xls'):
        sheet = pd.read_excel(file)
        df = df.append(sheet, ignore_index = True)


# In[4]:


df.to_excel('PG4_Master_2017-2021.xlsx')

