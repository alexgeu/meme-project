from django.contrib import admin

# Register your models here.
from .models import Products,Like #local folder import

admin.site.register(Products)
admin.site.register(Like)