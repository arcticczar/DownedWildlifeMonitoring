# -*- coding: utf-8 -*-
"""
Created on Mon Mar 06 08:23:46 2017

@author: mstelmach
"""
from django import forms
from django.core.exceptions import ValidationError

from .models import (SizeClass, 
                    Status, 
                    SpeciesDef, 
                    Age,
                    PlantSpecies,
                    Direction,
                    Bait,
                    Personnel,
                    Canine,
                    Site,
                    Infrastructure,
                    TrapType,
                    Weather,
                    NightSurvey_Behavior,
                    NightSurvey_Elevation,
                    NightSurvey_Distance,
                    BandColor)

class ScientificNameMixin:
    """check scientific name"""
    def clean_scientific_name(self):
        new_scientific_name = self.cleaned_data['scientific_name']
        if ' ' not in new_scientific_name:
            raise ValidationError( 'Scientific name must include genus and species', code='genus/species')
        return new_scientific_name
    
class CleanLocMixin:
    def clean_loc(self):
        return self.cleaned_data['loc']
        
class LatLonMixin:
    def clean_latitude(self):
        new_lat = self.cleaned_data['latitude']
        try:
            float(new_lat)
            return new_lat
        except:
            raise ValidationError('Latitude must be a number', code='lat#')
            
    def clean_longitude(self):
        new_lon = self.cleaned_data['longitude']
        try:
            float(new_lon)
            return new_lon
        except:
            raise ValidationError('longitude must be a number', code='lon#')


class SizeClassForm(forms.ModelForm):
    class Meta:
        model = SizeClass
        fields = '__all__'
        
    def clean_size_txt(self):
        return self.cleaned_data['size_txt']
        
class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = '__all__'

    def clean_status_txt(self):
        return self.cleaned_data['size_txt']

class SpeciesDefForm(ScientificNameMixin, forms.ModelForm):
    class Meta:
        model = SpeciesDef
        fields = '__all__'
        
    def clean_common_name(self):
        return self.cleaned_data['common_name']
    
    def clean_species_code(self):
        return self.cleaned_data['species_code'].upper()
    
class AgeForm(forms.ModelForm):
    class Meta:
        model = Age
        fields = '__all__'
        
    def clean_age_text(self):
        return self.cleaned_data['age_text']
    
class PlantSpeciesForm(ScientificNameMixin, forms.ModelForm):
    class Meta:
        model = PlantSpecies
        fields = '__all__'
        
    def clean_common_name(self):
        return self.cleaned_data['common_name']
    
    def clean_hawaiian_name(self):
        return self.cleaned_data['hawaiian_name']
        
    def clean_status(self):
        return self.cleaned_data['status']
    
    def clean_family(self):
        return self.cleaned_data['family']
    
    def clean_distribution(self):
        return self.cleaned_data['distribution']
    
    def clean_notes(self):
        return self.cleaned_data['notes']
        
class DirectionForm(forms.ModelForm):
    class Meta:
        model = Direction
        fields = '__all__'
        
    def clean_direction_text(self):
        return self.cleaned_data['direction_text']
    
    def clean_direction_short(self):
        return self.cleaned_data['direction_short']
    
    def clean_direction_deg(self):
        return self.cleaned_data['direction_deg']
    
class BaitForm(forms.ModelForm):
    class Meta:
        model = Bait
        fields = '__all__'
        
    def clean_bait_text(self):
        return self.cleaned_data['bait_text']
    
class PersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = '__all__'
        
    def clean_first_name(self):
        return self.cleaned_data['first_name']
    
    def clean_last_name(self):
        return self.cleaned_data['last_name']
    
    def clean_organization(self):
        return self.cleaned_data['organization']
    
    def clean_initials(self):
        return self.cleaned_data['initals'].upper()
    
    def clean_staff_type(self):
        return self.cleaned_data['staff_type']
    
    def clean_hire_date(self):
        return self.cleaned_data['hire_date']

    def clean_phone(self):
        return self.cleaned_data['phone']
    
    def clean_email(self):
        return self.cleaned_data['email']
    
    def clean_active(self):
        return self.cleaned_data['active']
    
class CanineForm(forms.ModelForm):
    class Meta:
        model = Canine
        fields = '__all__'
        
    def clean_name(self):
        return self.cleaned_data['name']
    
class SiteForm(CleanLocMixin, forms.ModelForm):
    class Meta:
        model = Site
        fields = '__all__'

    
    def clean_locations(self):
        return self.cleaned_data['locations']
    
    def clean_short(self):
        return self.cleaned_data['short']
    
class InfrastructureForm(CleanLocMixin, LatLonMixin, forms.ModelForm):
    class Meta:
        model = Infrastructure
        fields = '__all__'
        
    def clean_name(self):
        return self.cleaned_data['name']
    
    def clean_physical_phase(self):
        return self.cleaned_data['physical_phase']
    
    def clean_phase(self):
        return self.cleaned_data['phase']
    
    def clean_notes(self):
        return self.cleaned_data['notes']
    
    def clean_elevation(self):
        return self.cleaned_data['elevation']
        
class TrapTypeForm(forms.ModelForm):
    class Meta:
        model = TrapType
        fields = '__all__'
        
    def clean_trap_type_text(self):
        return self.cleaned_data['trap_type_text']
    
    def clean_cost(self):
        return self.cleaned_data['cost']
    
    def clean_check_frequency(self):
        return self.cleaned_data['check_frequency']
    
class WeatherForm(forms.ModelForm):
    class Meta:
        model = Weather
        fields = '__all__'
        
        def clean_rain(self):
            return self.cleaned_data['rain']
        
class NightSurvey_BehaviorForm(forms.ModelForm):
    class Meta:
        model = NightSurvey_Behavior
        fields = '__all__'
        
        def clean_behavior(self):
            return self.cleaned_data['behavior']
        
class NightSurvey_ElevationForm(forms.ModelForm):
    class Meta:
        model = NightSurvey_Elevation
        fields = '__all__'
        
        def clean_elevation(self):
            return self.cleaned_data['elevation']
        
class NightSurvey_DistanceForm(forms.ModelForm):
    class Meta:
        model = NightSurvey_Distance
        fields = '__all__'
        
        def clean_distance(self):
            return self.cleaned_data['distance']
        
class BandColorForm(forms.ModelForm):
    class Meta:
        model = BandColor
        fields = '__all__'
        
        def clean_color_text(self):
            return self.cleaned_fields['color_text']

#Random points model excluded, data to be entered through GIS

#Search Area Model excluded, data to be entered through GIS