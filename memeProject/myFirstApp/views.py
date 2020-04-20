from django.shortcuts import render, get_object_or_404

from .models import Products, Register
from .forms import RawProductForm, RegisterForm, ProductCreateForm
from .filters import OrderFilter


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

def upload(httprequest, *args, **kwargs):
	return render(httprequest, 'uploading.html')


