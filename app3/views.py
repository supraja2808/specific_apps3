from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def string(request):
    return HttpResponse('THIS IS MY FIRST STRING')

def h7(request):
    return render(request,'h7.html')

def h8(request):
    return render(request,'h8.html')

def h9(request):
    return render(request,'h9.html')
