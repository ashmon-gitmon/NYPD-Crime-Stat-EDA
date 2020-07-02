# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:13:48 2020

@author: ashwi
"""

import pandas as pd
import numpy as np

df = pd.read_csv('NYPD_Complaint_Data_Historic.csv')

df['CMPLNT_FR_DT'] = df['CMPLNT_FR_DT'].astype(str)

ndf = pd.DataFrame()

df.iloc[1,1][-2:]

str()

def yr(yer):
    if yer=='15':
        return True
    else:
        return False
    
yr(df.iloc[1,1][-2:])

df.iloc[1,:]

for i in range(0,len(df)):
    if yr(str(df.iloc[i,1][-2:])):
        ndf.append(df.iloc[i,:])
  
      