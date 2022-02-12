from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('resetpassword_validate/<uidb64>/<token>/', resetpassword_validate, name='resetpassword_validate'),
    # path('pharmacyregister/', pharmacyregister, name="pharmacyregister"),
    path('pharmacyregister/<data>', pharmacyregister, name="pharmacyregister"),
    path('pharmacyregister/', pharmacyregister, name="pharmacyregister"),
    path('forgotpassword/', forgotpassword, name="forgotpassword"),
    path('resetpassword/', resetpassword, name="resetpassword"),

]