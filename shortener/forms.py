from django import forms
from django.core.validators import URLValidator
from .validators import validate_url

class SubmitUrlForm(forms.Form):
	url = forms.CharField(label="" , validators=[validate_url] , widget=forms.TextInput(
		attrs={
			"placeholder":"http://xxx.xx/xxx/xx/xx", 
			"class" : "form-control"
		}))

	#abc 
	"""
	def clean(self): # form
		cleaned_data = super(SubmitUrlForm , self).clean()
		url = cleaned_data.get('url')
		url_validator = URLValidator()
		try:
			url_validator(url)
		except:
			raise forms.ValidationError("Invalid URL")
		return url 
		#print(url)
	
	def clean_url(self): # field
		url = self.cleaned_data['url']
		print(url)
		url_validator = URLValidator()
		try:
			url_validator(url)
		except:
			raise forms.ValidationError("Invalid URL")
		return url 

	
	def clean_abc()

	"""