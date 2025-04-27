# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informations personnelles', {'fields': ('first_name', 'last_name', 'email', 'phone', 'address')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_vendor', 'groups', 'user_permissions')}),
    )
    list_display = ('username', 'email', 'is_vendor', 'is_staff')
    list_filter = ('is_vendor', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email')
