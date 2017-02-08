"""
This script creates a shape uses 10 minute averages from 
weather data to create a merged predictive shape for
downed wildlife monitoring.
"""

import os
import datetime
import sys
import math

import arcpy
from arcpy import env

#Set environmental variables
env.workspace = sys.path[0]
arcpy.env.overwriteOutput = True

#Set the Projection to EPSG 32604 WGS 84 UTM 4 North - Hawaii
prj = arcpy.SpatialReference(32604)

#NOTE:Define Variables for ArcGIS tool dialogue box
rotor = float(arcpy.GetParameter(0))
nacelle = float(arcpy.GetParameter(1))
carcass = float(arcpy.GetParameter(2))
cr = datetime.timedelta(days = carcass)
area = float(arcpy.GetParameter(3))
MaximumSearchDistance = (nacelle+rotor)*(float(area)/100)
MaxWindSpeed = float(arcpy.GetParameter(4))

#Example inputs
#rotor = float(50)
#nacelle = float(100)
#carcass = float(6)
#cr = datetime.timedelta(days = carcass)
#area = float(75)
#MaximumSearchDistance = (nacelle+rotor)*(float(area)/100)
#MaxWindSpeed = float(15)

#NOTE:Specify CSV with Fatality data
Fatalities = arcpy.GetParameterAsText(5)

#NOTE:Specify CSV with Weather Data
Weather = arcpy.GetParameterAsText(6)


a=open(Fatalities)
fat_header=len(a.readlines())
a.close()

c=open(Weather)
weather_header=len(c.readlines())
c.close()

