from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.



def homepage(request):
	return HttpResponse('KWP Homepage'+'<p><a href="http://127.0.0.1:8000/index/">index</a></p>')

