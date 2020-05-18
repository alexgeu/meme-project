from .models import Comment, Like, LIKE_CHOICES, Meme
from .forms import RawProductForm, ProductCreateForm, MemeForm
from django.views.generic import ListView, TemplateView, RedirectView
from django.core.files.storage import FileSystemStorage
from .forms import *
from .filters import OrderFilter
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404, request
from django.utils import timezone
from django.contrib.auth.models import User

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
#from django.contrib.auth import login, authenticate, logout
#from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, TemplateView



def home(request):
    return render(request, 'home.html')
'''
def productCreateView(httprequest, *args, **kwargs):
	my_form = ProductCreateForm(httprequest.POST or None)
	if my_form.is_valid():
		my_form.save()  # Products.objects.create(**my_form.cleaned_data)
		my_form = ProductCreateForm()
	# my_form = RawProductForm

	context = {
		'form': my_form
	}
	return render(httprequest, 'product_create_view.html', context)
'''
'''
def search(request, *args, **kwargs):
	allProducts = Meme.objects.all()
	print(allProducts)
	myFilter = OrderFilter(request.GET, queryset=allProducts)
	print(myFilter)
	allProducts = myFilter.qs
	print(allProducts)
	context = {
		'allProducts': allProducts,
		'title': 'My Meme list',
		'myFilter': myFilter
	}
	
	return render(request, 'meme_list2.html', context)
'''

def get_context_data(request, *args, **kwargs):
	allmemes = Meme.objects.all()
	myFilter = OrderFilter(request.GET, queryset=allmemes)
	allmemes = myFilter.qs
	context = {
		'allmemes': allmemes,
		'title': 'My Meme list',
		'myFilter': myFilter,
	}
	
	return render(request, 'meme_list2.html', context)

#I think this is also unecessary?
def product_view(request,*args, **kwargs):
	qs = Meme.objects.all()
	user = request.user
	allProducts = Meme.objects.all()

	context = {
		'qs': qs,
		'user': user,
		'allProducts': allProducts,
		'title': 'My product list'
	}
	return render(request, 'meme_list.html', context)
	
def like_meme(request):
	user = request.user
	if request.method == 'POST':
		meme_id = request.POST.get('meme_id')
		meme_obj = Meme.objects.get(id=meme_id)
		
		if user in meme_obj.liked.all():
			meme_obj.liked.remove(user)
		else:
			meme_obj.liked.add(user)
		
		like, created = Like.objects.get_or_create(user=user, meme_id=meme_id)
		
		if not created:
			if like.value == 'Like':
				like.value = 'Unlike'
			else:
				like.value = 'Like'
		like.save()
	return redirect('memes:meme-list')

#this should be renamed to memeDetail
def productDetail(request, my_id, *args, **kwargs):
	oneProduct = get_object_or_404(Meme, id=my_id)
	comments = Comment.objects.filter(meme_id=my_id).order_by('-id')
	print(my_id)
	comment_form = CommentForm(request.POST or None)
	if request.method == 'POST':
		if comment_form.is_valid():
			content = request.POST.get('content')
			comment = Comment.objects.create(meme=oneProduct, user=request.user, content=content)
			comment.save()

			return HttpResponseRedirect(oneProduct.get_absolute_url())
		else:
			comment_form = CommentForm()
	context = {
	'meme' : oneProduct,
	'title' : 'Product Details',
	'comments' : comments,
	'comment_form' : comment_form,
	}

	return render(request,'meme_detail.html', context)

def upload(request):
	context = {}
	if request.method == 'POST':
		uploaded_file = request.FILES['document']
		fs = FileSystemStorage()
		name = fs.save(uploaded_file.name, uploaded_file)
		context ['url'] = fs.url(name)
	return render(request, 'upload.html', context)

def meme_list(request):
	memes = Meme.objects.all()
	print(memes)
	return render(request, 'meme_list.html', {
		'memes': memes
	})

'''def productList(httprequest, *args, **kwargs):
	allProducts = Products.objects.all()
	print(allProducts)
	context = {
		'allProducts': allProducts,
		'title': 'My product list'
	}
	
	return render(httprequest, 'product_list.html', context)
'''

def upload_meme(request):
	if request.method == 'POST':
		form = MemeForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('meme_list')
	else:
		form = MemeForm()
	return render(request, 'upload_meme.html', {
		'form': form
	})

'''
def productDetail(request, my_id, *args, **kwargs):
	oneProduct = get_object_or_404(Products, id=my_id)
	comments = Comment.objects.filter(product=my_id).order_by('-id')
	comment_form = CommentForm(request.POST or None)
	if request.method == 'POST':
		if comment_form.is_valid():
			content = request.POST.get('content')
			comment = Comment.objects.create(product=oneProduct, user=request.user, content=content)
			comment.save()

			return HttpResponseRedirect(oneProduct.get_absolute_url())
		else:
			comment_form = CommentForm()
	context = {
	'obj' : oneProduct,
	'title' : 'Product Details',
	'comments' : comments,
	'comment_form' : comment_form,
	}
'''
