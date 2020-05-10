from django.shortcuts import render, get_object_or_404
from .models import Products, Register, Like
from .forms import RawProductForm, RegisterForm, ProductCreateForm
from .filters import OrderFilter
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404, request
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import RedirectView
from django.utils import timezone
from django.contrib.auth.models import User


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


#ALEX COPY
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import RegisterForm
#from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, TemplateView

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created ({username})! Your are now able to login.')
            return redirect('/login')
    else:
        form = RegisterForm()

    return render(request, "register/register.html", {"form": form})

# Decorator to check if user is logged in
@login_required
def profile(request):
    return render(request, 'users/profile.html')

