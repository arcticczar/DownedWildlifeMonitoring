from django.shortcuts import render, get_object_or_404, render_to_response
from django.http.response import HttpResponse, Http404
from django.template import Context, loader
from django.apps import apps

import lookup_tables
from .models import *

def lookup_index(request):
	app = ''
	return HttpResponse('Im here' +str(request))

def models(request, app, app_model):
	
	try:
		model = apps.get_model(app,app_model)
	except:
		raise Http404
	template = loader.get_template('lookup_tables/lookup_template.html')
	context = Context({'source':model._meta.object_name, 'model':model.objects.all()})
	output = template.render(context)
	return HttpResponse(output)


def personnel_data(request, app, instance, model):
	model = apps.get_model(app, model)
	data = model.objects.get(initials__iexact=instance) # return data
	fieldlist = [field.name for field in data._meta.fields] #return field list as string
	attr = [getattr(data, item) for item in fieldlist] #return list of object attributes.
	ziplist = zip(fieldlist, attr)
	template = loader.get_template('lookup_tables/data_template.html')
	context = Context({'instance': instance, 'ziplist': ziplist})
	output = template.render(context)
	return HttpResponse(output)

def status(request):
	return HttpResponse('Status')