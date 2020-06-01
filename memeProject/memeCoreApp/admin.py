from django.contrib import admin

# Register your models here.
#from .models import Products #local folder import
#from .models import Post
from .models import Meme

#admin.site.register(Products)
#admin.site.register (Post)
admin.site.register (Meme)
from .models import Like, Comment

admin.site.register(Like)
admin.site.register(Comment)
