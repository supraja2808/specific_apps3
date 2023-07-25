from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def h4(request):
    return render(request,'h4.html')

def h5(request):
    return render(request,'h5.html')

def h6(request):
    return render(request,'h6.html')

def string2(request):
    return HttpResponse('THIS IS MY STRING2')

