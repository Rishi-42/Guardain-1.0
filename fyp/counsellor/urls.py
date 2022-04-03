from django.urls import path
from .views import *

urlpatterns = [
    path('dashboardcounsellor', dashboardcounsellor, name='dashboardcounsellor'),
    path('added_blog/', added_blog, name="added_blog"),

]