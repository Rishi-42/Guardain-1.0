from django.contrib import admin
from .models import UploadPrescription


class UploadAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'prescription', 'prescripted_by', 'prescripted_for')
                   


admin.site.register(UploadPrescription, UploadAdmin)