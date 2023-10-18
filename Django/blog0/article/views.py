from django.shortcuts import render
from django.http import HttpResponse
from .db_libry import articles

def Articles_view(request):
    return render(request,'articles/list.html',context={'articles':articles})
def Article_view(request,slug):
    return HttpResponse(slug)