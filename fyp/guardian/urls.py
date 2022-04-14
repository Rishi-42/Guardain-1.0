from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('placeorder', placeorder, name="placeorder"),
    path('productdetail', productdetail, name="productdetail"),
    path('placeorder', placeorder, name="placeorder"),
    path('test', test, name="test"),
    path('cities', cities, name='cities'),
    path('cities/<str:city_slug>', pharmacies, name='pharmacies'),
    path('cities/<str:city_slug>/<str:pharmacy_slug>', ind_pharmacy, name='ind_pharmacy'),
    
    path('searchmed', searchmed, name='searchmed'),
    path('readblog', readblog, name='readblog'),


]

