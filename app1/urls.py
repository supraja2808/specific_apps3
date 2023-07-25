from django.urls import path
from app1.views import *

urlpatterns=[
    path('h1/',h1,name='h1'),
    path('h2/',h2,name='h2'),
    path('h3/',h3,name='h3'),
    path('string1/',string1,name='string1'),


]