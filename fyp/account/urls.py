from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('pharmacyregister/', pharmacyregister, name="pharmacyregister"),
]