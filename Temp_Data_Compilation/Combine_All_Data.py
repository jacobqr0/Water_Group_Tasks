#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os 
import pandas as pd 


# In[2]:


ppg1 = pd.read_csv('PPG1_20392334_062218_020921.csv')
ppg2 = pd.read_csv('PPG2_20392332_062218_020921.csv')
ppg3 = pd.read_csv('PPG3_20392331_041519_020921.csv')
ppg4 = pd.read_csv('PPG4_20392330_062218_020921.csv')
ppg5 = pd.read_csv('PPG5_20392333_062218_020921.csv')
ppg6 = pd.read_csv('PPG6_20392329_062218_020921.csv')


# In[3]:


ppg1.head()


# In[4]:


ppg1['date'] = pd.to_datetime(ppg1['Date_Time'])  
PPG1_OUTFALL_ppg1 = ppg1.loc[(ppg1['date']< '9/7/2018 11:00')]


# In[5]:


PPG1_ofall_upstream = ppg1.loc[(ppg1['date']>'9/7/2018 11:00')]


# In[6]:


PPG1_OUTFALL_ppg1['Location'] = 'PPG Outfall'
PPG1_ofall_upstream['Location'] = 'PPG Outfall Upstream'


# In[7]:


df1 = PPG1_OUTFALL_ppg1.append(PPG1_ofall_upstream)


# In[8]:


df1['Gen_Location'] = 'PPG Outfall'
df1['Probe']= 'PPG1'
df1 = df1[['Date_Time', 'Temp', 'Location', 'Gen_Location', 'Probe']] #df1 contains updated location for PPG1


# In[9]:


ppg2['Location'] = 'PPG Outfall'
ppg2['Gen_Location'] = 'PPG Outfall'
ppg2['Probe'] = 'PPG2'
df2 = ppg2[['Date_Time', 'Temp', 'Location', 'Gen_Location', 'Probe']] #df2 contains updated Location for PPG2
df2.head()


# In[10]:


ppg3['date'] = pd.to_datetime(ppg3['Date_Time'])
ppg3_upstreamtrib = ppg3.loc[(ppg3['date']< '9/18/2018  9:00:00')]
ppg3_upstreamtribup = ppg3.loc[(ppg3['date']> '9/18/2018  9:00:00')]


# In[11]:


ppg3 = ppg3.sort_values(['date'])
ppg3.head()


# In[12]:


ppg3_upstreamtrib = ppg3.loc[(ppg3['date']< '9/18/2018  9:00:00')]
ppg3_upstreamtribup = ppg3.loc[(ppg3['date']> '9/18/2018  9:00:00')]


# In[13]:


ppg3_upstreamtrib['Location'] = 'Upstream Tributary'
ppg3_upstreamtrib['Gen_Location'] = 'Upstream Tributary'


# In[14]:


ppg3_upstreamtribup['Location'] = 'Upstream Tributary, Upstream'
ppg3_upstreamtribup['Gen_Location'] = 'Upstream Tributary'
ppg3_upstreamtribup.head()


# In[15]:


df3 = ppg3_upstreamtrib.append(ppg3_upstreamtribup)
df3['Probe'] = 'PPG3'
df3 = df3[['Date_Time', 'Temp', 'Location', 'Gen_Location', 'Probe']] #df3 contains updated Location for PPG3
df3.head()


# In[16]:


ppg4['Location'] = 'Upstream Tributary'
ppg4['Gen_Location'] = 'Upstream Tributary'
ppg4['Probe'] = 'PPG4'
df4 = ppg4[['Date_Time', 'Temp', 'Location', 'Gen_Location', 'Probe']] #df4 contains updated locations for PPG4


# In[17]:


df4.head()


# In[18]:


ppg5['Location'] = 'Downstream Confluence'
ppg5['Gen_Location'] = 'Downstream Confluence'
ppg5['Probe'] = 'PPG5'
df5 = ppg5[['Date_Time', 'Temp', 'Location', 'Gen_Location', 'Probe']] #df5 contains updated locations for PPG5
df5.head()


# In[19]:


ppg6['Location'] = 'Downstream Confluence'
ppg6['Gen_Location'] = 'Downstream Confluence'
ppg6['Probe'] = 'PPG6'
df6 = ppg6[['Date_Time', 'Temp', 'Location', 'Gen_Location', 'Probe']] #df5 contains updated locations for PPG5
df6.head()


# In[52]:


#write files to csv
df1.to_csv('update_PPG1_20392334_062218_020921.csv')
df2.to_csv('update_PPG2_20392332_062218_020921.csv')
df3.to_csv('update_PPG3_20392331_041519_020921.csv')
df4.to_csv('update_PPG4_20392330_062218_020921.csv')
df5.to_csv('update_PPG5_20392333_062218_020921.csv')
df6.to_csv('update_PPG6_20392329_062218_020921.csv')


# In[20]:


#Create Master Sheet
master = df1.append(df2)
master = master.append(df3)
master = master.append(df4)
master = master.append(df5)
master = master.append(df6)


# In[21]:


#read DNR limits Table
limits = pd.read_excel('DNR_limits.xlsx')


# In[22]:


limits.head(7)


# In[23]:


#create Month column for master
master['Month'] = pd.DatetimeIndex(master['Date_Time']).month
master.head()


# In[24]:


master = pd.merge(master, limits)
master.head()


# In[25]:


#write master sheet to csv
master.to_csv('20210816_PPG_Master_Sheet.csv')


# In[ ]:




