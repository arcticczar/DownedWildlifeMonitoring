from django import forms

from .models import *

class DownedWildlifeMonitoringForm(forms.ModelForm):

	class Meta:
		model = DownedWildlifeMonitoring
    	fields = '__all__'

class ActionsTakenForm(forms.ModelForm):

	class Meta:
		model = ActionsTaken
		fields = '__all__'

class NeneSurveyForm(forms.ModelForm):

	class Meta:
		model = NeneSurvey
		fields = '__all__'

class CareSetUpForm(forms.ModelForm):

	class Meta:
		model = CareSetUp
		fields = '__all__'

class CareMonitoringForm(forms.ModelForm):

	class Meta:
		model = CareMonitoring
		fields = '__all__'

class KWPISearchingForm(forms.ModelForm):

	class Meta:
		model = KWPISearching
		fields = '__all__'

class KWPIISearchingForm(forms.ModelForm):

	class Meta:
		model = KWPIISearching
		fields = '__all__'

class SEEFMasterForm(forms.ModelForm):

	class Meta:
		model = SEEFMaster
		fields = '__all__'

class SEEFReportingForm(forms.ModelForm):

	class Meta:
		model = SEEFReporting
		fields = '__all__'


class WEOPForm(forms.ModelForm):

	class Meta:
		model = WEOP
		fields = '__all__'
		