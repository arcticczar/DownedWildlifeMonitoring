# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 10:39:41 2017

@author: mstelmach
"""

import os
import sys
import pandas as pd
import ephem
import datetime


#specify the folder containing song meter sensor files
inputfolder = r'w:/2017WAData'


# create column names for data
cols = []

for root, dirs, files in os.walk(inputfolder):
        
        for sensorfile in files:
            if sensorfile.startswith('KWP') and sensorfile.endswith('.txt'):
                unit_name = sensorfile.split("_")[0].split("/")[-1]
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
            
            unit_name = inputfile.split("_")[0].split("/")[-1]
            print inputfile, unit_name
            
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
    #                log=open(r'w:/2017WAData/results/logfile.txt','a')
    #                log.write('{},{},{},{}\n'.format (unit_name, date_time, prior_time, date_time- prior_time))
    #                log.close()
                    run_time += (date_time-prior_time)
                    prior_time=datetime.datetime.strptime(get_date, FMT)
                
                elif date_time-prior_time<datetime.timedelta(hours=0):  
                    pass
                
                #if the time is discontinuous record the period start, end, 
                #and proportion of the active hours vs the total darkness hours
                
                else:
                    #iterate over the current units records to see if there was a previous record and change the end time.
    #                for item, detail in record[unit_name].iteritems():
    #                    if (datetime.datetime.strptime()-ephem.localtime(maui.previous_setting(ephem.Sun()))).total_seconds()/60/60 < 10:
    #                        pass
                    
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
                    
                        
            '''
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
            '''
            #print the results dictionary (formatted readable)
    #        for item, detail in record.iteritems():
    #            for item2, detail2 in detail.iteritems():
    #                print 'name:',item, 'date:',item2, 'start:',detail2['start'], 'end:',detail2['end'], 'proportion:',detail2['proportion']
            
        else:
            print '{} : no such file'.format(inputfile)
            
       
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
             darkness_hours
             )
    except:
        err = sys.exc_info()
        print '{}\n{}\n{}'.format(err[0],err[1],err[2])
        
        
    
for root, dirs, files in os.walk(inputfolder):
        
    for sensorfile in files:
        if sensorfile.startswith('KWP') and sensorfile.endswith('.txt'):
            current = r'{}/{}'.format(root,sensorfile).replace('\\','/')
            sm_read(current)

log.close()  
print sensordf
sensordf.to_excel(r'w:\2017WAData\results\ActiveNights.xlsx', sheet_name='Sheet1')