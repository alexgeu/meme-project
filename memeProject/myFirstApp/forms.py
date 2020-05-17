from django import forms

from .models import *
from django import forms
from django.contrib.auth.models import User

class RawProductForm(forms.Form):
	title = forms.CharField()
	description = forms.CharField()
	price = forms.DecimalField()
	
class ProductCreateForm(forms.ModelForm):
	class Meta:
		model = Products
		fields = ['title', 'description', 'price',]
	

	def clean_title(self, *args, **kwargs):
		tmp = self.cleaned_data.get('title')
		if len(tmp) > 10:
			raise forms.ValidationError('This is too long')
		return tmp

class MemeForm(forms.ModelForm):
	class Meta:
		model = Meme
		fields = ('title', 'caption', 'image')

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('content',)
		

