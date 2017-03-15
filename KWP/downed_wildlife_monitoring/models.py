# -*- coding: utf-8 -*-
"""
Created on Tue Mar 07 08:32:18 2017

@author: mstelmach
"""

from datetime import datetime


from django.db import models
from django.utils import timezone

from django.contrib.gis.db import models


from lookup_tables.models import (Personnel,
                                    Canine,
                                    Age,
                                    Infrastructure,
                                    Direction,
                                    Weather,
                                    SpeciesDef,
                                    Site,
                                    BandColor,
                                    RandomPoints)

SearchType = (('Visual','Visual'),('Canine','Canine'))
SearchIncidental = (('Search','Search'),('Incidental','Incidental'))
Sex = (('Male','Male'),('Female','Female'),('Unknown','Unknown'))
Condition = (('Alive','Alive'),('Dead','Dead'))

#record a downed wildlife incident
class DownedWildlifeMonitoring(models.Model):
    IDKey = models.CharField(null=True, blank=True, max_length=50)
    loc = models.PointField(null=True,blank=True)
    discovery_date = models.DateField(default=timezone.now)
    discovered_by = models.ForeignKey(Personnel, related_name='discover')
    search_type = models.CharField(max_length=20, choices= SearchType) #Visual or Canine
    search_incidental = models.CharField(max_length=20, choices=SearchIncidental)
    affiliation = models.CharField(max_length=50)
    canine_searcher = models.ForeignKey(Canine, null=True,blank=True)
    species = models.ForeignKey(SpeciesDef)
    age = models.ForeignKey(Age)
    sex = models.CharField(max_length=50,choices=Sex)
    time_discovered = models.TimeField(default=timezone.now)
    location_description = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=20, decimal_places=10)
    longitude = models.DecimalField(max_digits=20, decimal_places=10)
    site = models.ForeignKey(Site)
    turbine = models.ForeignKey(Infrastructure)
    distance = models.DecimalField(max_digits = 10, decimal_places=2)
    bearing = models.PositiveIntegerField()
    ground_cover = models.CharField(max_length = 200)
    wind_dir = models.ForeignKey(Direction)
    wind_speed = models.PositiveIntegerField(help_text="Meters per second") 
    cloud_cover = models.PositiveIntegerField(help_text="Percent")
    cloud_deck = models.CharField(max_length=50)
    precip = models.ForeignKey(Weather)
    temp = models.PositiveIntegerField(help_text="degrees fahrenheit")
    animal_condition = models.CharField(max_length =20, choices = Condition)
    description = models.TextField(help_text="describe the carcass: injuries, fat, condition, etc...")
    collected_by = models.ForeignKey(Personnel, related_name='collected')
    photo_structure = models.ImageField(null=True,blank=True, help_text="Photo relative to the structure")
    photo_as_found = models.ImageField(null=True,blank=True, help_text="Photo of the carcass from just above")
    photo_as_found2 = models.ImageField(null=True,blank=True, help_text="Photo of the carcass opposite side")
    photo_injury = models.ImageField(null=True,blank=True, help_text="Close up of animal injury")
    photo_other = models.ImageField(null=True,blank=True, help_text="Additional photo if needed")
    notes = models.TextField(null=True,blank=True)
    report_date = models.DateField(default=timezone.now, null=True, blank=True)
    time_reported = models.DateTimeField(null=True,blank=True, help_text="What time were the agencies first notified")
    time_responded = models.DateTimeField(null=True,blank=True, help_text="What time did the agencies respond")
    time_collected = models.DateTimeField(null=True,blank=True, help_text="What time was the specimen collected")
    date_last_searched = models.DateField(null=True,blank=True, help_text="The date of the last monitoring")
    weather_TOD = models.CharField(default='unknown',max_length=200, null=True, blank=True)
    outside = models.BooleanField()

    #Define a unique ID based on standard values format YYYYMMDD_SITE_Turbine_Species Code
    def IDcode(self):
        #fmt = '%Y-%M-%d'
        out = '%Y%m%d'
        disco_date = self.discovery_date.strftime(out)

        try:
            sublocation = 'T'+str(int(self.turbine.name))
        except:
            sublocation = self.turbine.name
            
        output = (disco_date
            +'_'
            +self.site.short
            +'_'
            +sublocation
            +'_'
            +self.species.species_code)
        
        return output
    
    def __str__(self):
        return self.IDcode()

#Actions taken as a subreport of Downed Wildlife Monitoring.  Should include:
#Initial observation, collection, and reporting
class ActionsTaken(models.Model):
    parent = models.ForeignKey(DownedWildlifeMonitoring)
    event_time = models.DateTimeField()
    action = models.TextField()

    def __str__(self):
        return self.parent.ID()+'-'+self.event_time

#KWP nene survey for each phase.
class NeneSurvey(models.Model):
    date = models.DateField(default=timezone.now)
    site = models.ForeignKey(Site)
    start_time =models.TimeField()
    end_time = models.TimeField()
    observer = models.ForeignKey(Personnel)
    count = models.PositiveIntegerField(help_text="Total number of Nene observed")
    notes = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.date) +'-'+ self.site.short

