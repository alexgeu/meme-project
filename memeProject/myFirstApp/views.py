from .models import Products, Meme, Like, Comment
from .forms import RawProductForm, ProductCreateForm, MemeForm
from django.views.generic import ListView, TemplateView, RedirectView
from .models import Post
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


def search(httprequest, *args, **kwargs):
	allProducts = Products.objects.all()
	print(allProducts)
	myFilter = OrderFilter(httprequest.GET, queryset=allProducts)
	allProducts = myFilter.qs
	context = {
		'allProducts': allProducts,
		'title': 'My product list',
		'myFilter': myFilter
	}
	
	return render(httprequest, 'product_list2.html', context)

# Create your views here.
def productList(httprequest, *args, **kwargs):
	allProducts = Products.objects.all()
	print(allProducts)
	context = {
		'allProducts': allProducts,
		'title': 'My product list'
	}
	
	return render(httprequest, 'product_list.html', context)


def product_view(request,*args, **kwargs):
	qs = Products.objects.all()
	user = request.user
	allProducts = Products.objects.all()

	context = {
		'qs': qs,
		'user': user,
		'allProducts': allProducts,
		'title': 'My product list'
	}
	return render(request, 'product_list.html', context)




def like_product(request):
	user = request.user
	if request.method == 'POST':
		product_id = request.POST.get('product_id')
		product_obj = Products.objects.get(id=product_id)
		
		if user in product_obj.liked.all():
			product_obj.liked.remove(user)
		else:
			product_obj.liked.add(user)
		
		like, created = Like.objects.get_or_create(user=user, product_id=product_id)
		
		if not created:
			if like.value == 'Like':
				like.value = 'Unlike'
			else:
				like.value = 'Like'
		like.save()
	return redirect('products:product-list')

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

	return render(request,'product_detail.html', context)

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
	return render(request, 'meme_list.html', {
		'memes': memes
	})

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


