from django import forms
from .models import Products
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

#ALEX COPY

from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]