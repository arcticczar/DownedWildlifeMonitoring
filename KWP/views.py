from django.apps import apps
from django.template import Context, loader
from django.conf import settings
from django.http.response import HttpResponse, Http404


def homepage(request):
	#Get all apps into a set
	applist = set()
	for item in settings.INSTALLED_APPS:
		if item.split('.')[0]!='django':
			applist.add(item.split('.')[0])

	#Create dictionary for apps with models
	modellist =dict()
	for app in applist:
		for model in apps.get_app_config(app).get_models():
			if app in modellist:
				modellist[app].append(model._meta.model_name)
			else:
				modellist[app]=[model._meta.model_name]

	template = loader.get_template('landingPage.html')
	context = Context({'applist':modellist})
	output = template.render(context)
	return HttpResponse(output)
