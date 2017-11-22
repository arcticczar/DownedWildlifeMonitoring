# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
import os
import datetime

import pandas as pd


#input_file=r'H:\MyDocuments\WorkFiles\KWP\Python\SensorFiles\KWP2-02_Sensor-TESTB.txt'
inputfolder=r'W:\2017WAData'

counter = 2

def get_date(day, time):
    FMT='%Y-%b-%d %X'
    string = day + ' ' + time
    date_time = datetime.datetime.strptime(string, FMT)
    return date_time


err_list=[]

#look for errors in the dates
def datecorrect(inputfile):   
    
    file_open = open(inputfile, 'r')
        
    #SM3 creates CSV files, SM2 creates tab delimited files
    #check for file type and read it into memory
    if len(file_open.readline().split(','))>1:
        file_open.close()
        df = pd.read_csv(inputfile)
        sensortype='sm3'
        
    else:
        file_open.close()
        df = pd.read_table(inputfile, header=None)
        sensortype='sm2'
    
    print sensortype
    
    del_list = []
    count = 2
    while count<len(df):
        
        if sensortype == 'sm2':
            col_id=0
            col_id2=1
        elif sensortype == 'sm3':
            col_id=df.columns[0]
            col_id2=df.columns[1]
        
        time1 = get_date(df.loc[count-2, col_id], df.loc[count-2,col_id2])
        time2 = get_date(df.loc[count-1, col_id], df.loc[count-1,col_id2])
        time3 = get_date(df.loc[count, col_id], df.loc[count,col_id2])
        
        #Remove times greater than 1 month apart
        if abs((time3-time2).total_seconds()/60/60/24)>30:
                del_list.append(count)
        
        if time1<time2<time3:
            #print 'Times are correct'
            pass
        else:
            if time3<time2:
                print 'Error {} is less than {}'.format(time3, time2)
                if time3+datetime.timedelta(days=1)>time2 and (time3+datetime.timedelta(days=1)).date()==time2.date():
                    print 'corrected date is {}'.format(time3+datetime.timedelta(days=1))
                    df.loc[count,col_id]=datetime.datetime.strftime(time2, '%Y-%b-%d')
                else:
                    del_list.append(count)
                    print '{} will be deleted'.format(time3)

            
            
        
        count+=1
    for item in del_list:
        df=df[df.index != item]
    try:
        df.to_excel(inputfile.split('.')[0]+'.xlsx')
    except:
        print sys.displayhook()
        print sys.excepthook()
        err_list.append(inputfile)
        

for root, dirs, files in os.walk(inputfolder):
        
        for sensorfile in files:
            if sensorfile.startswith('KWP') and sensorfile.endswith('.txt'):
                current = r'{}/{}'.format(root,sensorfile).replace('\\','/')
                print current
                datecorrect(current)
                

print err_list   
