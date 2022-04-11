from django.urls import path
from .views import *

urlpatterns =[
    path('', blogs, name='blogs'),
    path('<str:slug>/', blog_detail, name='blog_detail'),
]