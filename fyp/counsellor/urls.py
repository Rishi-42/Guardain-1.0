from django.urls import path
from .views import *

urlpatterns = [
    path('dashboardcounsellor', dashboardcounsellor, name='dashboardcounsellor'),
    path('added_blog/', added_blog, name="added_blog"),
    path('cpaymentlog', cpaymentlog, name="cpaymentlog"),
    path('ccustomerbook', ccustomerbook, name="ccustomerbook"),
    path('corderlog', corderlog, name="corderlog"),
    path('creview', creview, name="creview"),	
]