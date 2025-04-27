# orders/models.py
from django.db import models
from django.conf import settings
from apps.cart.models import Cart

class Order(models.Model):
    STATUS_CHOICES = [
        ('P', 'En attente'),
        ('C', 'Confirmée'),
        ('S', 'Expédiée'),
        ('R', 'Reçue'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cart = models.OneToOneField(Cart, on_delete=models.PROTECT)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commande #{self.id} – {self.get_status_display()}"
