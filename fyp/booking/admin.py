from django.contrib import admin
from .models import Meeting
# Register your models here.

class MeetingAdmin(admin.ModelAdmin):
    list_display = ('meeting_title', 'slug', 'client_age', 'meeting_date', 'meeting_time', 'marital_status', 'created_date', 'modified_date')
    prepopulated_fields = {'slug': ('meeting_title',)}

admin.site.register(Meeting, MeetingAdmin)