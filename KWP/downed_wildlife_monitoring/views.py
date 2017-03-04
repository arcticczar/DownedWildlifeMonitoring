from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import View
from django.apps import apps

from .models import *

class index(View):
    def get(self, request):
	
        models = '<br/>'.join(apps.get_app_config('downed_wildlife_monitoring').models)
        return HttpResponse('<H2>Downed Wildlife Monitoring landing page</h2><br/>'+models)