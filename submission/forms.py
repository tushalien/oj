from django import forms 
from .models import Submissions

class SubmitForm(forms.ModelForm):
	class Meta :
		model = Submissions
		fields=[
			"language",
			
			"code"
		]