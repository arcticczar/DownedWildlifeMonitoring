# -*- coding: utf-8 -*-
"""
Created on Thu Mar 02 11:01:48 2017

@author: mstelmach
"""

from django.conf.urls import url

from .views import Maka_index

urlpatterns = [
	url(r'^$', Maka_index.as_view(), name='Maka'),
	
	]