# apps/boutiques/admin.py
from django.contrib import admin
from django.core.exceptions import PermissionDenied
from .models import Boutique

@admin.register(Boutique)
class BoutiqueAdmin(admin.ModelAdmin):
    list_display    = ('name', 'user', 'city', 'shop_type')
    list_filter     = ('city', 'shop_type', 'categories')
    search_fields   = ('name', 'user__username', 'city', 'neighborhood')
    filter_horizontal = ('categories',)

    def has_add_permission(self, request):
        # Seuls les vendeurs peuvent créer leur boutique
        if not request.user.is_authenticated or not request.user.is_vendor:
            return False
        # empêche un vendeur de créer deux boutiques
        return not hasattr(request.user, 'boutique')

    def has_change_permission(self, request, obj=None):
        # Un vendeur ne peut modifier que sa boutique
        if obj is None:
            return super().has_change_permission(request, obj)
        return request.user.is_superuser or (obj.user == request.user)

    def has_delete_permission(self, request, obj=None):
        # On pourrait interdire la suppression pure si souhaité
        return request.user.is_superuser
