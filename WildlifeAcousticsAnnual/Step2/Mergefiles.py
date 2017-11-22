# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 10:38:26 2017

@author: mstelmach
"""

import os
import pandas as pd


#specify the folder containing the output of 'Timecorrection.py'
#the input is expected to be excel converted and corrected sensor files.
input_folder = r'w:\2017WAData'

#create a dictionary to collect key values containing unit names and 
# values containing sensor file path names.
detectors = {}


#look through subdirectories of the input folder
for root, dirs, files in os.walk(input_folder):
        
        for sensorfile in files:
            #return only excel files that start with KWP expectation is that they
            # are all valid sensor files (no built in error handling)
            if sensorfile.startswith('KWP') and sensorfile.endswith('.xlsx'):
                #return the current file name
                current = r'{}/{}'.format(root,sensorfile).replace('\\','/')
                #return the detector name
                detector = sensorfile.split('_')[0]
                print sensorfile
                
                #create a key value pair if the detector is not in the dictionary
                # files are added as a list
                if detector not in detectors:
                    detectors[detector]=[current]
                #otherwise add the file to the existing key list of files
                else:
                    detectors[detector].append(current)
                

# for each detector collect each of the files and merge them.
for item, detail in detectors.iteritems():
    collector = pd.DataFrame()
    for sensorfile in detail:
        df=pd.read_excel(sensorfile)
        collector=collector.append(df)
    #Arrange the dataframe by date then time
    collector.sort_values([collector.columns[0],collector.columns[1]])
    collector.to_excel(r'w:\2017WAData\results\{}.xlsx'.format(item))