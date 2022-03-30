from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('placeorder', placeorder, name="placeorder"),
    path('counsellor', counsellor, name="counsellor"),
    path('cart', cart, name="cart"),
    path('productdetail', productdetail, name="productdetail"),
    path('placeorder', placeorder, name="placeorder"),
    path('test', test, name="test"),
    path('cities', cities, name='cities'),
    path('cities/<str:city_slug>', pharmacies, name='pharmacies'),
    path('pharmacies', pharmacies, name='pharmacies'),
    # path('pharmacies/<slug:city_slug>/', pharmacies, name='pharmacies_by_cities'),


    path('counsellors', counsellors, name='counsellors'),
    path('searchmed', searchmed, name='searchmed'),
    path('viewblogs', viewblogs, name='viewblogs'),
    path('readblog', readblog, name='readblog'),
]

