from django.conf.urls import url

from .views import *

urlpatterns = [
	url(r'^$', index.as_view(), name="DownedWildlife"), #List all models in Downed Wildlife Monitoring
    url(r'^downed/(?P<idkey>[\w\-]+)/$', DownedWildlife.as_view(), name='downedwildlifemonitoring_detail'),
    
]