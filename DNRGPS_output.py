import os

import utm
from Tkinter import *
import tkFileDialog
import pandas as pd

def dnrconvert():

    wdpath = os.path.abspath(__file__)
    dname = os.path.dirname(wdpath)
    os.chdir(dname)

    seeffile = "H:/KWP/Environmental/CARE/FY16-17/2017-01-04 CARE Locations.txt"
    #seeffile = str(openFile.get())

    dnrgpsfmt = ('type,\
                 ident,\
                 Latitude,\
                 Longitude,\
                 y_proj,\
                 x_proj,\
                 comment,\
                 display,\
                 symbol,\
                 dist,\
                 proximity,\
                 color,\
                 altitude,\
                 depth,\
                 temp,\
                 time,\
                 wpt_class,\
                 sub_class,\
                 attrib,\
                 link,\
                 state,\
                 country,\
                 city,\
                 address,\
                 zip,\
                 facility,\
                 crossroad,\
                 ete,\
                 dtype,\
                 model,\
                 filename,\
                 ltime,\
                 magvar,\
                 geoidheight,\
                 desc,\
                 fix,\
                 sat,\
                 hdop,\
                 vdop,\
                 pdop,\
                 ageofdgpsdata,\
                 dgpsid,\
                 dir \n')

    
    

    #label = seeffile.rstrip('.csv') + '-DNRGPS.txt'
    label = makeFile.get()

    print label

    csvfile = pd.read_csv(seeffile)
        
    DNR = open (label, 'a')
    DNR.write(dnrgpsfmt)

    for i in range(len(csvfile)):
        latlon = utm.to_latlon(float(csvfile.loc[i]['Longitude']),
                               float(csvfile.loc[i]['Latitude']),
                               4,
                               'Q')
        DNR.write('WAYPOINT, ' + \
                  str(csvfile.loc[i]['CarcassType'])\
                  + str(csvfile.loc[i]['PointID']) \
                  +'-KWP'\
                  + str(csvfile.loc[i]['Site'])\
                  + '-'+ str(csvfile.loc[i]['Turbine'])\
                  + ','+ str(latlon[0])\
                  + ','+ str(latlon[1])\
                  +',' + str(csvfile.loc[i]['Latitude'])\
                  +','+ str(csvfile.loc[i]['Longitude'])\
                  + ', Turbine '\
                  + str(csvfile.loc[i]['Turbine'])\
                  +' Distance '\
                  + str(csvfile.loc[i]['Distance'])\
                  +', Flag, Blue,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\n')
        
    
    DNR.close()

    print 'Complete'



def openfile():
    global fileinput
    filename = tkFileDialog.askopenfilename()
    if filename:
        return fileinput.set(filename)

def makefile():
	global fileoutput
	filename2 = tkFileDialog.asksaveasfilename( filetypes = [('all files', '.*'),
                                                 ('text files', '.txt')])
	filename3=filename2 + '.txt'
	if filename2:
		return fileoutput.set(filename3)

root = Tk()

fileinput = StringVar()
fileoutput = StringVar()

root.title("DNRGPS converter")

button = Button(root, text='open file', command=openfile)
button.grid(row=0, column=0)
openFile=Entry(root, width = 100, textvariable=fileinput)
openFile.grid(row=0, column=1)

button = Button(root, text='create file', command=makefile)
button.grid(row=1, column=0)
makeFile=Entry(root, width = 100, textvariable=fileoutput)
makeFile.grid(row=1, column=1)



run = Button(root, text='Run', command = dnrconvert)
run.grid(columnspan=2)

root.mainloop()
