# -*- coding: utf-8 -*-
"""
Created on Tue Mar 07 08:33:14 2017

@author: mstelmach
"""

'''
Lookup tables are created to be modified rarely if ever.
Models here will be referenced by data in other apps.
'''

from django.db import models
from django.contrib.gis.db import models
from django.shortcuts import reverse

# define relative wildlife size classes
class SizeClass(models.Model):
    size_txt = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.size_txt
    
    def get_absolute_url(self):
        return reverse('sizeclass_detail', kwargs={'size_txt':self.size_txt})
    
    def get_post_url(self):
        pass
    
    def get_modify_url(self):
        pass
    
    def get_delete_url(self):
        pass

#list federal and state status.
class Status(models.Model):
    status_txt = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.status_txt
    
    def get_absolute_url(self):
        return reverse('status_detail', kwargs={'status_txt':self.status_txt})
    
#species information for all wildlife
class SpeciesDef(models.Model):
    common_name=models.CharField(max_length=200)
    scientific_name=models.CharField(max_length=200)
    species_code=models.CharField(max_length=10)
    species_status=models.ForeignKey(Status) #get status from status model
    size_class=models.ForeignKey(SizeClass) #get size from sizeclass model

    def __str__(self):
        return self.common_name
    
    def get_absolute_url(self):
        return reverse('speciesdef_detail', kwargs={'species_code':self.species_code})

#relative age
class Age(models.Model):
    age_text = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.age_text
    
    def get_absolute_url(self):
        return reverse('age_detail', kwargs={'age':self.age_text})

#Species information for plants to use in outplanting and weed control
class PlantSpecies(models.Model):
    common_name = models.CharField(max_length=200)
    hawaiian_name = models.CharField(max_length=200)
    scientific_name = models.CharField(max_length=200, unique=True)
    status = models.CharField(max_length=200)
    family = models.CharField(max_length=200)
    distribution = models.CharField(max_length=200)
    notes = models.CharField(max_length=200, null=True,blank=True)

    def __str__(self):
        return self.scientific_name
    
    def get_absolute_url(self):
        return reverse('age_detail', kwargs={'common_name':self.common_name})

#Cardinal directions for use with compass bearings
class Direction(models.Model):
    direction_text = models.CharField(max_length=50, unique=True)
    direction_short = models.CharField(max_length=2)
    direction_deg = models.IntegerField()

    def __str__(self):
        return self.direction_text
    
    def get_absolute_url(self):
        return reverse('direction_detail', kwargs={'direction_short':self.direction_short})

#Bait used for trapping
class Bait(models.Model):
    bait_text=models.CharField(max_length=200, unique=True)
    

    def __str__(self):
        return self.bait_text
    
    def get_absolute_url(self):
        return reverse('bait_detail', kwargs={'bait_text': self.bait_text.replace(' ','')})

#All personnel related to site activity
class Personnel(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    initials = models.CharField(max_length=20, unique=True)
    staff_type = models.CharField(max_length=50)
    hire_date = models.DateField( null=True, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    active = models.BooleanField()

    def __str__(self):
        return self.first_name +' ' + self.last_name
    
    def get_absolute_url(self):
        return reverse('personnel_detail', kwargs={'model':'Personnel', 'instance':self.initials})

#Canine searchers
class Canine(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return (reverse('canine_detail', kwargs={'name':self.name}))

#General locations where activity occurs
class Site(models.Model):
    loc = models.MultiPolygonField(null=True,blank=True) #Defines general area
    locations = models.CharField(max_length=200, unique=True)
    short = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.locations
    
    def get_absolute_url(self):
        return reverse('site_detail', kwargs={'site':self.locations})

#On Site infrastructure buildings and sites of importance
class Infrastructure(models.Model):
    loc = models.PointField(null=True,blank=True) #point location for buildings
    name = models.CharField(max_length=200)
    physical_phase = models.ForeignKey(Site, related_name='geographic_location')
    phase = models.ForeignKey(Site, related_name='owner')
    notes = models.TextField( null=True, blank=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
    elevation = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)

    def __str__(self):
        return self.phase.short +'-'+ self.name
    
    def get_absolute_url(self):
        return reverse('infrastructure', kwargs={'phase':self.phase, 'name':self.name})

class TrapType(models.Model):
    trap_type_text = models.CharField(max_length=200, unique=True)
    cost = models.CharField(max_length=200)
    check_frequency = models.IntegerField()
    

    def __str__(self):
        return self.trap_type_text
    
    def get_absolute_url(self):
        return reverse('traptype_detail', kwargs={'trap_type_text':self.trap_type_text})

class Weather(models.Model):
    rain = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.rain
    
    def get_absolute_url(self):
        return reverse('weather_detail', kwargs={'rain':self.rain})

class NightSurvey_Behavior(models.Model):
    behavior = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.behavior
    
    def get_absolute_url(self):
        return reverse('nightsurvey_behavior_detail', kwargs={'behavior':self.behavior})

class NightSurvey_Elevation(models.Model):
    elevation = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.elevation
    
    def get_absolute_url(self):
        return reverse('nightsurvey_elevation_detail', kwargs={'elevation':self.elevation})

class NightSurvey_Distance(models.Model):
    distance_range = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.distance_range
    
    def get_absolute_url(self):
        return reverse('site_detail', kwargs={'site':self.locations})

class BandColor(models.Model):
    color_text = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.color_text

class RandomPoints(models.Model):
    point_id = models.AutoField(primary_key=True, unique=True)
    loc = models.PointField(null=True,blank=True)
    phase = models.ForeignKey(Site)
    near = models.ForeignKey(Infrastructure)
    notes = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.point_id

class SearchArea(models.Model):
    loc = models.MultiPolygonField()
    site = models.ForeignKey(Site)
    turbine = models.ForeignKey(Infrastructure)
    from_0_to_10 = models.DecimalField(max_digits=20, decimal_places=10, null=True,blank=True)
    from_10_to_20 = models.DecimalField(max_digits=20, decimal_places=10, null=True,blank=True)
    from_20_to_30 = models.DecimalField(max_digits=20, decimal_places=10, null=True,blank=True)
    from_30_to_40 = models.DecimalField(max_digits=20, decimal_places=10, null=True,blank=True)
    from_40_to_50 = models.DecimalField(max_digits=20, decimal_places=10, null=True,blank=True)
    from_50_to_60 = models.DecimalField(max_digits=20, decimal_places=10, null=True,blank=True)
    from_60_to_70 = models.DecimalField(max_digits=20, decimal_places=10, null=True,blank=True)
    from_70_to_80 = models.DecimalField(max_digits=20, decimal_places=10, null=True,blank=True)
    total_searchable = models.DecimalField(max_digits=20, decimal_places=10, null=True,blank=True)
    notes = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.site.short+'-'+self.turbine.name