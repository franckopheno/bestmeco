# apps/boutiques/models.py
from django.db import models
from django.conf import settings
from apps.catalog.models import Category  # réutiliser vos catégories

class Boutique(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='boutique'
    )
    name            = models.CharField("Nom de la boutique", max_length=255)
    city            = models.CharField("Ville", max_length=100)
    neighborhood    = models.CharField("Quartier", max_length=100)
    shop_type       = models.CharField("Type de boutique", max_length=100)
    categories      = models.ManyToManyField(
        Category,
        verbose_name="Catégories de la boutique",
        related_name='boutiques'
    )
    website         = models.URLField("Lien du site web", blank=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = "Boutique"
        verbose_name_plural = "Boutiques"

    def __str__(self):
        return f"{self.name} ({self.user.username})"
