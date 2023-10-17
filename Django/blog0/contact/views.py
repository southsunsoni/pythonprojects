from django.shortcuts import render
from django.http import HttpResponse
def Contact_view(request):
    return render(request,'contact/contact.html')