#NOTE:Specify CSV for data
try:
    if rotor>=nacelle:
        arcpy.AddError("Rotor radius cannot exceed Nacelle height")
        arcpy.GetMessages()
    elif fat_header==0 or weather_header==0:
        arcpy.AddError("CSV files must contain data")
        arcpy.GetMessages()
    else:
        fat_reader=open(Fatalities)
        
        #NOTE: create empty lists for fatality data and weather data
        fat_list = []
        weather_list = []
        #NOTE: Read weather data in the format M/D/YYYY
        weather=open(Weather)
        FMT = "%m/%d/%Y"
        #Note: Add a header to the temp file
        for row in fat_reader.readlines():
            if "Common" in row:
                continue
            rs = row.split(",")
            #NOTE: append Date, Name, SiteTurbine
            fat_list.append([datetime.datetime.strptime(rs[0],FMT),
                            rs[1], rs[5].rstrip()])
        
        
        for row in weather.readlines():
            #Skip the first row if there is a headder
            if "ID" in row:
                    continue
            rs2 = row.split(",")
            #Return the timestamp from CSV
            wthr_dt = rs2[1].split(" ")
            
            #NOTE:append Site-turbine, Windspeed, Yaw, Date, Time
            weather_list.append([rs2[6].rstrip(),
                          rs2[2],
                          rs2[3],
                          datetime.datetime.strptime(wthr_dt[0],FMT),
                          wthr_dt[1]])
        
        fat_reader.close()
        weather.close()

        ellipsedata = []
        #NOTE: Compare lists and append values to ellipsedata list
        for item in fat_list:
            for day in weather_list:
                if item[0] >= day[3] and item[0]-cr <= day[3] and item[2]==day[0]:
                    #Set center of ellipse to utm 0,0
                    X = 0
                    Y = 0
                    FatalityID = day[0]
                    #Ellipse semimajor axis length
                    Major = float(day[1])/MaxWindSpeed*MaximumSearchDistance
                    #Ellipse semiminor axis length
                    Minor = 2*(rotor*1.1)
                    Yaw = day[2]
                    WDate = day[3]
                    WTime = day[4]
                    ellipsedata.append([str(FatalityID),
                                        str(X),
                                        str(Y),
                                        str(Major),
                                        str(Minor),
                                        str(Yaw),
                                        str(WDate),
                                        str(WTime)])


        temp2 = "temp2.csv"

        #output line shapefile
        ELLIPSE = "ellipsetest.shp"

        #output polygon shapefile
        ELLIPSEPOLY = "ellipsepoly.shp"
        
        #If the working shapefile was already created, delete it.
        if arcpy.Exists("ellipsecollector.shp"):
            arcpy.Delete_management("ellipsecollector.shp")
            
        arcpy.CreateFeatureclass_management(sys.path[0],
                                            "EllipseCollector.shp",
                                            "POLYGON",
                                            "",
                                            "",
                                            "",
                                            prj)
        
        #insert field for ID
        arcpy.AddField_management("ellipsecollector.shp",
                                  "SitTurb",
                                  "STRING",
                                  250)
        fid = 0

        for row in ellipsedata:

            write_headers = open(temp2, 'w')
            newstring = ",".join(row)
            write_headers.write('FatalityID,X,Y,Major,Minor,Yaw,Date,Time\n'+ newstring )
            write_headers.close()

            Yaw = float(row[5])
            
            #NOTE: create ellipse
            arcpy.TableToEllipse_management(temp2,
                                            ELLIPSE,
                                            "X",
                                            "Y",
                                            "Major",
                                            "Minor",
                                            "METERS",
                                            "Yaw",
                                            "DEGREES",
                                            "FatalityID",
                                            prj)
            
            #NOTE: create ellipse polygon
            arcpy.FeatureToPolygon_management(ELLIPSE, ELLIPSEPOLY)
            arcpy.AddField_management(ELLIPSEPOLY, "SitTurb", "STRING", 250)
            
            
            #distance from 0,0 to upwind corners
            posdist = math.sqrt(100.0+rotor**2) 
            #angle of upwind right corners
            degree = math.degrees(math.atan(float(rotor)/10.0)) 
            degree1 = 0+degree+float(Yaw)
            #angle of downwind right
            degree2 = 180-math.degrees(math.atan(float(rotor)/float(MaximumSearchDistance)))+Yaw
            # angle of downwind left
            degree3 = 180+math.degrees(math.atan(float(rotor)/float(MaximumSearchDistance)))+Yaw 
            # angle of upwind left
            degree4 = 0-degree+float(Yaw) 
            negdist = math.sqrt(MaximumSearchDistance**2+rotor**2) # distance from 0,0 to downwind corners
            #print "distance to negative corner:",negdist


            #create point coordinates based on rotation and distance
            bound1 = (posdist*math.sin(math.radians(degree1)),
                      posdist*math.cos(math.radians(degree1)))
            bound2 = (negdist*math.sin(math.radians(degree2)),
                      negdist*math.cos(math.radians(degree2)))
            bound3 = (negdist*math.sin(math.radians(degree3)),
                      negdist*math.cos(math.radians(degree3)))
            bound4 = (posdist*math.sin(math.radians(degree4)),
                      posdist*math.cos(math.radians(degree4)))

            # create an array of the 4 tuples
            pointlist = [bound1,bound2,bound3,bound4]
            array = arcpy.Array()
            point = arcpy.Point()
            for corner in pointlist:
                point.X, point.Y = corner[0], corner[1]
                array.add(point)
    
            #Create the bounding box to which the ellipse will be clipped
            if arcpy.Exists("boundingbox.shp"):
                arcpy.Delete_management("boundingbox.shp")
            arcpy.CreateFeatureclass_management( env.workspace,
                                                "boundingbox.shp",
                                                "POLYGON",
                                                "",
                                                "",
                                                "",
                                                prj) 
            cursor = arcpy.da.InsertCursor("boundingbox.shp" , ["SHAPE@"])
            cursor.insertRow([arcpy.Polygon(array)])
    
            del cursor

            #Clip the ellipse to the bounding box
            arcpy.Clip_analysis(ELLIPSEPOLY, "boundingbox.shp", "clipellipse.shp")
            arcpy.Append_management("clipellipse.shp","ellipsecollector.shp")
            curs = arcpy.da.UpdateCursor("ellipsecollector.shp", ["FID","SitTurb"])
            
            #Match FID to Fatality ID
            for en in curs:
                if en[0]==fid:
                    en[1]=row[0]
                curs.updateRow(en)
            del curs
            
            fid += 1
        #Get output shapefile location and merge
        predictiveshape = arcpy.GetParameterAsText(7)
        arcpy.Dissolve_management("ellipsecollector.shp", predictiveshape, "SitTurb")
        
        #Clean up working files
        arcpy.Delete_management("ellipsecollector.shp")
        arcpy.Delete_management("clipellipse.shp")
        arcpy.Delete_management("ellipsetest.shp")
        arcpy.Delete_management("ellipsepoly.shp")
        arcpy.Delete_management("boundingbox.shp")
        os.remove(temp2)

        #NOTE: Create Fatality Shapefile
        fatshape = arcpy.GetParameterAsText(8)
        arcpy.CreateFeatureclass_management(os.path.dirname(os.path.realpath(fatshape)),
                                            os.path.basename(fatshape), "POINT","","","",prj)
        arcpy.AddField_management(fatshape, "FatDate", "DATE")
        arcpy.AddField_management(fatshape, "SpName", "STRING")
        arcpy.AddField_management(fatshape, "SiteTurb", "STRING")
        arcpy.AddField_management(fatshape, "Contained", "SHORT")
        
        #Read from CSV to Shapefile
        fat_CSV=open(Fatalities)
        point1 = arcpy.Point()
        for line in fat_CSV.readlines():
            
            #Skip first line
            if "Common" in line:
                continue
            
            linesplit = line.split(",")
            #Set X,Y Coordinates
            point1.X,point1.Y = float(linesplit[3]),float(linesplit[2])
            #Create the shape
            cursor1 = arcpy.da.InsertCursor(fatshape,
                                            ["SHAPE@",
                                             "FatDate",
                                             "SpName",
                                             "SiteTurb"])
            cursor1.insertRow([point1,
                               linesplit[0],
                               linesplit[1],
                               linesplit[5]])
                               
        #Push the shape into memory and close the CSV        
        del cursor1
        fat_CSV.close()

except ExecuteError:
    arcpy.GetMessages()

except:
    arcpy.AddMessage("There has been a nontool error")
    arcpy.GetMessages()
       
