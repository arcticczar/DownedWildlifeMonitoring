# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 09:31:26 2017

@author: mstelmach
"""
import os
import pandas as pd

inputfolder= r'W:\2017WAData\results'




for root, dirs, files in os.walk(inputfolder):
        
        for sensorfile in files:
            if sensorfile.startswith('KWP') and sensorfile.endswith('.xlsx'):
                current = r'{}/{}'.format(root,sensorfile).replace('\\','/')
                newname = sensorfile.split('.')[0] + "_named.xlsx"  #change the name of the new file
                update = r'{}/{}'.format(root,newname).replace('\\','/') #create a new file path with new name
                print "Current: ", current, " File: ", sensorfile.split('.')[0]
                df = pd.read_excel(current) #read data into memory
                df2=pd.DataFrame() #create new empty data frame
                if "DATE" in df.columns: #define rows for SM3
                    
                    df2['SensorDATE']=df["DATE"]
                    df2['SensorTIME']=df['TIME']
                    
                elif 0 in df and 1 in df:
                    df2['SensorDATE']=df[0]
                    df2['SensorTIME']=df[1]
                    
                df2["name"]= sensorfile.split('.')[0]
                df2.to_excel(update)