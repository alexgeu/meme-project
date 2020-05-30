"""testproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from register import views as register_views
from myViewSample.views import home
from django.views.generic import TemplateView
from myFirstApp.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', get_context_data, name='search'),
    path('', include('myFirstApp.urls', namespace='memes')),
    path('upload/', upload, name='upload'),
    path('memes/upload/', upload_meme, name='upload_meme'),
    path('memes/<int:my_id>', memeDetail, name='meme-detail'),
    path('memes/', meme_list, name='meme_list'),
    path('register/', register_views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('profile/', register_views.profile, name='profile'),
    path('category/nerd/', cat_nerd),
    path('category/dailystruggle/', cat_dailystruggle),
    path('category/programming/', cat_programming),
    path('category/quotes/', cat_quotes),
    path('mostliked/', count_likes),
    path('mostcommented', count_comments)
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    # URL Patterns for profile pics
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # URL Patterns for static files
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)