from django import forms
from .models import *
from django.contrib.auth.models import User

class MemeForm(forms.ModelForm):
	class Meta:
		model = Meme
		fields = ('title', 'caption', 'image', 'category')

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('content',)