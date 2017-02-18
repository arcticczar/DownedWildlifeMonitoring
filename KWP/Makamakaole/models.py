from datetime import date

from django.db import models
from django.utils import timezone
from django.contrib.gis.db import models

from lookup_tables.models import PlantSpecies, Site, Direction, SpeciesDef, Personnel
# Create your models here.

enclosure_list = (('A','A'),('B','B') )

class BurrowMonitoring(models.Model):
    monitoring_date = models.DateField(default=timezone.now)
    enclosure = models.CharField(max_length=1, choices = enclosure_list)
    burrow_num = models.PositiveSmallIntegerField()
    toothpick_activity = models.BooleanField(default=False)
    scent_activity = models.BooleanField(default=False)
    burrow_opened = models.BooleanField(default=False)
    feather_activity = models.BooleanField(default=False)
    chick_present = models.BooleanField(default=False)
    nest_material_present = models.BooleanField(default=False)
    ant_activity = models.BooleanField(default=False)
    other_activity = models.BooleanField(default=False)
    notes = models.TextField(null=True,blank=True)

    
    def __str__(self):
        MonitorID = str(enclosure)+str(burrow_num)+str(monitoring_date)
        return self.MonitorID

class FenceCheck(models.Model):
    fence_check_date = models.DateField(default=timezone.now)
    enclosure = models.CharField(max_length=1, choices = enclosure_list)
    culverts_sound = models.BooleanField(default=True)
    fenceline_sound = models.BooleanField(default=True)
    hood_sound = models.BooleanField(default=True)
    gate_sound = models.BooleanField(default=True)
    notes = models.TextField(null=True,blank=True)

    def __str__(self):
        fenceID = str(enclosure)+str(fence_check_date)
        return self.fenceID
    
class SoundCheck(models.Model):
    sound_check_date = models.DateField(default=timezone.now)
    enclosure = models.CharField(max_length=1, choices = enclosure_list)
    battery = models.IntegerField()
    battery2 = models.IntegerField()
    ants = models.BooleanField()

    def __str__(self):
        soundID = str(enclosure)+str(monitoring_date)
        return self.soundID

class GeneralNotes(models.Model):
    note_date = models.DateField(default=timezone.now)
    makamakaole_notes = models.TextField(null=True,blank=True)

class Outplanting(models.Model):
    outplanting_date = models.DateField(default=timezone.now)
    enclosure = models.CharField(max_length=1, choices = enclosure_list)
    plant_species = models.ForeignKey(PlantSpecies, related_name="plants")
    number = models.PositiveIntegerField()
    notes = models.TextField(null=True,blank=True)


class NightSurvey(models.Model):
    survey_date = models.DateField(default=timezone.now)
    start_time = models.TimeField()
    end_time = models.TimeField()
    loc = models.PointField(null=True,blank=True)
    location_coordinates_x = models.DecimalField(max_digits=20, decimal_places=10)
    location_coordinates_y = models.DecimalField(max_digits=20, decimal_places=10)
    location_text = models.ForeignKey(Site, related_name="site")
    sublocation = models.CharField(max_length=100)
    auditory_minutes_surveyed = models.PositiveIntegerField()
    binocular_minutes_surveyed = models.PositiveIntegerField()
    night_vision_minutes_surveyed = models.PositiveIntegerField()
    observer1 = models.OneToOneField(Personnel, related_name='first')
    observer2 = models.OneToOneField(Personnel, related_name='second')
    cloud_cover = models.PositiveIntegerField()
    wind_speed = models.PositiveIntegerField()
    wind_dir = models.ForeignKey(Direction, related_name="dir")
    precipitation = models.PositiveIntegerField()
    survey_quality = models.PositiveIntegerField()
    visibility = models.PositiveIntegerField()
    ceiling = models.PositiveIntegerField()
    comments = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.survey_date

elevation = (('Above','Above'),('Below','Below'),('Same','Same') )
behavior = (('transit', 'Transit'),('Circling','Circling'))

class NightSurveyObservations(models.Model):
    parent_survey = models.ForeignKey(NightSurvey, related_name="night_survey")
    observation_time = models.TimeField()
    species = models.ForeignKey(SpeciesDef, related_name="species_def")
    count = models.PositiveIntegerField()
    quadrat = models.PositiveIntegerField()
    elevation = models.CharField(max_length=20, choices = elevation)
    behavior = models.CharField(max_length=20, choices = behavior)
    flight_direction = models.ForeignKey(Direction, related_name="direction")
    notes = models.TextField(null=True,blank=True)
    
class BANOControl(models.Model):
    control_date = models.DateField(default = timezone.now)
    staff1 = models.ForeignKey(Personnel, related_name="obs1")
    staff2 = models.ForeignKey(Personnel, related_name="obs2")
    start_time = models.TimeField()
    end_time = models.TimeField(default= timezone.now)
    loc = models.PointField(null=True,blank=True)
    BANO_observerd = models.PositiveIntegerField()
    BANO_controlled = models.PositiveIntegerField()
    notes = models.TextField(null=True,blank=True)

