from django.urls import path
from .views import *


urlpatterns = [
    path('place_order/', place_order, name="place_order"),
    path('payments/', payments, name="payments"),
    path('order_complete/', order_complete, name="order_complete"),
]

