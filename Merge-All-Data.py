#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os 


# In[2]:


cwd = os.path.abspath('') #identify path for the current working directory
files = os.listdir(cwd) #create list of files in the current working directory


# In[6]:


dfPG1 = pd.read_excel('PG1_Master_2017-2021.xls')
dfPG2 = pd.read_excel('PG2_Master_2017-2021.xlsx')
dfPG3 = pd.read_excel('PG3_Master_2017-2021.xlsx')
dfPG4 = pd.read_excel('PG4_Master_2017-2021.xlsx')
dfPG5 = pd.read_excel('PG5_Master_2017-2021.xlsx')
dfPG6 = pd.read_excel('PG6_Master_2017-2021.xlsx')
dfPG7 = pd.read_excel('PG7_Master_2017-2021.xlsx')


# In[7]:


df1to2 = pd.merge(dfPG1, dfPG2, on = 'date')


# In[8]:


df1to3 = pd.merge(df1to2, dfPG3, on = 'date')


# In[9]:


df1to4 = pd.merge(df1to3, dfPG4, on ='date')


# In[10]:


df1to5 = pd.merge(df1to4, dfPG5, on = 'date')

df1to6 = pd.merge(df1to5, dfPG6, on = 'date')

df1to7 = pd.merge(df1to6, dfPG7, on = 'date')


# In[11]:


df1to7['day'] = df1to7['date'].dt.day 


# In[12]:


#PG1
'''['date', 'precip', 'inf_flow', 'eff_flow', 'max_temp', 'min_temp', 'chamber_cl', 'final_cl', 'fecal_coli',
        'PBL1', 'PBL2', 'PBL3', 'PBL4', 'SBL1', 'SBL2', 'SBL3', 'SBL4', '3MS1', '3MS2', 'SVI1', 'SVI2']]'''
#PG2
'''['date','inf_bod_mgl', 'inf_bod_ppd', 'inf_CBOD_mgl', 'inf_CBOD_ppd', 'prim_bod_mgl', 'eff_cbod_mgl', 'eff_cbod_ppd',
             'cen_bod_mgl', 'inf_TSS_mgl', 'inf_TSS_ppd', 'prim_TSS_mgl', 'prim_load_ppd', 'eff_TSS_mgl', 'eff_TSS_ppd',
             'cen_TSS_mgl', 'MLSS1', 'MLSS2', 'RAS_TSS1', 'RAS_TSS2', 'WAS_TSS1', 'WAS_TSS2', 'MLVSS1', 'MLVSS2']'''
#PG3
'''['date', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11', 'a12', 'a13', 'a14', 'a15', 'a16']'''
#PG4
'''['date','inf_TP_mgl', 'inf_TP_ppd', 'eff_TP_mgl', 'eff_TP_ppd', 'prim_eff_TP_mgl', 'cen_TP_mgl', 
             'inf_NH3_mgl', 'inf_NH3_ppd', 'eff_NH3_mgl', 'eff_NH3_ppd', 'prim_eff_NH3_mgl', 'cen_NH3_mgl', 'inf_pH',
             'eff_pH', 'bld_sludge_pH', 'dig1_pH', 'dig2_pH']'''
#PG5
'''['date', 'bld_sludge_TS_perc', 'bld_slg_TS_load_ppd', 'bld_slg_TS_75_ppd', 'bld_slg_TS_avg', 
              'bld_slg_TS_GPD', 'TVS_bld_slg', 'TVS_prim_slg', 'TVS_dig1', 'TVS_dg2', 'TVS_cent_feed', 'TVS_VR', 
              'FMB1','FMB2', 'max_outfall_temp_F', 'min_outfall_temp_F', 'avg_outfall_temp_F' ]'''
#PG6
'''['date', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'b10', 'b11', 'b12', 'b13', 'b14', 
         'b15', 'b16']'''
#PG7
'''['date', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 
          'c12', 'c13', 'c14', 'c15', 'c16', 'c17', 'c18', 'c19', 'c20', 'c21', 'c22', 'c23']'''


# In[13]:


final_df = df1to7[['date', 'day', 'precip', 'inf_flow', 'eff_flow','max_temp', 'min_temp', 'inf_pH', 'inf_bod_mgl', 
                  'inf_TSS_mgl','inf_TP_mgl', 'inf_NH3_mgl','inf_bod_ppd', 'inf_TSS_ppd', 'inf_TP_ppd', 'inf_NH3_ppd',
                  'max_outfall_temp_F', 'min_outfall_temp_F', 'avg_outfall_temp_F','eff_pH','chamber_cl', 'final_cl', 
                   'fecal_coli','eff_cbod_mgl', 'eff_TSS_mgl', 'eff_TP_mgl','eff_NH3_mgl','eff_cbod_ppd','eff_TSS_ppd',
                  'eff_TP_ppd','eff_NH3_ppd','prim_bod_mgl','prim_TSS_mgl', 'prim_eff_TP_mgl', 'prim_eff_NH3_mgl',
                  'prim_load_ppd','cen_bod_mgl','cen_TSS_mgl','cen_NH3_mgl','cen_TP_mgl', 'PBL1', 'PBL2', 'PBL3', 'PBL4', 
                   'SBL1', 'SBL2', 'SBL3', 'SBL4', '3MS1', '3MS2', 'SVI1', 'SVI2', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 
                   'a9', 'a10', 'a11', 'a12', 'a13', 'a14', 'a15', 'a16', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 
                   'b10', 'b11', 'b12', 'b13', 'b14', 'b15', 'b16','c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 
                   'c11','c12', 'c13', 'c14', 'c15', 'c16', 'c17', 'c18', 'c19', 'c20', 'c21', 'c22', 'c23', 'inf_CBOD_mgl', 
                   'inf_CBOD_ppd', 'MLSS1', 'MLSS2', 'RAS_TSS1', 'RAS_TSS2', 'WAS_TSS1', 'WAS_TSS2', 'MLVSS1', 'MLVSS2',
                  'bld_sludge_pH', 'dig1_pH', 'dig2_pH','bld_sludge_TS_perc', 'bld_slg_TS_load_ppd', 'bld_slg_TS_75_ppd', 'bld_slg_TS_avg', 
                  'bld_slg_TS_GPD', 'TVS_bld_slg', 'TVS_prim_slg', 'TVS_dig1', 'TVS_dg2', 'TVS_cent_feed', 'TVS_VR', 
                  'FMB1','FMB2']]


# In[14]:


final_df.to_excel('ALL_Oshkosh_Data_2017-2021.xlsx')


# In[ ]:




