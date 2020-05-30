from .models import *
from .forms import *
from django.views.generic import ListView, TemplateView, RedirectView
from django.core.files.storage import FileSystemStorage
from .filters import OrderFilter
from django.db.models import Q, Count
from django.http import HttpResponse, HttpResponseRedirect, Http404, request
from django.utils import timezone
from django.contrib.auth.models import User
from subprocess import run, PIPE
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import View, TemplateView
from register import models
from django.core.paginator import Paginator

def get_context_data(request, *args, **kwargs):
	"""This function offfers the ability to (partially) search memes)"""
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

def like_meme(request):
	"""Users can like memes and saving the likes"""
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
	"""counting the likes an showing and ordering them. Afterwards they are shown in the sidebar"""
	context ={
		'likecount_list': Meme.objects.annotate(the_count=Count('liked')).order_by('-the_count')[:10]
	}
	return render(request, 'count_likes.html', context)

def count_comments(request):
	"""counting the comments an showing and ordering them. Afterwards they are shown in the sidebar"""
	context = {
		'commentcount_list': Meme.objects.annotate(the_count=Count('comment')).order_by('-the_count')[:10]
	}
	return render(request, 'count_comments.html', context)

#this should be renamed to memeDetail
def memeDetail(request, my_id, *args, **kwargs):
	"""The memes, which are shown on the landing page, are linked to the own view.
	The view shows comments, likes and some other details."""
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
	"""shows all memes, which are currently uploaded to the webpage"""
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
	"""Displays all memes within the category 'nerd'"""
	queryset = Meme.objects.filter(category = 'Nerd')
	context={
		'nerd_list':queryset
	}
	return render(request, 'category_nerd.html', context)

def cat_dailystruggle(request):
	"""Displays all memes within the category 'dailystruggle'"""
	queryset = Meme.objects.filter(category = 'Daily struggle')
	context={
		'dailystruggle_list': queryset
	}
	return render(request, 'category_dailystruggle.html', context)

def cat_programming(request):
	"""Displays all memes within the category 'programming'"""
	queryset = Meme.objects.filter(category = 'Programming')
	context={
		'programming_list': queryset
	}
	return render(request, 'category_programming.html', context)

def cat_quotes(request):
	"""Displays all memes within the category 'quotes'"""
	queryset = Meme.objects.filter(category = 'Quotes')
	context={
		'quotes_list': queryset
	}
	return render(request, 'category_quotes.html', context)

def upload_meme(request):
	"""uploads and saves a meme"""
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