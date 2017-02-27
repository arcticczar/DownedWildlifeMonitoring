from django.conf.urls import url

from .views import lookup_index, models, personnel_data, status

urlpatterns = [
	url(r'^lookup/', lookup_index),
	url(r'^(?P<app>[\w\-]+)/(?P<app_model>[\w\-]+)/$', models), #display model and database records
    url(r'^(?P<app>[\w\-]+)/(?P<model>[\w\-]+)/(?P<instance>[\w\-]+)/$', personnel_data),
    url(r'^lookup/$', lookup_index), #lookup tables landing page
	]