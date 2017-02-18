from django import forms

from .models import *


class BurrowMonitoringForm(forms.ModelForm):

    class Meta:
    	model = BurrowMonitoring
    	fields = '__all__'

class FenceCheckForm(forms.ModelForm):

	class Meta:
		model = FenceCheck
		fields = '__all__'

class SoundCheckForm(forms.ModelForm):
	class Meta:
		model = SoundCheck
		fields = '__all__'

class GeneralNotesForm(forms.ModelForm):
	class Meta:
		model = GeneralNotes
		fields = '__all__'


class OutplantingForm(forms.ModelForm):
	class Meta:
		model = Outplanting
		fields = '__all__'


class NightSurveyForm(forms.ModelForm):
	class Meta:
		model = NightSurvey
		fields = '__all__'


class NightSurveyObservationsForm(forms.ModelForm):
	class Meta:
		model = NightSurveyObservations
		fields = '__all__'


class BANOControlForms(forms.ModelForm):
	class Meta:
		model = BANOControl
		fields = '__all__'