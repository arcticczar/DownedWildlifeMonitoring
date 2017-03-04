from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import View
from django.apps import apps

from .models import *

class Maka_index(View):
    def get(self, request):
	
        models = '<br/>'.join(apps.get_app_config('Makamakaole').models)
        return HttpResponse('<H2>Makamakaole landing page</h2><br/>'+models)