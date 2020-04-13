from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import View, TemplateView


# Create your views here.
def home_view(httprequest, *args):
	my_dict = {
		'name' : 'Sasa',
		'lastname' : 'Malesevic',
		'year' : 1992,
		'myList' : ['this', 'is', 'my', 'list', 'hello']
	}
	return render(httprequest, 'home.html',my_dict)


class HomeViewClass(View):
	def get(self, request):
		return HttpResponse('<h1>Hello World! through Class view</h1>')

