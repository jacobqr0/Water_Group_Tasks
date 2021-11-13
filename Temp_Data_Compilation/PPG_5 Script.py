#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import os 


# In[2]:


cwd = os.path.abspath('') # set the cwd 
files = os.listdir(cwd) #make a list of files in the cwd


# In[3]:


#compile all PPG_5 data

df = pd.DataFrame() # create an empty datafram

for file in files:
    if file.startswith('PPG_5') and file.endswith('.csv'): #apply only to the ppg_5 data files
        ppg_5 = pd.read_csv(file, header=1, usecols= [1,2]) #read the ppg5 file, locate where columns are read, use columns 1&2
        rows = ppg_5[:-12]#delete the last 12 rows of data
        df = df.append(rows, ignore_index =True)#append the files to a blank dataframe


# In[6]:


#rename columns to something simpler
df = df.rename(columns = {'Date Time, GMT-05:00':'Date_Time','Temp, °F (LGR S/N: 20392333, SEN S/N: 20392333)': 'Temp'})


# In[9]:


# fill empty date columns with the other date column
df['Date_Time'].fillna(df['Date Time, GMT-06:00'], inplace = True)


# In[10]:


#select only the Date and Temp columns
df = df[['Date_Time', 'Temp']] 


# In[11]:


df.head()


# In[12]:


df.tail()


# In[13]:


df.to_csv('PPG5_20392333_062218_020921.csv')

