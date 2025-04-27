# shipping/models.py
from django.db import models
from django.conf import settings

class Address(models.Model):
    full_name = models.CharField("Nom complet", max_length=255)
    address_line1 = models.CharField("Adresse ligne 1", max_length=255)
    address_line2 = models.CharField("Adresse ligne 2", max_length=255, blank=True)
    city = models.CharField("Ville", max_length=100)
    zip_code = models.CharField("Code postal", max_length=20)
    country = models.CharField("Pays", max_length=3)
    phone = models.CharField("Téléphone", max_length=20, blank=True)

    class Meta:
        abstract = True

class ShippingAddress(Address):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='shipping_addresses')
    default = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Adresse d'expédition"
        verbose_name_plural = "Adresses d'expédition"

class BillingAddress(Address):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='billing_addresses')
    default = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Adresse de facturation"
        verbose_name_plural = "Adresses de facturation"