#Day 0 initial set-up of carcass retention studies.
class CareSetUp(models.Model):
    loc = models.PointField(null=True,blank=True)
    trial = models.CharField(max_length=3, help_text="trial ID, unique for each CARE trial")
    carcass_number = models.PositiveIntegerField(help_text="sequential number for each carcass in trial")
    start_date = models.DateField(default = timezone.now)
    carcass_type = models.ForeignKey(SpeciesDef)
    distance = models.PositiveIntegerField(help_text="distance in meters from the turbine")
    direction = models.PositiveIntegerField(help_text="bearing from the turbine to the CARE location")
    latitude = models.DecimalField(max_digits=20, decimal_places=10)
    longitude = models.DecimalField(max_digits=20, decimal_places=10)
    site = models.ForeignKey(Site)
    turbine = models.ForeignKey(Infrastructure)
    vegetation = models.CharField(max_length=50, help_text="relative vegetation height")
    waypoint = models.ForeignKey(RandomPoints, related_name="CARE_waypoint")
    photo = models.ImageField()
    notes = models.TextField(null=True,blank=True)
    observer = models.ForeignKey(Personnel)

    class Meta:
        ordering = ['-start_date']
        get_latest_by = "start_date"

    def __str__(self):
        return str(self.trial)+str(self.carcass_number)

CarcassStatus = (('Intact','Intact'),
                 ('Scavenged', 'Scavenged'),
                 ('Odor','Odor'),
                 ('Moved','Moved'),
                 ('Feather/Hair loss', 'Feather/Hair loss'),
                 ('Feather/Hair pile','feather/hair pile'),
                 ('Ants','Ants'),
                 ('Beetles','Beetles'),
                 ('Flies','Flies'),
                 ('Larvae','Larvae'),
                 ('Skeleton visible','Skeleton visible'),
                 ('Skeleton only','Skeleton only'),
                 ('Dessicated', 'Dessicated'),
                 ('Gone','Gone'),
                 ('Other (notes)', 'Other (notes)'))

                 
#Continued Monitoring of Carcass Retention
class CareMonitoring(models.Model):
    parent = models.ForeignKey(CareSetUp, help_text="Related to CARE Setup ID")
    loc = models.PointField(null=True,blank=True)
    monitor_date = models.DateField(default=timezone.now)
    present = models.BooleanField(help_text="True if present")
    latitude = models.DecimalField(max_digits=20, decimal_places=10)
    longitude = models.DecimalField(max_digits=20, decimal_places=10)
    condition = models.CharField(max_length=255, choices=CarcassStatus)
    photo = models.ImageField()
    notes = models.TextField(null=True,blank=True)
    observer = models.ForeignKey(Personnel)

    def __str__(self):
        return self.parent.trial+self.parent.carcass_number+'_'+str(self.monitor_date)

#KWP Phase I searching one entry per search day per person.
class KWPISearching(models.Model):
    monitor_date = models.DateField(default=timezone.now)
    observer = models.ForeignKey(Personnel)
    search_type = models.CharField(max_length=20, choices=SearchType)
    temp = models.PositiveIntegerField(help_text="degrees fahrenheit")
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2, help_text="meters per second")
    wind_dir = models.ForeignKey(Direction, help_text="direction wind is blowing from(NE for trades)")
    cloud_cover = models.PositiveIntegerField(help_text="percent")
    precip = models.ForeignKey(Weather)
    start_time = models.TimeField()
    t1 = models.BooleanField()
    t2 = models.BooleanField()
    t3 = models.BooleanField()
    t4 = models.BooleanField()
    t5 = models.BooleanField()
    t6 = models.BooleanField()
    t7 = models.BooleanField()
    t8 = models.BooleanField()
    t9 = models.BooleanField()
    t10 = models.BooleanField()
    t11 = models.BooleanField()
    t12 = models.BooleanField()
    t13 = models.BooleanField()
    t14 = models.BooleanField()
    t15 = models.BooleanField()
    t16 = models.BooleanField()
    t17 = models.BooleanField()
    t18 = models.BooleanField()
    t19 = models.BooleanField()
    t20 = models.BooleanField()
    end_time = models.TimeField()
    notes = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.monitor_date)

#KWP Phase II searching one entry per search day per person.
class KWPIISearching(models.Model):
    monitor_date = models.DateField(default=timezone.now)
    observer = models.ForeignKey(Personnel)
    search_type = models.CharField(max_length=20, choices=SearchType)
    temp = models.PositiveIntegerField(help_text="degrees fahrenheit")
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2, help_text="meters per second")
    wind_dir = models.ForeignKey(Direction, help_text="direction wind is blowing from(NE for trades)")
    cloud_cover = models.PositiveIntegerField()
    precip = models.ForeignKey(Weather)
    start_time = models.TimeField()
    t1 = models.BooleanField()
    t2 = models.BooleanField()
    t3 = models.BooleanField()
    t4 = models.BooleanField()
    t5 = models.BooleanField()
    t6 = models.BooleanField()
    t7 = models.BooleanField()
    t8 = models.BooleanField()
    t9 = models.BooleanField()
    t10 = models.BooleanField()
    t11 = models.BooleanField()
    t12 = models.BooleanField()
    t13 = models.BooleanField()
    t14 = models.BooleanField()
    end_time = models.TimeField()
    notes = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.monitor_date)

