import string
import datetime
import os


text = raw_input("Full file path for sensor files:") #get path
if not os.path.exists(text+"\\\\results"): # create results folder
    os.makedirs(text+"\\\\results")
    results = open(text+"\\\\results\\\\results.txt", "a") # create results txt file
for file in os.listdir(text):
    if file.endswith(".txt"): #read all text files
        print file+" :"
        results.write(file+" :\n")
        
        sensor = open(text+"\\\\"+file)
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
                continue
            else:
                timeshift = time2-t1
                if timeshift > datetime.timedelta(seconds=4000): # if time is greater than 1hr 6 mins and 40 sec return date and time
                        print t1, "to", time2,":", timeshift
                        results.write(str(t1)+ " to "+ str(time2)+" : "+ str(timeshift)+"\n")
                
                t1=time2
del t1
results.close()