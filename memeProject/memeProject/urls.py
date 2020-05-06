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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
#from myViewSample.views import HomeViewClass
from django.views.generic import TemplateView
from myFirstApp.views import productList, productCreateView, productDetail, signup, search, upload, meme_image_view, success, home, HomePageView
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Welcome/', home),
    #path('WelcomeClass/', HomeViewClass.as_view()),
    path('create/', productCreateView, name=''),
    path('products/<int:my_id>', productDetail, name='product-detail'),
    path('profile/', signup),
    path('products/', include('myFirstApp.urls')),
    path('search/', search),
    path('upload/', meme_image_view, name='upload' ),
    path('success/', success, name='success'),
    path('', include('myFirstApp.urls')),
    path('', HomePageView.as_view(), name='home'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

