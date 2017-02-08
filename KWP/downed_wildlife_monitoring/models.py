from datetime import date, datetime

from django.db import models

from lookup_tables.models import *

SearchType = (('Visual','Visual'),('Canine','Canine'))
SearchIncidental = (('Search','Search'),('Incidental','Incidental'))
Sex = (('Male','Male'),('Female','Female'),('Unknown','Unknown'))
Condition = (('Alive','Alive'),('Dead','Dead'))

# Create your models here.
class DownedWildlifeMonitoring(models.Model):
    discovery_date = models.DateField(default=date.today)
    discovered_by = models.ForeignKey(Personnel, related_name='discover')
    search_type = models.CharField(max_length=20, choices= SearchType)
    search_incidental = models.CharField(max_length=20, choices=SearchIncidental)
    affiliation = models.CharField(max_length=50)
    canine_searcher = models.ForeignKey(Canine)
    species = models.ForeignKey(SpeciesDef)
    age = models.ForeignKey(Age)
    sex = models.CharField(max_length=50,choices=Sex)
    time_discovered = models.TimeField()
    location_description = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=20, decimal_places=10)
    longitude = models.DecimalField(max_digits=20, decimal_places=10)
    site = models.ForeignKey(Site)
    turbine = models.ForeignKey(Infrastructure)
    distance = models.DecimalField(max_digits = 10, decimal_places=2)
    bearing = models.PositiveIntegerField()
    ground_cover = models.CharField(max_length = 200)
    wind_dir = models.ForeignKey(Direction)
    wind_speed = models.PositiveIntegerField()
    cloud_cover = models.PositiveIntegerField()
    cloud_deck = models.CharField(max_length=50)
    precip = models.ForeignKey(Weather)
    temp = models.PositiveIntegerField()
    animal_condition = models.CharField(max_length =20, choices = Condition)
    description = models.TextField()
    collected_by = models.ForeignKey(Personnel, related_name='collected')
    photo_structure = models.ImageField()
    photo_as_found = models.ImageField()
    photo_as_found2 = models.ImageField()
    photo_injury = models.ImageField()
    photo_other = models.ImageField()
    notes = models.TextField()
    report_date = models.DateField()
    time_reported = models.DateTimeField()
    time_responded = models.DateTimeField()
    time_collected = models.DateTimeField()
    date_last_searched = models.DateField()
    weather_TOD = models.CharField(max_length=200)
    outside = models.BooleanField()

    def ID(self):
        return (self.discovery_date.year+self.discovery_date.month+self.discovery_date.day+'_'+self.site+_+'T'+self.turbine+self.species)
    
    def __str__(self):
        return self.ID

class ActionsTaken(models.Model):
    parent = models.ForeignKey(DownedWildlifeMonitoring)
    event_time = models.DateTimeField()
    action = models.TextField()

class NeneSurvey(models.Model):
    date = models.DateField(default=date.today)
    site = models.ForeignKey(Site)
    start_time =models.TimeField()
    end_time = models.TimeField()
    observer = models.ForeignKey(Personnel)
    count = models.PositiveIntegerField()
    notes = models.TextField()

    def __str__(self):
        return str(self.date) + str(self.site)

class CareSetUp(models.Model):
    trial = models.CharField(max_length=3)
    carcass_number = models.PositiveIntegerField()
    start_date = models.DateField(default = date.today)
    carcass_type = models.ForeignKey(SpeciesDef)
    distance = models.PositiveIntegerField()
    direction = models.PositiveIntegerField()
    latitude = models.DecimalField(max_digits=20, decimal_places=10)
    longitude = models.DecimalField(max_digits=20, decimal_places=10)
    site = models.ForeignKey(Site)
    turbine = models.ForeignKey(Infrastructure)
    vegetation = models.CharField(max_length=50)
    waypoint = models.PositiveIntegerField()
    photo = models.ImageField()
    notes = models.TextField()
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

                 

class CareMonitoring(models.Model):
    parent = models.ForeignKey(CareSetUp)
    monitor_date = models.DateField(default=date.today)
    present = models.BooleanField()
    latitude = models.DecimalField(max_digits=20, decimal_places=10)
    longitude = models.DecimalField(max_digits=20, decimal_places=10)
    condition = models.CharField(max_length=255, choices=CarcassStatus)
    photo = models.ImageField()
    notes = models.TextField()
    observer = models.ForeignKey(Personnel)

    def __str__(self):
        return str(self.parent)+str(self.monitor_date)

class KWPISearching(models.Model):
    monitor_date = models.DateField(default=date.today)
    observer = models.ForeignKey(Personnel)
    search_type = models.CharField(max_length=20, choices=SearchType)
    temp = models.PositiveIntegerField()
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2)
    wind_dir = models.ForeignKey(Direction)
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
    t15 = models.BooleanField()
    t16 = models.BooleanField()
    t17 = models.BooleanField()
    t18 = models.BooleanField()
    t19 = models.BooleanField()
    t20 = models.BooleanField()
    end_time = models.TimeField()
    notes = models.TextField()

    def __str__(self):
        return str(self.monitor_date)

class KWPIISearching(models.Model):
    monitor_date = models.DateField(default=date.today)
    observer = models.ForeignKey(Personnel)
    search_type = models.CharField(max_length=20, choices=SearchType)
    temp = models.PositiveIntegerField()
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2)
    wind_dir = models.ForeignKey(Direction)
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
    notes = models.TextField()

    def __str__(self):
        return str(self.monitor_date)
        
class SEEFMaster(models.Model):
    trial_date = models.DateField()
    site = models.ForeignKey(Site)
    turbine = models.ForeignKey(Infrastructure)
    species = models.ForeignKey(SpeciesDef)
    found = models.BooleanField()
    not_recovered = models.BooleanField()
    latitude = models.DecimalField(max_digits=20, decimal_places=10)
    longitude = models.DecimalField(max_digits=20, decimal_places=10)
    distance = models.DecimalField(max_digits=6, decimal_places=2)
    point_id = models.PositiveIntegerField()
    searcher = models.ForeignKey(Personnel, related_name='searcher')
    canine = models.ForeignKey(Canine)
    veg_type = models.CharField(max_length=50)
    proctor = models.ForeignKey(Personnel, related_name='proctor')
    notes = models.TextField

    def __str__(self):
        return str(self.trial_date)+str(self.site)+str(self.turbine)+str(self.point_id)

DetType = (('Ground','Ground'),('Nacelle','Nacelle'))

class WACardSwap(models.Model):
    swap_date = models.DateField(default=date.today)
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
    notes = models.TextField()

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


class WEOP(models.Model):
    obs_date = models.DateField(default=date.today)
    obs_time = models.TimeField(default=datetime.now())
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

    def __str__(self):
        return str(self.obs_date)+str(self.obs_time)+str(self.species)
