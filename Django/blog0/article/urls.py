from django.urls import path 
from . import views

urlpatterns = [
    path('<slug:slug>',views.Articles_view, name='articles'),
]