from django.shortcuts import render

from django.http import HttpResponse

from django.apps import apps

from .models import *


def index(request):
	output = "<p> ".join([str(item._meta.verbose_name) for item in apps.get_models()])
	return HttpResponse(output)