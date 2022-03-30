from django.urls import path
from .views import *

urlpatterns = [
    path('dashboardcounsellor', dashboard, name='dashboard'),
    path('added_blog/', added_blog, name="add_blog"),

]