# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 10:02:14 2017

@author: mstelmach
"""

import os
import sys
import pandas as pd
import ephem
import datetime


#specify the folder containing corrected and compiled sensor files
# the expected input is the folder containing the xlsx files form the Mergefiles.py program
inputfolder = r'w:/2017WAData/results'


# create column names for data
cols = []

for root, dirs, files in os.walk(inputfolder):
        
        for sensorfile in files:
            if sensorfile.startswith('KWP') and sensorfile.endswith('.xlsx'):
                unit_name = sensorfile.split("/")[-1].split('.')[0]
                cols.append(unit_name)
                


cols = [item for item in set(cols)]
         
cols.sort()

#Define the rows 
dates = pd.date_range('6/1/2016', periods=396)

sensordf = pd.DataFrame(0, index=dates, columns=cols)

log=open(r'w:/2017WAData/results/logfile.txt','a')

def sm_read(inputfile):
    try:
            
        if os.path.exists(inputfile):
            
            #get the unit name from the file
            unit_name = sensorfile.split("/")[-1].split('.')[0]
            print inputfile, unit_name
            
            file_read = pd.read_excel(inputfile)               
            
            #get current sunset and sunrise
            maui=ephem.Observer()
            
            maui.lat, maui.lon = '20.81','-156.55'
            
            #Datetime format
            FMT='%Y-%b-%d %X'
            
            first_date = None  # keeps a record of the first date for the unit in the sensor file
            end_date=None
            initial_datetime = None 
            prior_time = None
            end_time = None
            run_time=datetime.timedelta(seconds=0)
            record = {unit_name:{}}
            
            for index, row in file_read.iterrows():
                get_date= row[0] + ' ' + row[1]
                date_time = datetime.datetime.strptime(get_date, FMT)
                
                #set the start date and time of the current recording
                if initial_datetime == None:
                    initial_datetime = date_time
                    #print 'initial datetime : ', initial_datetime
                    maui.date=ephem.Date(date_time) #set the date for sunrise/sunset
                    
                #set the date for the recording period (month)
                if first_date == None:
                    first_date=date_time
                
                #Calculate the total number of hours of darkness
                darkness_hours = maui.next_rising(ephem.Sun()).datetime()-maui.next_setting(ephem.Sun()).datetime()
                
                if darkness_hours<datetime.timedelta(0):
                    darkness_hours= maui.next_rising(ephem.Sun()).datetime()-maui.previous_setting(ephem.Sun()).datetime()
                
                #for the first record, set the datetime to the current record
                if prior_time == None:
                    prior_time=initial_datetime
                
                #Check the prior time against the current time for continuity
                #if the time exceeds 6 hours it will be considered discontinuous
                
                elif date_time-prior_time < datetime.timedelta(hours=6) and date_time-prior_time>datetime.timedelta(hours=0):
                    run_time += (date_time-prior_time)
                    prior_time=datetime.datetime.strptime(get_date, FMT)
                
                elif date_time-prior_time<datetime.timedelta(hours=0):  
                    pass
                
                #if the time is discontinuous record the period start, end, 
                #and proportion of the active hours vs the total darkness hours
                
                else:
                    
                    log.write('unit {}: finish time: {}, run time: {} \n'.format(unit_name, prior_time, prior_time-initial_datetime))
                    
                    date = initial_datetime.date()
                    date = datetime.datetime.combine(date, datetime.datetime.min.time())  #return 00:00 timestamp to datetime for comparison with pandas timestamp
                    proportion = (prior_time-initial_datetime).total_seconds()/darkness_hours.total_seconds()
                    print initial_datetime, prior_time, proportion
                    if run_time>datetime.timedelta(hours=6):
                        sensordf[unit_name][date]=1
                        print date, unit_name, sensordf[unit_name][date]
                    
                    #After recording the data reset the records
                    initial_datetime = None
                    prior_time = None
                    end_time = None
                    run_time=datetime.timedelta(seconds=0)
                    end_date=date_time
                    
                        
            
        else:
            print '{} : no such file'.format(inputfile)
            
       
        del (unit_name, 
             maui, 
             FMT, 
             first_date, 
             end_date, 
             initial_datetime, 
             prior_time, 
             end_time, 
             run_time, 
             record, 
             get_date, 
             date_time, 
             darkness_hours
             )
    except:
        err = sys.exc_info()
        print '{}\n{}\n{}'.format(err[0],err[1],err[2])
        
        
    
for root, dirs, files in os.walk(inputfolder):
        
    for sensorfile in files:
        if sensorfile.startswith('KWP') and sensorfile.endswith('.xlsx'):
            current = r'{}/{}'.format(root,sensorfile).replace('\\','/')
            sm_read(current)

log.close()  
print sensordf
sensordf.to_excel(r'w:\2017WAData\results\ActiveNights.xlsx', sheet_name='Sheet1')