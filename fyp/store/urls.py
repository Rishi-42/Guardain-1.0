from django.urls import path
from .views import *

urlpatterns = [
    path('', store, name='store'),
    # path('<slug:city_slug>/', pharmacy_city, name='pharmacy_city'),
    # path('location', location, name='location'),

]
