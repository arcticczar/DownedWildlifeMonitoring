# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http.response import HttpResponse, Http404
from django.template import RequestContext, loader
from django.apps import apps
from django.views.generic import View
from django.core.urlresolvers import reverse

from .models import *
from lookup_tables.forms import SizeClassForm


class generic_detail_mixin:
    def get(self, request, inputvalue ):
        data = get_object_or_404(self.parentmodel, self.search_term) # return data
    	fieldlist = [field.name for field in data._meta.fields] #return field list as string
    	attr = [getattr(data, item) for item in fieldlist] #return list of object attributes.
    	ziplist = zip(fieldlist, attr) #merge column names and values
    	return render(request, self.template_name,  {'instance': self.model_attribute, 'ziplist': ziplist})

#Return all models in the lookup_tables app
def lookup_index(request):
	models = '<br/>'.join(apps.get_app_config('lookup_tables').models)
	return HttpResponse('<H2>Lookup landing page</h2><br/>'+models)



class SizeClassDetail(View):
    template_name= 'lookup_tables/SizeClass_detail.html'
    
    def get_object(self):
        return get_object_or_404(SizeClass, size_txt__iexact=self.size_txt)
    
    def get_absolute_url(self, size_txt):
        return reverse('sizeclass_detail', kwargs={'size_txt':size_txt})
    
    def get(self, request, size_txt):
        size_text = get_object_or_404(SizeClass, size_txt__iexact=size_txt)
        return render(request, self.template_name, {'size_txt':size_text})

'''
#Create a size class through POST
def SizeClassCreate(request):
    if request.method == 'POST':
        form = SizeClassForm(request.POST)
        if form.is_valid():
            new_SizeClass=form.save()
            return redirect(new_SizeClass)
        else:  #invalid data
            return render (request, 'lookup_tables/SizeClass_form.html', {'form':SizeClassForm})
    else:  #non 'post' method
        form = SizeClassForm()
        return render(request, 'lookup_tables/SizeClass_form.html', {'form':SizeClassForm})
'''

class SizeClassCreate(View):
    form_class=SizeClassForm
    template_name='lookup_tables/SizeClass_form.html'
    
    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})
    
    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_post= bound_form.save()
            return redirect(new_post)
        else:
            return render(request, self.template_name, {'form':bound_form})
        

#return only the detail of a single status
class Status(View):
    template_name='lookup_tables/Status_detail.html'
    
    def get_absolute_url(self, status_txt):
        return reverse('status_detail', kwargs={'status_txt':status_txt})
    
    def status_detail(self, request, status_txt):
        #Match only status text, case insensitive
        status = get_object_or_404(Status, status_txt__iexact=status_txt)
        return render(request, self.template_name, {'status_txt': status})

#Return details for each speices def
class SpeciesDefView(View):
    template_name = 'lookup_tables/data_template.html'
    
    def get(self, request, species_code):
    	data = get_object_or_404(SpeciesDef, species_code__iexact=species_code.lower()) # return data
    	fieldlist = [field.name for field in data._meta.fields] #return field list as string
    	attr = [getattr(data, item) for item in fieldlist] #return list of object attributes.
    	ziplist = zip(fieldlist, attr) #merge column names and values
    	return render(request, self.template_name,  {'instance': species_code, 'ziplist': ziplist})

class AgeView(View):
    template_name = 'lookup_tables/data_template.html'
    
    def get(self, request, age):
    	data = get_object_or_404(Age, age_text__iexact=age) # return data
    	fieldlist = [field.name for field in data._meta.fields] #return field list as string
    	attr = [getattr(data, item) for item in fieldlist] #return list of object attributes.
    	ziplist = zip(fieldlist, attr) #merge column names and values
    	return render(request, self.template_name,  {'instance': age, 'ziplist': ziplist})
    
