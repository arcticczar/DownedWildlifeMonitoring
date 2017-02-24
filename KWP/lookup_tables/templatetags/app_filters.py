from django import template
from django.core.urlresolvers import resolve

register = template.Library()

@register.filter(name=u'return_app_name')
def return_app_name(app):
	return request._meta.label

@register.filter(name=u'return_model_name')
def return_model_name(model):
	return model.__str__()