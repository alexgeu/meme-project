from django.shortcuts import render, redirect
from .forms import RegisterForm
#from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, TemplateView

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        # todo change redirect to sasas homepage
        return redirect("/home")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form": form})
