from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from django.views import generic
from django.views.generic import View, TemplateView

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home.html', context)

# Create your views here.
#def home(httprequest, *args):
#	my_dict = {
#		'name' : 'Sasa',
#		'lastname' : 'Malesevic',
#		'year' : 1992,
#		'myList' : ['this', 'is', 'my', 'list', 'hello']
#	}
#	return render(httprequest, 'home.html',my_dict)



#class HomeViewClass(View):
#	def get(self, request):
#		return HttpResponse('<h1>Hello World! through Class view</h1>')

