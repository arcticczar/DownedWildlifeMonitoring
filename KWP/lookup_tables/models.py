from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class SizeClass(models.Model):
    size_txt = models.CharField(max_length=50)

    def __str__(self):
        return self.size_txt

class Status(models.Model):
    status_txt = models.CharField(max_length=50)

    def __str__(self):
        return self.status_txt
    

class SpeciesDef(models.Model):
    common_name=models.CharField(max_length=200)
    scientific_name=models.CharField(max_length=200)
    species_code=models.CharField(max_length=10)
    species_status=models.ForeignKey(Status, on_delete=models.CASCADE)
    size_class=models.ForeignKey(SizeClass, on_delete=models.CASCADE)

    def __str__(self):
        return self.common_name

class Age(models.Model):
    age_text = models.CharField(max_length=200)

    def __str__(self):
        return self.age_text
    

class PlantSpecies(models.Model):
    common_name = models.CharField(max_length=200)
    hawaiian_name = models.CharField(max_length=200)
    scientific_name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    family = models.CharField(max_length=200)
    distribution = models.CharField(max_length=200)
    notes = models.CharField(max_length=200, null=True,blank=True)

    def __str__(self):
        return self.scientific_name

class Direction(models.Model):
    direction_text = models.CharField(max_length=50)
    direction_short = models.CharField(max_length=2)
    direction_deg = models.IntegerField()

    def __str__(self):
        return self.direction_text

class Bait(models.Model):
    bait_text=models.CharField(max_length=200)
    target_species=models.ManyToManyField(SpeciesDef)

    def __str__(self):
        return self.bait_text

class Personnel(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    initials = models.CharField(max_length=20)
    staff_type = models.CharField(max_length=50)
    hire_date = models.DateField()
    active = models.BooleanField()

    def __str__(self):
        return self.first_name +' ' + self.last_name

class Canine(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Site(models.Model):
    loc = models.PolygonField(null=True,blank=True)
    locations = models.CharField(max_length=200)
    short = models.CharField(max_length=20)

    def __str__(self):
        return self.locations

class Infrastructure(models.Model):
    loc = models.PointField(null=True,blank=True)
    name = models.CharField(max_length=200)
    physical_phase = models.ForeignKey(Site, related_name='geographic_location')
    phase = models.ForeignKey(Site, related_name='owner')
    notes = models.TextField()
    latitude = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)

    def __str__(self):
        return str(self.phase) + self.name

class TrapType(models.Model):
    trap_type_text = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)
    check_frequency = models.IntegerField()
    target_species=models.ManyToManyField(SpeciesDef)

    def __str__(self):
        return self.trap_type_text

class Weather(models.Model):
    rain = models.CharField(max_length=200)

    def __str__(self):
        return self.rain

class NightSurvey_Behavior(models.Model):
    behavior = models.CharField(max_length=200)

    def __str__(self):
        return self.behavior

class NightSurvey_Elevation(models.Model):
    elevation = models.CharField(max_length=200)

    def __str__(self):
        return self.elevation

class NightSurvey_Distance(models.Model):
    distance_range = models.CharField(max_length=200)

    def __str__(self):
        return self.distance_range

class BandColor(models.Model):
    color_text = models.CharField(max_length=50)

    def __str__(self):
        return self.color_text

class RandomPoints(models.Model):
    point_id = models.AutoField(primary_key=True)
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
    to_10 = models.DecimalField(max_digits=20, decimal_places=10)
    to_20 = models.DecimalField(max_digits=20, decimal_places=10)
    to_30 = models.DecimalField(max_digits=20, decimal_places=10)
    to_40 = models.DecimalField(max_digits=20, decimal_places=10)
    to_50 = models.DecimalField(max_digits=20, decimal_places=10)
    to_60 = models.DecimalField(max_digits=20, decimal_places=10)
    to_70 = models.DecimalField(max_digits=20, decimal_places=10)
    to_80 = models.DecimalField(max_digits=20, decimal_places=10)
    total_searchable = models.DecimalField(max_digits=20, decimal_places=10)
    notes = models.TextField(null=True,blank=True)

