# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 13:33:47 2017

@author: mstelmach
"""

from django.shortcuts import redirect, render

class ObjectCreateMixin:
    form_class=None
    template_name=''
    
    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})
    
    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        else:
            return render(request, self.template_name, {'form': bound_form})
        
class ObjectUpdateMixin:
    form_class=None
    model=None
    template_name=''
    search_method= None
    
    def get(self, request, searchterm):
        obj = get_object_or_404(self.model, search_method=searchterm)
        context = {'form':self.form_class(instance=obj),
                   self.model.__name__.lower(): obj}
        return render(request, self.template_name, context)