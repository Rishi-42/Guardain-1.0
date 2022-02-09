from django.contrib import admin
from .models import Add_product, Category


class Add_productAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'slug', 'image', 'cost', 'stock', 'category', 'created_date', 'modified_date')
    prepopulated_fields = {'slug': ('product_name',)}


class CatogaryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'slug', 'created_date', 'modified_date')
    prepopulated_fields = {'slug': ('category_name',)}




# register Add_product model and Category model
admin.site.register(Add_product, Add_productAdmin)
admin.site.register(Category, CatogaryAdmin)

