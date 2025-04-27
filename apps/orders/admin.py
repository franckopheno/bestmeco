# orders/admin.py
from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'ordered_at')
    list_filter = ('status', 'ordered_at')
    date_hierarchy = 'ordered_at'
    search_fields = ('user__username', 'id')
