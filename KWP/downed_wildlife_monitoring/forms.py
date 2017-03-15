# -*- coding: utf-8 -*-
"""
Created on Tue Mar 07 08:35:37 2017

@author: mstelmach
"""

from django import forms
from django.core.exceptions import ValidationError

from .models import (DownedWildlifeMonitoring,
                     ActionsTaken,
                     NeneSurvey,
                     CareSetUp,
                     CareMonitoring,
                     KWPISearching,
                     KWPIISearching,
                     SEEFMaster,
                     SEEFReporting,
                     WACardSwap,
                     WEOP)
###################### Mixin Models ############################

#Create methods for validating latitude and longitude.
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

#Create location for all forms            
class CleanLocMixin:
    def clean_loc(self):
        return self.cleaned_data['loc']
    
class CleanSiteMixin:
    def clean_site(self):
        return self.cleaned_data['site']
    
class CleanTurbineMixin:
    def clean_infrastructure(self):
        return self.cleaned_data['turbine']
    
class CleanDistanceMixin:
    def clean_distance(self):
        return self.cleaned_data['distance']
    
class CleanWeatherMixin:
    def clean_wind_speed(self):
        return self.cleaned_data['wind_speed']
    
    def clean_wind_dir(self):
        return self.cleaned_data['wind_dir']
    
    def clean_cloud_cover(self):
        return self.cleaned_data['cloud_cover']

class CleanNotesMixin:
    def clean_notes(self):
        return self.cleaned_data['notes']

#Start and end times for searches and surveys    
class CleanTimeMixin:
    def clean_start_time(self):
        return self.cleaned_data['start_time']
    
    def clean_end_time(self):
        return self.cleaned_data['end_time']

class CleanObserverMixin:
    def clean_observer(self):
        return self.cleaned_data['observer']
    
class CleanParentMixin:
    def clean_parent(self):
        return self.cleaned_data('parent')
    
class CleanPhotoMixin:
    def clean_photo(self):
        return self.cleaned_data['photo']

class CleanTempMixin:
    def clean_temp(self):
        return self.cleaned_data['temp']
    
class CleanSearchTypeMixin:
    def clean_search_type(self):
        return self.cleaned_data['search_type']
    
class MonitorDateMixin:
    def clean_monitor_date(self):
        return self.cleaned_data['monitor_date']
    
class CleanPrecipMixin:
    def clean_precip(self):
        return self.cleaned_data['precip']
    
class Clean14Mixin:
    def clean_t1(self):
        return self.cleaned_data['t1']
    
    def clean_t2(self):
        return self.cleaned_data['t2']
    
    def clean_t3(self):
        return self.cleaned_data['t3']
    
    def clean_t4(self):
        return self.cleaned_data['t4']
    
    def clean_t5(self):
        return self.cleaned_data['t5']
    
    def clean_t6(self):
        return self.cleaned_data['t6']
    
    def clean_t7(self):
        return self.cleaned_data['t7']
    
    def clean_t8(self):
        return self.cleaned_data['t8']
    
    def clean_t9(self):
        return self.cleaned_data['t9']
    
    def clean_t10(self):
        return self.cleaned_data['t10']
    
    def clean_t11(self):
        return self.cleaned_data['t11']
    
    def clean_t12(self):
        return self.cleaned_data['t12']
    
    def clean_t13(self):
        return self.cleaned_data['t13']
    
    def clean_t14(self):
        return self.cleaned_data['t14']
    
class CleanSpeciesMixin:
    def clean_species(self):
        return self.cleaned_data['species']
    
class CleanTrialDateMixin:
    def clean_trial_date(self):
        return self.cleaned_data['trial_date']

################### Forms ##############################