class PlantSpeciesView(View):
    template_name = 'lookup_tables/data_template.html'
    
    def get(self, request, common_name):
    	data = get_object_or_404(PlantSpecies, common_name__iexact=common_name) # return data
    	fieldlist = [field.name for field in data._meta.fields] #return field list as string
    	attr = [getattr(data, item) for item in fieldlist] #return list of object attributes.
    	ziplist = zip(fieldlist, attr) #merge column names and values
    	return render(request, self.template_name,  {'instance': common_name, 'ziplist': ziplist})
    
class DirectionView(View):
    template_name = 'lookup_tables/data_template.html'
    
    def get(self, request, direction_short):
    	data = get_object_or_404(Direction, direction_short__iexact=direction_short) # return data
    	fieldlist = [field.name for field in data._meta.fields] #return field list as string
    	attr = [getattr(data, item) for item in fieldlist] #return list of object attributes.
    	ziplist = zip(fieldlist, attr) #merge column names and values
    	return render(request, self.template_name,  {'instance': direction_short, 'ziplist': ziplist})
    
class BaitView(View):
    template_name = 'lookup_tables/data_template.html'
    
    def get(self, request, bait_text):
    	data = get_object_or_404(Bait, bait_text__iexact=bait_text) # return data
    	fieldlist = [field.name for field in data._meta.fields] #return field list as string
    	attr = [getattr(data, item) for item in fieldlist] #return list of object attributes.
    	ziplist = zip(fieldlist, attr) #merge column names and values
    	return render(request, self.template_name,  {'instance': bait_text, 'ziplist': ziplist})
    
class CanineView(View):
    template_name = 'lookup_tables/data_template.html'
    
    def get(self, request, name):
    	data = get_object_or_404(Canine, name__iexact=name) # return data
    	fieldlist = [field.name for field in data._meta.fields] #return field list as string
    	attr = [getattr(data, item) for item in fieldlist] #return list of object attributes.
    	ziplist = zip(fieldlist, attr) #merge column names and values
    	return render(request, self.template_name,  {'instance': name, 'ziplist': ziplist})
    
class SiteView(View):
    template_name = 'lookup_tables/data_template.html'
    
    def get(self, request, locations):
    	data = get_object_or_404(Site, locations__iexact=locations) # return data
    	fieldlist = [field.name for field in data._meta.fields] #return field list as string
    	attr = [getattr(data, item) for item in fieldlist] #return list of object attributes.
    	ziplist = zip(fieldlist, attr) #merge column names and values
    	return render(request, self.template_name,  {'instance': locations, 'ziplist': ziplist})

#Class based view to return the details of infrastructure (location)
class InfrastructureView(View):
    template_name = 'lookup_tables/infrastructure.html'
    
    def get_absolute_url(self, phase, name):
        return reverse('infrastructure', kwargs={'phase':phase, 'name':name})
    
    def get(self, request, phase, name):
        #return the first item in the filtered list of Infrastrucutre objects by phase and name.  Expecting only 1.
        try:
            inf = Infrastructure.objects.filter(phase=phase, name__iexact=name)[0]
        except:
            raise Http404
        return render(
                request,
                self.template_name,
                {'phase':phase, 'name':name, 'inf':inf})
        
class TrapTypeView(View):
    template_name = 'lookup_tables/data_template.html'
    
    def get(self, request, trap_type_text):
    	data = get_object_or_404(TrapType, trap_type_text__iexact=trap_type_text) # return data
    	fieldlist = [field.name for field in data._meta.fields] #return field list as string
    	attr = [getattr(data, item) for item in fieldlist] #return list of object attributes.
    	ziplist = zip(fieldlist, attr) #merge column names and values
    	return render(request, self.template_name,  {'instance': trap_type_text, 'ziplist': ziplist})
        
    
class WeatherView(View):
    template_name = 'lookup_tables/data_template.html'
    
    def get(self, request, rain):
    	data = get_object_or_404(Weather, rain__iexact=rain) # return data
    	fieldlist = [field.name for field in data._meta.fields] #return field list as string
    	attr = [getattr(data, item) for item in fieldlist] #return list of object attributes.
    	ziplist = zip(fieldlist, attr) #merge column names and values
    	return render(request, self.template_name,  {'instance': rain, 'ziplist': ziplist})

