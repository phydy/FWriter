"""FWriters URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from dashboard import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve
from writers import views as writer_views
from django.contrib.auth import views as auth_views
from dashboard.views import create, submit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', writer_views.home, name = 'd-home'),
    path('register/', writer_views.register, name='register'),
    path('profile/', writer_views.profile, name='profile'),
    path('terms/', writer_views.terms, name='terms'),
    path('login/', auth_views.LoginView.as_view(template_name='writers/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='writers/logout.html'), name='logout'),
    path('dashboard/', include('dashboard.urls')),
    url(r'^download/(?P<path>^)$', serve,{'document_root:settings.MEDIA_ROOT'}),
    path('submit/', views.submit, name ='d-submit'),
    path('create/', views.create, name ='a-create')
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
