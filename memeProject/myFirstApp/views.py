from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Products, Register, Meme
from .forms import RawProductForm, RegisterForm, ProductCreateForm, MemeForm
from .filters import OrderFilter
from django.views.generic import ListView, TemplateView
from .models import Post
from django.core.files.storage import FileSystemStorage


def home(request):
    return render(request, 'home.html')

def productCreateView(httprequest, *args, **kwargs):
	my_form = ProductCreateForm(httprequest.POST or None)
	if my_form.is_valid():
		my_form.save() #Products.objects.create(**my_form.cleaned_data)
		my_form = ProductCreateForm()
		#my_form = RawProductForm
	
	context = {
		'form': my_form
	}
	return render(httprequest, 'product_create_view.html', context)


'''
def productCreateView(httprequest, *args, **kwargs):
	my_form = RawProductForm(httprequest.POST or None)
	if my_form.is_valid():
		Products.objects.create(**my_form.cleaned_data)
		my_form = RawProductForm
	
	context = {
		'form' : my_form
	}
	return render(httprequest, 'product_create_view.html', context)

'''

# Create your views here.
def productList(httprequest, *args, **kwargs):
	allProducts = Products.objects.all()
	print(allProducts)
	context = {
		'allProducts': allProducts,
		'title': 'My product list'
	}
	
	return render(httprequest, 'product_list.html', context)


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
	
	return render(httprequest, 'product_list.html', context)

def productDetail(httprequest, my_id, *args, **kwargs):
	#oneProduct = Products.objects.get(id=2)
	oneProduct = get_object_or_404(Products, id=my_id)
	context = {
	'obj' : oneProduct,
	'title' : 'Product Details'
	}
	
	return render(httprequest,'product_detail.html', context)


def signup(httprequest, *args, **kwargs):
	my_form = RegisterForm(httprequest.POST or None)
	if my_form.is_valid():
		Register.objects.create(**my_form.cleaned_data)
		my_form = RegisterForm
	
	context = {
		'form': my_form
	}
	return render(httprequest, 'profile.html', context)

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






