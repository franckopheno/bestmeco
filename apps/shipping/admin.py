# shipping/admin.py
from django.contrib import admin
from .models import ShippingAddress, BillingAddress

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'city', 'zip_code', 'country', 'default')
    list_filter = ('country', 'default')
    search_fields = ('user__username', 'full_name', 'city', 'zip_code')

@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'city', 'zip_code', 'country', 'default')
    list_filter = ('country', 'default')
    search_fields = ('user__username', 'full_name', 'city', 'zip_code')
