from django.urls import path
from .views import *

urlpatterns = [
    path('submit_review/<int:pharmacy_id>', submit_review, name='submit_review'),
]
