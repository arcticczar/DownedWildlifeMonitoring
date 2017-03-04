from django.shortcuts import render, get_object_or_404, render_to_response
from django.http.response import HttpResponse, Http404
from django.template import RequestContext, loader
from django.apps import apps
from django.views.generic import View
from django.core.urlresolvers import reverse

import lookup_tables
from .models import *

def lookup_index(request):
	models = '<br/>'.join(apps.get_app_config('lookup_tables').models)
	return HttpResponse('<H2>Lookup landing page</h2><br/>'+models)

def models(request, app, app_model):
	
	try:
		model = apps.get_model(app,app_model)
	except:
		raise Http404
	template = loader.get_template('lookup_tables/lookup_template.html')
	context = RequestContext(request, {'source':model._meta.object_name, 'model':model.objects.all()})
	output = template.render(context)
	return HttpResponse(output)

def personnel_data(request, app, instance, model):
	model = apps.get_model(app, model)
	data = model.objects.get(initials__iexact=instance) # return data
	fieldlist = [field.name for field in data._meta.fields] #return field list as string
	attr = [getattr(data, item) for item in fieldlist] #return list of object attributes.
	ziplist = zip(fieldlist, attr)
	template = loader.get_template('lookup_tables/data_template.html')
	context = RequestContext(request, {'instance': instance, 'ziplist': ziplist})
	output = template.render(context)
	return HttpResponse(output)

def status(request):
	return HttpResponse('Status')
'''
def data(request, model):
	modelactual=apps.get_model('lookup_tables', model)
	modelitems = modelactual.objects.all()
	return render(request, 'lookup_tables/general.html', {'model':modelactual._meta.object_name, 'modelitems':modelitems})
'''
class data(View):
    template_name = 'lookup_tables/general.html'
    
    
    def get_absolute_url(self, model):
        return reverse('data', args={'model':self.model})
        
    def get(self, request, model):
        modelactual=apps.get_model('lookup_tables', model)
        modelitems = modelactual.objects.all()
        return render(
                request, 
                self.template_name, 
                {'model':modelactual._meta.object_name, 'modelitems':modelitems})