class DownedWildlifeForm(CleanNotesMixin,
                         CleanWeatherMixin,
                         CleanTempMixin,
                         CleanDistanceMixin,
                         CleanTurbineMixin, 
                         CleanSiteMixin, 
                         CleanLocMixin, 
                         LatLonMixin, 
                         CleanSearchTypeMixin,
                         CleanPrecipMixin,
                         CleanSpeciesMixin,
                         forms.ModelForm):
    class Meta:
        model = DownedWildlifeMonitoring
        fields = '__all__'
        
    def clean_discovery_date(self):
        return self.cleaned_data['discovery_date']
    
    def clean_discovered_by(self):
        return self.cleaned_data['discovered_by']
    
    def clean_search_incidental(self):
        return self.cleaned_data['search_incidental']
    
    def clean_affiliation(self):
        return self.cleaned_data['affiliation']
    
    def clean_canine_searcher(self):
        return self.cleaned_data['canine_searcher']
    
    def clean_age(self):
        return self.cleaned_data['age']
    
    def clean_sex(self):
        return self.cleaned_data['sex']
    
    def clean_time_discovered(self):
        return self.cleaned_data['time_discovered']
    
    def clean_location_description(self):
        return self.cleaned_data['location_description']
    
    def clean_bearing(self):
        return self.cleaned_data['bearing']
    
    def clean_ground_cover(self):
        return self.cleaned_data['ground_cover']
    
    def clean_cloud_deck(self):
        return self.cleaned_data['cloud_deck']
    
    def clean_animal_condition(self):
        return self.cleaned_data['animal_condition']
    
    def clean_description(self):
        return self.cleaned_data['description']
    
    def clean_collected_by(self):
        return self.cleaned_data['collected_by']
    
    def clean_photo_structure(self):
        return self.cleaned_data['photo_structure']
    
    def clean_photo_as_found(self):
        return self.cleaned_data['photo_as_found']
    
    def clean_photo_as_found2(self):
        return self.cleaned_data['photo_as_found2']
        
    def clean_photo_injury(self):
        return self.cleaned_data['photo_injury']
        
    def clean_photo_other(self):
        return self.cleaned_data['photo_other']

    def clean_report_date(self):
        return self.cleaned_data['report_date']
    
    def clean_time_reported(self):
        return self.cleaned_data['time_reported']
    
    def clean_time_repsonded(self):
        return self.cleaned_data['time_responded']
    
    def clean_weather_TOD(self):
        return self.cleaned_data['weather_TOD']
    
    def clean_outside(self):
        return self.cleaned_data['outside']
    
class ActionsTakenForm(CleanParentMixin,
                       forms.ModelForm):
    class Meta:
        model = ActionsTaken
        fields = '__all__'
    
    def clean_event_time(self):
        return self.cleaned_data('event_time')
    
    def clean_action(self):
        newaction= self.cleaned_data('action')
        if len(newaction)>0:
            return newaction
        else:
            raise ValidationError('Must contain action text', code='actiontext')
            
class NeneSurveyForm(CleanNotesMixin,
                     CleanObserverMixin,
                     CleanTimeMixin,
                     CleanSiteMixin,
                     forms.ModelForm):
    class Meta:
        model = NeneSurvey
        fields = '__all__'
        
    def clean_date(self):
        return self.cleaned_data['date']
    
    def clean_count(self):
        return self.cleaned_data['count']

class CareSetUpForm(CleanLocMixin,
                    LatLonMixin,
                    CleanDistanceMixin,
                    CleanSiteMixin,
                    CleanTurbineMixin,
                    CleanNotesMixin,
                    CleanObserverMixin,
                    CleanPhotoMixin,
                    forms.ModelForm):
    class Meta:
        model = CareSetUp
        fields = '__all__'
        
    def clean_trial(self):
        return self.cleaned_data['trial']
    
    def clean_carcass_number(self):
        return self.cleaned_data['carcass_number']
    
    def clean_start_date(self):
        return self.cleaned_data['start_date']
    
    def clean_carcass_type(self):
        return self.cleaned_data['carcass_type']
    
    def clean_direction(self):
        return self.cleaned_data['direction']
    
    def clean_vegetation(self):
        return self.cleaned_data['vegetation']
    
    def clean_waypoint(self):
        return self.cleaned_data['waypoint']
    

    
class CareMonitoringForm(CleanParentMixin,
                         CleanLocMixin,
                         LatLonMixin,
                         CleanPhotoMixin,
                         CleanNotesMixin,
                         CleanObserverMixin,
                         forms.ModelForm):
    class Meta:
        model=CareMonitoring
        fields = '__all__'
        
    def clean_monitor_date(self):
        return self.cleaned_data['monitor_date']
    
    def clean_present(self):
        return self.cleaned_data['present']
    
    def clean_condition(self):
        return self.cleaned_data['condition']
    
    
