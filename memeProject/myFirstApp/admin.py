from django.contrib import admin

# Register your models here.
from .models import Products,Like, Comment

admin.site.register(Products)
admin.site.register(Like)
admin.site.register(Comment)