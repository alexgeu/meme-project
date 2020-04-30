from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
