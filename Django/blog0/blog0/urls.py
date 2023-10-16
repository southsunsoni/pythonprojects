
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home_view),
    path('contact/',views.Contact),
    path('article/',views.Articles)
]
