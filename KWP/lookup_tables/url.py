# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import (lookup_index, 
                    personnel_data, 
                    Status, 
                    InfrastructureView, 
                    SizeClassDetail,
                    SizeClassCreate,
                    SpeciesDefView,
                    AgeView,
                    PlantSpeciesView,
                    DirectionView,
                    BaitView,
                    CanineView,
                    SiteView,
                    TrapTypeView,
                    WeatherView,
                    Nightsurvey_BehaviorView,
                    Nightsurvey_ElevationView,
                    Nightsurvey_DistanceView,
                    BandColorView,
                    RandomPointsView,
                    SearchAreaView
                    )

urlpatterns = [
        url(r'^$', lookup_index, name='lookup'),
        url(r'sizeclass/create/$', SizeClassCreate.as_view(), name='SizeClassCreate'),
        url(r'sizeclass/(?P<size_txt>[\w\-]+)/$', SizeClassDetail.as_view(), name='sizeclass_detail'),
        url(r'status/(?P<status_txt>[\w\-]+)$', Status.as_view(),  name='status_detail'),
        url(r'speciesdef/(?P<species_code>[\w\-]+)$', SpeciesDefView.as_view(), name='speciesdef_detail'),
        url(r'age/(?P<age>[\w\-]+)$', AgeView.as_view(), name='age_detail'),
        url(r'plantspecies/(?P<common_name>[\w\-]+)$', PlantSpeciesView.as_view(), name='plantspecies_detail'),
        url(r'direction/(?P<direction_short>[\w\-]+)$', DirectionView.as_view(), name='direction_detail'),
        url(r'bait/(?P<bait_text>[\w\- ]+)$', BaitView.as_view(), name='bait_detail'),
        url(r'personnel/(?P<instance>[\w\-]+)/$', personnel_data, name='personnel_detail'),
        url(r'canine/(?P<name>[\w\- ]+)/$', CanineView.as_view(), name='canine_detail'),
        url(r'site/(?P<locations>[\w\- ]+)/$', SiteView.as_view(), name='site_detail'),
        url(r'infrastructure/(?P<phase>[\w\-]+)/(?P<name>[\w\-]+)$', InfrastructureView.as_view(), name='infrastructure'),
        url(r'traptype/(?P<trap_type_text>[\w\- ]+)$', TrapTypeView.as_view(), name='traptype_detail'),
        url(r'weather/(?P<rain>[\w\- ]+)$', WeatherView.as_view(), name='weather_detail'),
        url(r'nightsurvey_behavior/(?P<behavior>[\w\- ]+)$', Nightsurvey_BehaviorView.as_view(), name='nightsurvey_behavior_detail'),
        url(r'nightsurvey_elevation/(?P<elevation>[\w\- ]+)$', Nightsurvey_ElevationView.as_view(), name='nightsurvey_elevation_detail'),
        url(r'nightsurvey_distance/(?P<distance_range>[\w\- ><]+)$', Nightsurvey_DistanceView.as_view(), name='nightsurvey_distancedetail'),
        url(r'bandcolor/(?P<color_text>[\w\-]+)$', BandColorView.as_view(), name='bandcolor_detail'),
        url(r'randompoints/(?P<point_id>[\w\-]+)$', RandomPointsView.as_view(), name='randompoints_detail'),
        url(r'searcharea/(?P<turbine>[\w\-]+)$', SearchAreaView.as_view(), name='searcharea_detail')
	]