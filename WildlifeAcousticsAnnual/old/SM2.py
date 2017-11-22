# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 11:28:29 2017

@author: mstelmach
"""


import datetime
import os
import sys

import pandas as pd
import ephem




def sm_read(inputfile):
    
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
                print 'initial datetime : ', initial_datetime
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
            
            elif date_time-prior_time < datetime.timedelta(hours=6):
                log=open(r'w:/2017WAData/results/logfile.txt','a')
                log.write('{},{},{},{}\n'.format (unit_name, date_time, prior_time, date_time- prior_time))
                log.close()
                run_time += (date_time-prior_time)
                prior_time=datetime.datetime.strptime(get_date, FMT)
            
            #if the time is discontinuous record the period start, end, 
            #and proportion of the active hours vs the total darkness hours
            
            else:
                #iterate over the current units records to see if there was a previous record and change the end time.
#                for item, detail in record[unit_name].iteritems():
#                    if (datetime.datetime.strptime()-ephem.localtime(maui.previous_setting(ephem.Sun()))).total_seconds()/60/60 < 10:
#                        pass
                log=open(r'w:/2017WAData/results/logfile.txt','a')
                log.write('finish time: {}, run time: {} \n'.format(prior_time, prior_time-initial_datetime))
                log.close()        
                record[unit_name][datetime.datetime.strftime(initial_datetime, FMT)]= {'start': initial_datetime, 
                                                                            'end': prior_time,
                                                                            'proportion':(prior_time-initial_datetime).total_seconds()/darkness_hours.total_seconds()}
                #After recording the data reset the records
                initial_datetime = None
                prior_time = None
                end_time = None
                run_time=datetime.timedelta(seconds=0)
                end_date=date_time
                
    
            
        
        #total days is the difference between the last and first sensor readings
        print 'unit : ', unit_name
        print 'total days = ', (end_date-first_date).total_seconds()/60/60/24
        
        #an active night is counted if the unit was active for more than 50% of the night
        active_nights = 0
        
        #Duplicates holds dates with more than one record
        duplicates = []
        
        #Dates holds all unique dates for the detector.
        dates= []
        for item, detail in record.iteritems():
            for times in record[item]:
                
                date = record[item][times]['start'].date()
                if date not in dates and record[item][times]['proportion']>0.5:
                    dates.append(date)
                    active_nights +=1
                    
                elif date in dates:
                    duplicates.append(date)
                    
        
        print 'active nights:', active_nights
        
        print 'duplicates:', duplicates
        
        #Calculate any missing dates from the sorted list of dates
        dates.sort()
        all_dates = set(dates[0]+datetime.timedelta(x) for x in range((dates[-1]-dates[0]).days))
        missing = all_dates-set(dates)
        missed = open(r'w:/2017WAData/results/missed.txt','a')
        missed.write('{},{}\n'.format(unit_name, missing))
        missed.close()
        print 'missing:', missing
        
        #print the results dictionary (formatted readable)
#        for item, detail in record.iteritems():
#            for item2, detail2 in detail.iteritems():
#                print 'name:',item, 'date:',item2, 'start:',detail2['start'], 'end:',detail2['end'], 'proportion:',detail2['proportion']
        
    else:
        print '{} : no such file'.format(inputfile)
        
    return record
    del (unit_name, 
         file_open, 
         maui, 
         file_read, 
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
         darkness_hours, 
         active_nights, 
         duplicates, 
         
         missing
         )
    
    



#Create an empty dictionary to collect results from multiple input files.
total_read={}

inputfolder = r'w:/2017WAData'

#if the input is a single file process it individually.
if os.path.isfile(inputfolder):
    for item, detail in sm_read(inputfolder).iteritems():
        if item in total_read:
            for date, times in detail.iteritems():
                total_read[item][date]=times
        else:
            total_read[item]=detail
            
else:
    #Read through files and folders in a directory and return only sensor files as labeled for KWP.
    for root, dirs, files in os.walk(inputfolder):
        
        for sensorfile in files:
            if sensorfile.startswith('KWP') and sensorfile.endswith('.txt'):
                current = r'{}/{}'.format(root,sensorfile).replace('\\','/')
                for item, detail in sm_read(current).iteritems():
                    if item in total_read:
                        for date, times in detail.iteritems():
                            total_read[item][date]=times
                    else:
                        total_read[item]=detail
                    
#Create a pandas table with the results to export to excel.
column_names = ['unit', 'date', 'start', 'end', 'proportion']
rows = []

for item, detail in total_read.iteritems():
    for date, times in detail.iteritems():
        rows.append([item, date, detail[date]['start'], detail[date]['end'], detail[date]['proportion']])
        
df = pd.DataFrame(rows, columns=column_names)

df.sort_values(['unit','date'], inplace=True)
df.to_excel(r'W:\2017WAData\results\results.xlsx', sheet_name='Sheet1')
