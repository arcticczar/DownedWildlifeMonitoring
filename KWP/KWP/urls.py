"""KWP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from lookup_tables.views import lookup_index, models, data
from Makamakaole.views import index
from general.views import homepage

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),  #Admin site
    url(r'^$', homepage), #default landing page
    url(r'^index/', index), #List all models in Downed Wildlife Monitoring
    url(r'^lookup/$', lookup_index), #lookup tables landing page
    url(r'^(?P<app>[\w\-]+)/(?P<app_model>[\w\-]+)/$', models), #display model and database records
    url(r'^(?P<app>[\w\-]+)/(?P<model>[\w\-]+)/(?P<instance>[\w\-]+)/$', data)
]
