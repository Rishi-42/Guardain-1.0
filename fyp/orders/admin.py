from django.contrib import admin
from .models import *

admin.site.register(OrderProduct)
admin.site.register(Order)
admin.site.register(Payment)