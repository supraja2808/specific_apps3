from django.urls import path
from app2.views import *

urlpatterns=[
    path('h4/',h4,name='h4'),
    path('h5/',h5,name='h5'),
    path('h6/',h6,name='h6'),
    path('string2/',string2,name='string2'),
]