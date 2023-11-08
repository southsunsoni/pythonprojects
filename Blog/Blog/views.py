from django.http import HttpResponse
from django.shortcuts import  render
def Home_view(request):
    #return HttpResponse('je repond a une  requete')
    return render(request,'Home.html')
