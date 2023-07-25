from django.urls import path
from app3.views import *

urlpatterns=[
    path('string/',string,name='string'),
    path('h7/',h7,name='h7'),
     path('h8/',h8,name='h8'),
      path('h9/',h9,name='h9'),
]