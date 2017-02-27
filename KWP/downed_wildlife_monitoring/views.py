from django.shortcuts import render
from django.http import HttpResponse

from django.apps import apps

# Create your views here.

def index(request):
	output = "<p> ".join([str(item._meta.verbose_name) for item in apps.get_models()])
	return HttpResponse(output)