from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AuthUser
# Register your models here.


class AuthUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'birth', 'date_joined', 'last_login', 'is_active')
    list_display_links = ('username', 'email')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(AuthUser, AuthUserAdmin)