from django.contrib import admin
from .models import Province, District, City, Adresses
# Register your models here.
# admin.site.register(Province)


# admin.site.register(Person)

class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Province, ProvinceAdmin)


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'province')


admin.site.register(District, DistrictAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'district')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(City, CityAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'province', 'district',
                    'city', 'ward_no', 'tole')


admin.site.register(Adresses, AddressAdmin)
