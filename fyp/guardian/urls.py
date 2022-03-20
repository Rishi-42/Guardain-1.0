from django.urls import path
from .views import *

urlpatterns = [
    path('cities', cities, name='cities'),
    path('', home, name="home"),
    path('placeorder', placeorder, name="placeorder"),
    path('counsellor', counsellor, name="counsellor"),
    path('cart', cart, name="cart"),
    path('productdetail', productdetail, name="productdetail"),
    path('placeorder', placeorder, name="placeorder"),
    path('test', test, name="test"),
    path('dashboardcounsellor', dashboardcounsellor, name='dashboardcounsellor'),
    path('dashboardpharmacist', dashboardpharmacist, name='dashboardpharmacist'),
    path('pharmacies', pharmacies, name='pharmacies'),
]