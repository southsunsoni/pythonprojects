from django.http import HttpResponse
from django.shortcuts import render
def Home_view(request):
    return render(request,'home.html')
def Contact(request):
    return render(request,'contact.html')
def Articles(request):
    return render(request,'article.html')