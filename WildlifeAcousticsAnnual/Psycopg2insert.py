# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 06:10:38 2017

@author: MStelmach
"""

import psycopg2
import os
import pandas as pd

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
    
    
try:
    conn = psycopg2.connect("dbname='KWP-WA' user='Matt Stelmach' host='localhost' password=''")
except:
    print "I am unable to connect to the database"
    
cur=conn.cursor()

inputfolder = r'H:\MyDocuments\WorkFiles\KWP\Wildlife Acoustics\2017Summary'

for root, dirs, files in os.walk(inputfolder):
        
        for sensorfile in files:
            if sensorfile.startswith('KWP') and sensorfile.endswith('.txt'):
                current = r'{}/{}'.format(root,sensorfile).replace('\\','/')
                print current
    
                file_open = open(current, 'r')
        
                #SM3 creates CSV files, SM2 creates tab delimited files
                #check for file type and read it into memory
                if len(file_open.readline().split(','))>1:
                    file_open.close()
                    df = pd.read_csv(current)
                    sensortype='sm3'
                    
                else:
                    file_open.close()
                    df = pd.read_table(current, header=None)
                    sensortype='sm2'     
                    
                if sensortype =='sm2':
                    for index, row in df.iterrows():
                        cur.execute("""INSERT INTO "SensorFiles" ("SensorDate", "SensorTime", "Unit") VALUES (%s,%s,%s)""",[row[0],row[1],sensorfile.split('_')[0]])
                        
                elif sensortype =='sm3':
                    for index, row in df.iterrows():
                        cur.execute("""INSERT INTO "SensorFiles" ("SensorDate", "SensorTime", "Unit") VALUES (%s,%s,%s)""",[row['DATE'],row['TIME'],sensorfile.split('_')[0]])
                
                

conn.commit()

cur.close()
conn.close()