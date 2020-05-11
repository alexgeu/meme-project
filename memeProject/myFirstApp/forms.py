from django import forms
from .models import Products, Upload

class RawProductForm(forms.Form):
	title = forms.CharField()
	description = forms.CharField()
	price = forms.DecimalField()
	
	
class RegisterForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField()
	
class ProductCreateForm(forms.ModelForm):
	class Meta:
		model = Products
		fields = ['title', 'description', 'price']
	
	def clean_title(self, *args, **kwargs):
		tmp = self.cleaned_data.get('title')
		if len(tmp) > 10:
			raise forms.ValidationError('This is too long')
		return tmp

class uploadCreateForm(forms.ModelForm):
	class Meta:
		model = Upload
		fields = ['Caption', 'Image']

	def clean_caption(self, *args, **kwargs):
		tmp = self.cleaned_data.get('Caption')
		if len(tmp) > 100:
			raise forms.ValidationError('This is too long')
		return tmp

