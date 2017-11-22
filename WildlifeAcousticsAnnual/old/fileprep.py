# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 13:27:04 2017

@author: mstelmach
"""

import os
import sys
import pandas as pd
import ephem
import datetime

input_file = r'W:\2017WAData\20160710\Sensor\KWP1-01_Sensor-A.txt'

print os.path.exists(input_file)

readfile = open(input_file, 'r+')


def fileprep(inputfile):
    #Datetime format
    FMT='%Y-%b-%d %X'
    counter=0
    if os.path.exists(inputfile):
        
        unit_name = inputfile.split("_")[0].split("/")[-1]
        print unit_name
        
        file_open = open(inputfile, 'r')
        
        #SM3 creates CSV files, SM2 creates tab delimited files
        #check for file type and read it into memory
        if len(file_open.readline().split(','))>1:
            file_open.close()
            file_read = pd.read_csv(inputfile)
        else:
            file_open.close()
            file_read = pd.read_table(inputfile, header=None)
            
            
        prior = None
        current = None
        nextline = None
        
        
        
        
        for index, row in file_read.iterrows():
            
            get_date= row[0] + ' ' + row[1]
            date_time = datetime.datetime.strptime(get_date, FMT)
            
            if counter==0:
                prior = date_time
                print 'prior: {}'.format(prior)
            elif counter==1:
                current = date_time
                print 'current: {}'.format(current)
            elif counter==2:
                nextline= date_time
                print 'nextline: {}'.format(nextline)
            
            if prior and current and nextline:
                
                if prior<current<nextline:
                    print prior, current, nextline
                else:
                    print 'ERROR' , prior, current, nextline
                    break
            
            
            
                nextline=current
                current = prior
                prior=date_time
                
            counter +=1
            print 'counter {}'.format(counter)
            

fileprep(input_file)
                
readfile.close()
