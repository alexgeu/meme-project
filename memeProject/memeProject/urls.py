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
# from register.views import register
from register import views as register_views
from myViewSample.views import home_view
from myViewSample.views import HomeViewClass
from django.views.generic import TemplateView
from myFirstApp.views import productList, productCreateView, productDetail, signup, search
from django.urls import include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    path('admin/', admin.site.urls),
    path('Welcome/', home_view),
    path('WelcomeClass/', HomeViewClass.as_view()),
    path('create/', productCreateView, name=''),
    path('products/<int:my_id>', productDetail, name='product-detail'),
    path('profile/', signup),
    path('products/', include('myFirstApp.urls')),
    path('search/', search),
    path('register/', register_views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', register_views.profile, name='profile'),
    #path('', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
