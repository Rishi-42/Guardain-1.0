from django.contrib import admin
from .models import BlogModel

class Add_blogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(BlogModel, Add_blogAdmin)

# Register your models here.