class KWPISearchingForm(MonitorDateMixin,
                        CleanWeatherMixin,
                        CleanTempMixin,
                        CleanPrecipMixin,
                        CleanObserverMixin,
                        CleanSearchTypeMixin,
                        CleanTimeMixin,
                        Clean14Mixin,
                        forms.ModelForm):
    class Meta:
        model = KWPISearching
        fields = '__all__'
        
    def clean_t15(self):
        return self.cleaned_data['t15']
    
    def clean_t16(self):
        return self.cleaned_data['t16']
    
    def clean_t17(self):
        return self.cleaned_data['t17']
    
    def clean_t18(self):
        return self.cleaned_data['t18']
    
    def clean_t19(self):
        return self.cleaned_data['t19']
    
    def clean_t20(self):
        return self.cleaned_data['t20']
    
class KWPIISearchingForm(MonitorDateMixin,
                        CleanWeatherMixin,
                        CleanTempMixin,
                        CleanPrecipMixin,
                        CleanObserverMixin,
                        CleanSearchTypeMixin,
                        CleanTimeMixin,
                        Clean14Mixin,
                        forms.ModelForm):
    class Meta:
        model = KWPIISearching
        fields = '__all__'

class SEEFMasterForm(CleanLocMixin,
                     CleanTrialDateMixin,
                     CleanSiteMixin,
                     CleanTurbineMixin,
                     CleanSpeciesMixin,
                     LatLonMixin,
                     CleanDistanceMixin,
                     CleanNotesMixin,
                     forms.ModelForm):
    class Meta:
        model=SEEFMaster
        fields = '__all__'
        
    def clean_found(self):
        return self.cleaned_data['found']
    
    def clean_not_recovered(self):
        return self.cleaned_data['not_recovered']
    
    def clean_point_id(self):
        return self.cleaned_data['point_id']
    
    def clean_searcher(self):
        return self.cleaned_data['searcher']
    
    def clean_canine(self):
        return self.cleaned_data['canine']
    
    def clean_veg_type(self):
        return self.cleaned_data['veg_type']
    
    def clean_proctor(self):
        return self.cleaned_data['proctor']

class SEEFProctorForm(CleanLocMixin,
                     CleanTrialDateMixin,
                     CleanSiteMixin,
                     CleanTurbineMixin,
                     CleanSpeciesMixin,
                     LatLonMixin,
                     CleanDistanceMixin,
                     CleanNotesMixin,
                     forms.ModelForm):
    class Meta:
        model=SEEFMaster
        fields = '__all__'
        
    def clean_point_id(self):
        return self.cleaned_data['point_id']
    
    def clean_veg_type(self):
        return self.cleaned_data['veg_type']
    
    def clean_proctor(self):
        return self.cleaned_data['proctor']
        
class SEEFReportingForm(CleanTrialDateMixin,
                        CleanTurbineMixin,
                        CleanSpeciesMixin,
                        CleanLocMixin,
                        CleanNotesMixin,
                        forms.ModelForm):
    class Meta:
        model = SEEFReporting
        fields = '__all__'
        
    
class WACardSwap(CleanSiteMixin,
                 CleanTurbineMixin,
                 CleanNotesMixin,
                 forms.ModelForm):
    class Meta:
        model = WACardSwap
        fields = '__all__'
        
    def clean_swap_date(self):
        return self.cleaned_data['swap_date']
    
    def clean_detector_type(self):
        return self.cleaned_data['detector_type']
    
    def clean_firmware(self):
        return self.cleaned_data['firmware']
    
    def clean_battery(self):
        return self.cleaned_data['battery']
    
    def clean_mic(self):
        return self.cleaned_data['mic']
    
    def clean_mem_card1(self):
        return self.cleaned_data['mem_card1']
    
    def clean_memory_card1(self):
        return self.cleaned_data['memory_card1']
    
    def clean_mem_card2(self):
        return self.cleaned_data['mem_card2']
    
    def clean_memory_card2(self):
        return self.cleaned_data['memory_card2']
    
    def clean_mem_card3(self):
        return self.cleaned_data['mem_card3']
    
    def clean_memory_card3(self):
        return self.cleaned_data['memory_card3']
    
    