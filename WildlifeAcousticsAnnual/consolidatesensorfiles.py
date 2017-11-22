# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 08:39:25 2017

@author: mstelmach
"""

import os
import pandas as pd

inputfolder= r'W:\2017WAData\results'

df=pd.DataFrame()


for root, dirs, files in os.walk(inputfolder):
        
        for sensorfile in files:
            if sensorfile.startswith('KWP') and sensorfile.endswith('_named.xlsx'):
                current = r'{}/{}'.format(root,sensorfile).replace('\\','/')
                
                 #create a new file path with new name
                
                df = df.append(pd.read_excel(current)) #read data into memory

df.to_csv(r'w:\2017wadata\results\2017sensorcompiled.txt')