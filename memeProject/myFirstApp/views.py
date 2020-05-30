from .models import Comment, Like, LIKE_CHOICES, Meme
from .forms import RawProductForm, ProductCreateForm, MemeForm
from django.views.generic import ListView, TemplateView, RedirectView
from django.core.files.storage import FileSystemStorage
from .forms import *
from .filters import OrderFilter
from .models import Meme
from django.db.models import Q, Count
from django.http import HttpResponse, HttpResponseRedirect, Http404, request
from django.utils import timezone
from django.contrib.auth.models import User
import sys
from subprocess import run, PIPE
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
#from django.contrib.auth import login, authenticate, logout
#from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, TemplateView
from register import models
<<<<<<< HEAD
import os
=======
from django.core.paginator import Paginator
>>>>>>> f369e5fa8792110e221836fe028daced43388159

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
	myFilter2 = OrderFilter(request.GET, queryset=allmemes)
	allmemes = myFilter2.qs
	context = {
		'allmemes': allmemes,
		'title': 'My Meme list',
		'myFilter2': myFilter2,
	}
	redirect('search')

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

def count_likes(request):
	context ={
		'likecount_list': Meme.objects.annotate(the_count=Count('liked')).order_by('-the_count')[:10]
	}
	return render(request, 'count_likes.html', context)

def count_comments(request):
	context = {
		'commentcount_list': Meme.objects.annotate(the_count=Count('comment')).order_by('-the_count')[:10]
	}
	return render(request, 'count_comments.html', context)

#this should be renamed to memeDetail
def productDetail(request, my_id, *args, **kwargs):
	oneProduct = get_object_or_404(Meme, id=my_id)
	comments = Comment.objects.filter(meme_id=my_id).order_by('-id')
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
	'title' : 'Meme Detail View',
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
	paginator = Paginator(memes, 2)  # Show 1 meme per page.
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	print(memes)
	return render(request, 'meme_list.html', {
		# disable meme context due to pagination
		# 'memes': memes,
		'page_obj': page_obj,
	})

def cat_nerd(request):
	queryset = Meme.objects.filter(category = 'Nerd')
	context={
		'nerd_list':queryset
	}
	return render(request, 'category_nerd.html', context)

def cat_dailystruggle(request):
	queryset = Meme.objects.filter(category = 'Daily struggle')
	context={
		'dailystruggle_list': queryset
	}
	return render(request, 'category_dailystruggle.html', context)

def cat_programming(request):
	queryset = Meme.objects.filter(category = 'Programming')
	context={
		'programming_list': queryset
	}
	return render(request, 'category_programming.html', context)

def cat_quotes(request):
	queryset = Meme.objects.filter(category = 'Quotes')
	context={
		'quotes_list': queryset
	}
	return render(request, 'category_quotes.html', context)

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

