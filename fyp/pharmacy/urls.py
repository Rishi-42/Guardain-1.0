from django.urls import path
from .views import *

urlpatterns = [
    path('dashboardpharmacist', dashboardpharmacist, name='dashboardpharmacist'),
    path('added_product', added_product, name='added_product'),
    path('delete/<int:id>', delete, name='delete'),
    path('edit/<int:id>', update, name='edit'),
    path('edit/update/<int:id>', update, name='update'),
    path('pbooked', pbooked, name='pbooked'),
    path('pordered', pordered, name='pordered'),
    path('reviewed', reviewed, name='reviewed'),
    path('reviewdetail/<id>', reviewdetail, name='reviewdetail'),

]
