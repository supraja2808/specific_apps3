from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def h1(request):
    return render(request,'h1.html')

def h2(request):
    return render(request,'h2.html')

def h3(request):
    return render(request,'h3.html')

def string1(request):
    return HttpResponse('THIS IS MY STRING1')



