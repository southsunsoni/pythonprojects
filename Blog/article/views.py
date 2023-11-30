from django.shortcuts import render
from django.http import HttpResponse
from .forms import ArticleForm
from .models import Article
from django.http import Http404
from django.shortcuts import get_object_or_404

def articles_view(request):
    articles=Article.objects.all().order_by('date_of_creation')
    return render(request,'articles/article.html',context={'articles':articles})
   
def article_view(request,slug):
    article=get_object_or_404(Article,slug=slug)
    return render(request,'articles/list.html',context={'articles':article})
    #try:
     #   article=Article.objects.get(slug=slug)
     #   return render(request,'articles/detail.html',context={'article':article})
    #except Article.doesNotexist:
     #   raise Http404("page nexiste pas")
def cree_view(request):
    form = ArticleForm()
    return render(request,'articles/cree.html',context={'form':form})