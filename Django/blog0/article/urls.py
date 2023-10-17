from django.urls import path 
from . import views

urlpatterns = [
    path('',views.Article_view, name='articles'),
]