class Nightsurvey_BehaviorView(View):
    template_name = 'lookup_tables/data_template.html'
    
    def get(self, request, behavior):
    	data = get_object_or_404(NightSurvey_Behavior, behavior__iexact=behavior) # return data
    	fieldlist = [field.name for field in data._meta.fields] #return field list as string
    	attr = [getattr(data, item) for item in fieldlist] #return list of object attributes.
    	ziplist = zip(fieldlist, attr) #merge column names and values
    	return render(request, self.template_name,  {'instance': behavior, 'ziplist': ziplist})   
    
class Nightsurvey_ElevationView(View):
    template_name = 'lookup_tables/data_template.html'
    
    def get(self, request, elevation):
    	data = get_object_or_404(NightSurvey_Elevation, elevation__iexact=elevation) # return data
    	fieldlist = [field.name for field in data._meta.fields] #return field list as string
    	attr = [getattr(data, item) for item in fieldlist] #return list of object attributes.
    	ziplist = zip(fieldlist, attr) #merge column names and values
    	return render(request, self.template_name,  {'instance': elevation, 'ziplist': ziplist})
  
class Nightsurvey_DistanceView(View):
    template_name = 'lookup_tables/data_template.html'
    
    def get(self, request, distance_range):
    	data = get_object_or_404(NightSurvey_Distance, distance_range__iexact=distance_range) # return data
    	fieldlist = [field.name for field in data._meta.fields] #return field list as string
    	attr = [getattr(data, item) for item in fieldlist] #return list of object attributes.
    	ziplist = zip(fieldlist, attr) #merge column names and values
    	return render(request, self.template_name,  {'instance': distance_range, 'ziplist': ziplist})
    
class BandColorView(View):
    template_name = 'lookup_tables/data_template.html'
    
    def get(self, request, color_text):
    	data = get_object_or_404(BandColor, color_text__iexact=color_text) # return data
    	fieldlist = [field.name for field in data._meta.fields] #return field list as string
    	attr = [getattr(data, item) for item in fieldlist] #return list of object attributes.
    	ziplist = zip(fieldlist, attr) #merge column names and values
    	return render(request, self.template_name,  {'instance': color_text, 'ziplist': ziplist})
    
class RandomPointsView(View):
    template_name = 'lookup_tables/data_template.html'
    
    def get(self, request, point_id):
    	data = get_object_or_404(RandomPoints, point_id=point_id) # return data
    	fieldlist = [field.name for field in data._meta.fields] #return field list as string
    	attr = [getattr(data, item) for item in fieldlist] #return list of object attributes.
    	ziplist = zip(fieldlist, attr) #merge column names and values
    	return render(request, self.template_name,  {'instance': point_id, 'ziplist': ziplist})

class SearchAreaView(View):
    template_name = 'lookup_tables/data_template.html'
    
    def get(self, request, turbine):
    	data = get_object_or_404(SearchArea, turbine=turbine) # return data
    	fieldlist = [field.name for field in data._meta.fields] #return field list as string
    	attr = [getattr(data, item) for item in fieldlist] #return list of object attributes.
    	ziplist = zip(fieldlist, attr) #merge column names and values
    	return render(request, self.template_name,  {'instance': turbine, 'ziplist': ziplist})

#Return details of perssonel by initials lookup/personnel/ms/data
def personnel_data(request, instance):
	data = get_object_or_404(Personnel, initials__iexact=instance) # return data
	fieldlist = [field.name for field in data._meta.fields] #return field list as string
	attr = [getattr(data, item) for item in fieldlist] #return list of object attributes.
	ziplist = zip(fieldlist, attr) #merge column names and values
	template = loader.get_template('lookup_tables/data_template.html')
	context = RequestContext(request, {'instance': instance, 'ziplist': ziplist})
	output = template.render(context)
	return HttpResponse(output)

#General class based view for listing all records in a model.
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
