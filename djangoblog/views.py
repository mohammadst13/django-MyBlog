from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
    # return HttpResponse('hello I am Mohammad Sayartehrani :D')
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('this is home page and python langueg is the best')
    return render(request, 'about.html')
