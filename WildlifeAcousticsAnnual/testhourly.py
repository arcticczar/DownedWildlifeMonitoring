# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 13:22:57 2017

@author: mstelmach
"""

import os
import datetime as dt
import pandas as pd


inputfolder = r'w:/2017WAData/results'

for root, dirs, files in os.walk(inputfolder):
        
        for sensorfile in files:
            if sensorfile.startswith('KWP') and sensorfile.endswith('_named.xlsx'):
                current = r'{}/{}'.format(root,sensorfile).replace('\\','/')
                DF1 = pd.read_excel(current)
                DF2 = pd.DataFrame()
                for row in DF1:
                
                