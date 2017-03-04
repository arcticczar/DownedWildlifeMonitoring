from django.conf.urls import url

from .views import lookup_index, models, personnel_data, status, data

urlpatterns = [
	url(r'^$', lookup_index, name='lookup'),
	#url(r'^(?P<app>[\w\-]+)/(?P<app_model>[\w\-]+)/$', models, name='model_data'), #display model and database records
   url(r'^(?P<app>[\w\-]+)/(?P<model>[\w\-]+)/(?P<instance>[\w\-]+)/$', personnel_data),
   #url(r'^(?P<model>[\w\-]+)/data$', data.as_view(), name='data' )
	]