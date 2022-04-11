from django.urls import path
from .views import *

urlpatterns = [
    path('', counselor, name='counselor'),
    path('<int:pk>/', counselor_detail, name='counselor_detail'),
]
