from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import Context, loader

from .models import *

def lookup_index(request):
	return HttpResponse('Lookup Tables')

def sizes(request):
	model = SizeClass.objects.all()
	template = loader.get_template('lookup_tables/lookup_template.html')
	context = Context({''})
	return HttpResponse(output)

def status(request):
	return HttpResponse('Status')