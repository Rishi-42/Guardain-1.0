from django.urls import path
from .views import *

urlpatterns =[
    path('<int:id>', schedule_meeting, name='schedulemeeting'),	
]