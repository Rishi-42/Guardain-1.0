from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, PharmacistDetail, Type_user, CounsellorDetail, Adresses
# Register your models here


class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username',
                    'date_joined', 'last_login', 'user_type', 'is_active')
    list_display_links = ('email', 'username')
    readonly_feilds = ('date_joined', 'last_login')
    ordering = ('date_joined',)
    search_fields = ('email', 'username')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)


class Type_userAdmin(UserAdmin):
    list_display = ('user', 'is_administrator', 'is_customer',
                    'is_counsellor', 'is_pharmacist')
    list_display_links = ('user',)
    readonly_feilds = ('is_administrator', 'is_customer',
                       'is_counsellor', 'is_pharmacist')
    ordering = ('user',)
    search_fields = ('user',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Type_user, Type_userAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'province', 'district',
                    'city', 'ward_no', 'tole')


admin.site.register(Adresses, AddressAdmin)

admin.site.register(PharmacistDetail)
admin.site.register(CounsellorDetail)
