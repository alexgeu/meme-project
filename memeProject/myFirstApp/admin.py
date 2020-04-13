from django.contrib import admin

# Register your models here.
from .models import Products #local folder import

admin.site.register(Products)