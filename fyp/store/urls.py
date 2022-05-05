from django.urls import path
from .views import *

urlpatterns = [
    path('pharmacy/<int:pharmacy_id>', all_product, name='all_product'),
    path('pharmacy/<int:pharmacy_id>/category/<slug:category_slug>', all_product, name='category_product'),
    path('pharmacy/<int:pharmacy_id>/category/<slug:category_slug>/<slug:product_slug>', product_detail, name='product_detail'),

    # path('<slug:city_slug>/', pharmacy_city, name='pharmacy_city'),
    # path('location', location, name='location'),
    path('search/', search, name='search'),
]
