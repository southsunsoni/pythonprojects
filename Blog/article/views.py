from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.http import Http404

def articles_view(request):
    articles=Article.objects.all().order_by('date_of_creation')
    return render(request,'articles/article.html',context={'articles':articles})
   
def article_view(request,slug):
    try:
        article=Article.objects.get(slug=slug)
        return render(request,'articles/detail.html',context={'article':article})
    except Article.doesnotexist:
        raise Http404("page nexiste pas")