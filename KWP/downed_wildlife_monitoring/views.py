from django.shortcuts import render, get_object_or_404, render_to_response

from django.http import HttpResponse, Http404
from django.views.generic import View
from django.apps import apps
from django.template import RequestContext, loader

from .models import *

class index(View):
    def get(self, request):
	
        models = '<br/>'.join(apps.get_app_config('downed_wildlife_monitoring').models)
        return HttpResponse('<H2>Downed Wildlife Monitoring landing page</h2><br/>'+models)
    
class DownedWildlife(View):
    template_name = 'downed_wildlife_monitoring/data_template'
    
    def get(self, request, idkey):
    	data = get_object_or_404(DownedWildlifeMonitoring, IDKey__iexact=idkey) # return data
    	fieldlist = [field.name for field in data._meta.fields] #return field list as string
    	attr = [getattr(data, item) for item in fieldlist] #return list of object attributes.
    	ziplist = zip(fieldlist, attr) #merge column names and values
    	return render(request, self.template_name,  {'instance': idkey, 'ziplist': ziplist})
        