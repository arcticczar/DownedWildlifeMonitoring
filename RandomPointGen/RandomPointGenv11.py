# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 17:17:21 2016

@author: MStelmach
"""

import random
import datetime
import sys
import os
import csv
import math
from Tkinter import *
import tkFileDialog


#Statustext = "Status OK"

def SEEF():

        
    #get current date
    now = datetime.datetime.now()

    #get current working directory
    wdpath = os.path.abspath(__file__)
    dname = os.path.dirname(wdpath)
    os.chdir(dname)

    #print os.getcwd()


    # Date range for trials: used to determine trials per week.
    def dateentry(dentry):
        if len(dentry)==0:
            Statustext = "Date fields must be entered"
            status = Label(bottomFrame, text = Statustext , bd=1, relief=SUNKEN, anchor=W)
            status.pack(side=BOTTOM, fill=X)
            
     
    
    SDate = SDEntry.get()
    EDate = EDEntry.get()
    
    dateentry(SDate)
    dateentry(EDate)

    FMT = "%Y-%m-%d" #YYYY-MM-DD
    StartDate = datetime.datetime.strptime(SDate,FMT)
    EndDate = datetime.datetime.strptime(EDate,FMT)
    if (EndDate-StartDate)<datetime.timedelta(0):
        Statustext = "Start date must be before End Date"
        status = Label(bottomFrame, text = Statustext , bd=1, relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)
    else:
        Weeks = (EndDate-StartDate).days/7

        # create results folder
        if not os.path.exists(dname+"\\\\results"): 
                os.makedirs(dname+"\\\\results")
        results = open(makeFile.get(), "a") # create results txt
        
        
        results.write('Year,Month,TrialWeek,PointID,Latitude,Longitude,Site,Turbine,Distance,CarcassType\n')
        
        
        LargeBirds_Phase1= int(LBP1Entry.get())
        MedBirds_Phase1 = int(MBP1Entry.get())
        Rat_Phase1 = int(RP1Entry.get())
        LargeBirds_Phase2= int(LBP2Entry.get())
        MedBirds_Phase2 = int(MBP2Entry.get())
        Rat_Phase2 = int(RP2Entry.get())


        def SEEFGen(Carcasses, CarcassType, phase):
            Trial = []
            while Carcasses > 0:
                #print LargeBirds_Phase1, "remaining"
                #CarcassType = 'LargeBird'
                phase = int(phase)
                if phase == 1:
                    y=random.randint(1,7500)
                elif phase ==2:
                    y=random.randint(7501,12750)
                points = open ('kwprandompointscomplete20161017.csv')
                pointreader = csv.reader(points)
                pointreader.next()
                for row in pointreader:
                    if int(row[0]) == y:
                        #print row
                        phase = row[3]
                        #write the point to a new CSV
                        Trial.append(row[0] +','+ row[1] +','+ row[2] +','+ row[3] +','+ row[4] +','+ row[5] +','+ CarcassType+ '\n')
                points.close()
                Carcasses += -1
                #print 'Large Birds remaining on Phase 1:', LargeBirds_Phase1
            return Trial 

        LBP1 = SEEFGen(int(LargeBirds_Phase1), 'LargeBird', 1)
        MBP1 = SEEFGen(int(MedBirds_Phase1), 'MedBird', 1)
        RP1 = SEEFGen(int(Rat_Phase1), 'Rat', 1)
        LBP2 = SEEFGen(int(LargeBirds_Phase2), 'LargeBird', 2)
        MBP2 = SEEFGen(int(MedBirds_Phase2), 'MedBird', 2)
        RP2 = SEEFGen(int(Rat_Phase2), 'Rat', 2)

        Trials = LBP1+MBP1+RP1+LBP2+MBP2+RP2

        #Determine trials per week
        SEEFnum=len(Trials)
        CarcassesRemaining = SEEFnum
        week = []
        Weekly = int(math.ceil(SEEFnum/Weeks))
        MaxTrials = 2*Weekly
        TrialWeek = 1
        while CarcassesRemaining>0:
            if TrialWeek > Weeks:
                TrialWeek = 1
                Counter = 1
                #print 'counter:', Counter
                #print 'TrialWeek:', TrialWeek
                WeeklyTrials = random.randrange(0,MaxTrials,1)
                #print 'weekly trials:', WeeklyTrials
                if WeeklyTrials == 0:
                    TrialWeek +=1
                else:
                    while Counter <= WeeklyTrials:
                        week.append(TrialWeek)
                        CarcassesRemaining += -1
                        Counter += 1
                    TrialWeek +=1
            else:
                Counter = 1
                #print 'counter:', Counter
                #print 'TrialWeek:', TrialWeek
                WeeklyTrials = random.randrange(0,MaxTrials,1)
                #print 'weekly trials:', WeeklyTrials
                if WeeklyTrials == 0:
                    TrialWeek +=1
                else:
                    while Counter <= WeeklyTrials:
                        week.append(TrialWeek)
                        CarcassesRemaining += -1
                        Counter += 1
                    TrialWeek +=1

        week = sorted(week)   
        #print week
        #print len(week)
        random.shuffle(Trials)
        zipper = zip(week,Trials)
        Trials2=[]
        for line in zipper:
                datecalc = StartDate+datetime.timedelta((line[0]-1)*7)
                year = datecalc.year
                month = datecalc.month
                comb = str(year)+ ',' + str(month)+ ',' + str(line[0])+','+line[1]
                Trials2.append(comb)
 
        #print Trials2
        for line in Trials2:
                results.write(line)
   
        print results, "created"

        results.close()
       

def makefile():
	global fileoutput
	filename2 = tkFileDialog.asksaveasfilename( filetypes = [('all files', '.*'), ('text files', '.txt')])
	filename3=filename2 + '.txt'
	if filename2:
		return fileoutput.set(filename3)

root = Tk()
root.title("SEEF Generator")
#root.geometry("400x600")

fileoutput = StringVar()

topFrame = Frame(root)
topFrame.pack()
bottomFrame= Frame(root)
bottomFrame.pack(side=BOTTOM)


SD = Label(topFrame, text="Start Date Format =YYYY-MM-DD:")
ED = Label(topFrame, text="End Date Format =YYYY-MM-DD:")
SDEntry = Entry(topFrame)
EDEntry = Entry(topFrame)


LBP1label=Label(topFrame, text="Large Birds Phase 1:")
MBP1label=Label(topFrame, text="Medium Birds Phase 1:")
RP1label=Label(topFrame, text="Rats Phase 1:")
LBP2label=Label(topFrame, text="Large Birds Phase 2:")
MBP2label=Label(topFrame, text="Medium Birds Phase 2:")
RP2label=Label(topFrame, text="Rats Phase 2:")
LBP1Entry = Entry(topFrame)
MBP1Entry = Entry(topFrame)
RP1Entry = Entry(topFrame)
LBP2Entry = Entry(topFrame)
MBP2Entry = Entry(topFrame)
RP2Entry = Entry(topFrame)

LBP1Entry.insert(0, "0")
MBP1Entry.insert(0, "0")
RP1Entry.insert(0, "0")
LBP2Entry.insert(0, "0")
MBP2Entry.insert(0, "0")
RP2Entry.insert(0, "0")

SD.grid(row=0, column=0)
ED.grid(row=1, column=0)
SDEntry.grid(row=0, column=1)
EDEntry.grid(row=1, column=1)

LBP1label.grid(row=2, column=0)
MBP1label.grid(row=3, column=0)
RP1label.grid(row=4, column=0)
LBP2label.grid(row=5, column=0)
MBP2label.grid(row=6, column=0)
RP2label.grid(row=7, column=0)
LBP1Entry.grid(row=2, column=1)
MBP1Entry.grid(row=3, column=1)
RP1Entry.grid(row=4, column=1)
LBP2Entry.grid(row=5, column=1)
MBP2Entry.grid(row=6, column=1)
RP2Entry.grid(row=7, column=1)

button = Button(topFrame, text='create file', command=makefile)
button.grid(row=8, column=0)
makeFile=Entry(topFrame, width = 100, textvariable=fileoutput)
makeFile.grid(row=8, column=1)

button = Button(bottomFrame, text="Run", command=SEEF)
button.pack(padx=20,pady=20)

credit = Label(bottomFrame, text="M. Stelmach 2016", anchor=E)
credit.pack(side=RIGHT)


#Status bar
#status = Label(bottomFrame, text = Statustext , bd=1, relief=SUNKEN, anchor=W)
#status.pack(side=BOTTOM, fill=X)


root.mainloop()


#b = SEEF()

