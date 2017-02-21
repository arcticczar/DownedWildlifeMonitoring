from django import forms

from .models import *

class TrapLocationForm(forms.ModelForm):

	class Meta:
		model=TrapLocation
		fields = '__all___'

class TrapCheckForm(forms.ModelForm):

	class Meta:
		model=TrapCheck
		fields = '__all__'