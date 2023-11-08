from django.urls import path
from . import views
app_name="produit" 
urlpatterns = [
    path('' ,views.articles_view,name='articles'),
    path('creet/',views.creet_view,name='creet'),
    path('<slug:slug>/' ,views.article_view,name='article')
]