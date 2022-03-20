from django.urls import path
from .views import *

urlpatterns = [
    path('dashboardpharmacist', dashboardpharmacist, name='dashboardpharmacist'),
    path('added_product', added_product, name='added_product'),
]
