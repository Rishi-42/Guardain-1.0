from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('placeorder', placeorder, name="placeorder"),
    path('counsellor', counsellor, name="counsellor"),
    path('cart', cart, name="cart"),
    path('productdetail', productdetail, name="productdetail"),
]