#Searcher Efficiency Trial monitoring data
class SEEFMaster(models.Model):
    loc = models.PointField(null=True,blank=True)
    trial_date = models.DateField()
    site = models.ForeignKey(Site)
    turbine = models.ForeignKey(Infrastructure)
    species = models.ForeignKey(SpeciesDef)
    found = models.NullBooleanField()
    not_recovered = models.NullBooleanField()
    latitude = models.DecimalField(max_digits=20, decimal_places=10)
    longitude = models.DecimalField(max_digits=20, decimal_places=10)
    distance = models.DecimalField(max_digits=6, decimal_places=2)
    point_id = models.ForeignKey(RandomPoints)
    searcher = models.ForeignKey(Personnel, related_name='searcher', null=True,blank=True)
    canine = models.ForeignKey(Canine, null=True,blank=True)
    veg_type = models.CharField(max_length=50)
    proctor = models.ForeignKey(Personnel, related_name='proctor')
    notes = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.trial_date)+self.site.short+self.turbine.name+self.point_id.point_id

#Class for searcher reporing of SEEF Results
class SEEFReporting(models.Model):
	trial_date = models.DateField(default = timezone.now)
	turbine = models.ForeignKey(Infrastructure)
	species = models.ForeignKey(SpeciesDef)
	loc = models.PointField(null=True,blank=True)
	notes = models.TextField(null=True,blank=True)

	

DetType = (('Ground','Ground'),('Nacelle','Nacelle'))

#Collecting data associated with changing wildlife acoustics cards.
class WACardSwap(models.Model):
    swap_date = models.DateField(default=timezone.now)
    site = models.ForeignKey(Site)
    turbine = models.ForeignKey(Infrastructure)
    detector_type = models.CharField(max_length = 50, choices=DetType)
    firmware = models.CharField(max_length=20)
    battery = models.DecimalField(max_digits=6, decimal_places=2)
    mic = models.DecimalField(max_digits=6, decimal_places=2)
    mem_card1 = models.BooleanField()
    memory_card1 = models.PositiveIntegerField()
    mem_card2 = models.BooleanField()
    memory_card2 = models.PositiveIntegerField()
    mem_card3 = models.BooleanField()
    memory_card3 = models.PositiveIntegerField()
    mem_card4 = models.BooleanField()
    memory_card4 = models.PositiveIntegerField()
    cables_connected = models.BooleanField()
    unit_time_correct = models.BooleanField()
    notes = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.swap_date)+str(self.site)+str(self.turbine)+str(self.detector_type)

Behavior = (('Standing','Standing'),
            ('Feeding','Feeding'),
            ('Flying','Flying'),
            ('Sitting','Roosting'),
            ('Foraging','Foraging'),
            ('Roosting','Roosting'),
            ('Other','Other'))
YesNo = (('Yes','Yes'),
         ('No', 'No'),
         ('None','None'),
         ('Unknown','Unknown'))
RightLeft = (('Right','Right'),
             ('Left','Left'),
             ('None','None'),
             ('Unknown','Unknown'))

#incidental wildlife observations
class WEOP(models.Model):
    obs_date = models.DateField(default=timezone.now)
    obs_time = models.TimeField(auto_now_add=True, blank=True)
    site = models.ForeignKey(Site)
    turbine = models.ForeignKey(Infrastructure)
    species = models.ForeignKey(SpeciesDef)
    number = models.PositiveIntegerField()
    banded = models.CharField(max_length=20, choices=YesNo)
    color_band_leg = models.CharField(max_length=20, choices=YesNo)
    primary_band_color = models.ForeignKey(BandColor, related_name='Primary', default='Yellow')
    secondary_band_color = models.ForeignKey(BandColor, related_name='Secondary', default='Black')
    color_band_id = models.CharField(max_length=5)
    usgs_band = models.CharField(max_length=20, choices=RightLeft)
    behavior = models.CharField(max_length=20, choices=Behavior)
    flight_dir = models.ForeignKey(Direction, related_name='flight')
    flight_altitude = models.PositiveIntegerField()
    wind_speed = models.DecimalField(max_digits=6, decimal_places=2)
    wind_dir = models.ForeignKey(Direction, related_name='wind')
    cloud_cover = models.PositiveIntegerField()
    precip = models.ForeignKey(Weather)
    observer = models.ForeignKey(Personnel)
    notes = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.obs_date)+str(self.obs_time)+str(self.species)
