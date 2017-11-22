# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 09:05:31 2017

@author: mstelmach
"""

import datetime
import os

# User input for the target file folder
sensor_file_folder = raw_input("Full file path for sensor files:") #get path

#Create a file folder and file to contain results.
#if not os.path.exists(sensor_file_folder+"\\\\results"): # create results folder
#    os.makedirs(sensor_file_folder+"\\\\results")
#    results = open(sensor_file_folder+"\\\\results\\\\results.txt", "a") # create results txt file

time_record_dict = {}

for file in os.listdir(sensor_file_folder):
    if file.startswith("KWP") and file.endswith(".txt"): #read all sensor files
        print file+" :"
        
#        results.write(file+" :\n")
        
        sensor = open(sensor_file_folder+"\\\\"+file)
        sensorlist =  sensor.readlines()
        sensortime = []
        for line in sensorlist:
            if len(line.split(","))==1:
                values= line.split("\t")
            else:
                values = line.split(",")
            #values = line.split(",")
            #print len(values)
            #break
            sensortime.append(values[0]+"\t"+values[1]) # add date and time
        #print sensortime
        sensor.close()

        fmt = []
        FMT = "%Y-%b-%d\t%H:%M:%S" # read date and time
        sensortime = sensortime[1:]
        for time1 in sensortime:
            pytime = datetime.datetime.strptime(time1, FMT)
            fmt.append(pytime)
            

        #print fmt
        for time2 in fmt:
            try:
                t1
            except:
                t1=time2
                time_record_dict[file.split('_')[0]][t1.strftime(FMT)]={'start':t1}
                continue
            else:
                timeshift = time2-t1
                if timeshift > datetime.timedelta(hours=6): # if time is greater than 1hr 6 mins and 40 sec return date and time
                    print t1, "to", time2,":", timeshift
                    time_record_dict[file.split('_')[0]]={'end':t1}
                elif timeshift< datetime.timedelta(hours=6):
                    
#                        results.write(str(t1)+ " to "+ str(time2)+" : "+ str(timeshift)+"\n")
                
                t1=time2
del t1
#results.close()