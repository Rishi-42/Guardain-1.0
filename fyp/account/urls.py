from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('resetpassword_validate/<uidb64>/<token>/',
         resetpassword_validate, name='resetpassword_validate'),
    path('pharmacyregister/', pharmacyregister, name="pharmacyregister"),
    path('counsellorregister/', counsellorregister, name="counsellorregister"),
    path('forgotpassword/', forgotpassword, name="forgotpassword"),
    path('resetpassword/', resetpassword, name="resetpassword"),
    path('ajax/load_districts/', load_districts, name='ajax_load_districts'),
    path('ajax/load-cities/', load_cities, name='ajax_load_cities'),
]
