from django.urls import path
from .views import *

urlpatterns = [
    path('add_blog/', add_blog, name="add_blog"),

]