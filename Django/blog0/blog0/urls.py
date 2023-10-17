
from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('',views.Home_view,name='Home'),
    path('article/',include('article.urls')),
    path('contact/',include('contact.urls')),
]
