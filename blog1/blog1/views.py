from django.http import HttpResponse
from django.shortcuts import render
def Home_view(request):
    #return HttpResponse('this is my home page')
    return render(request,'home.html')