# catalog/models.py
from django.db import models
from django.utils.text import slugify
from django.db.models import JSONField
from django.core.validators import MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    parent = models.ForeignKey(
        'self',
        null=True, blank=True,
        related_name='subcategories',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='categories/', null=True, blank=True)

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.parent.name + ' > ' if self.parent else ''}{self.name}"

# definition de la classe produit
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    attributes = JSONField(default=dict, blank=True)  # dimensions, matériau, etc.
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    main_image = models.ImageField(upload_to='products/main/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# classes pour gerer les options et variant de produits
class Option(models.Model):
    """
    Ex : 'Couleur', 'Taille', 'Matériau'
    """
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class OptionValue(models.Model):
    """
    Ex : pour Option('Couleur'): 'Rouge', 'Bleu'
    """
    option = models.ForeignKey(Option, related_name='values', on_delete=models.CASCADE)
    value = models.CharField(max_length=100)

    class Meta:
        unique_together = ('option', 'value')

    def __str__(self):
        return f"{self.option.name}: {self.value}"

# classe de variants de produits
class ProductVariant(models.Model):
    """
    Lie un Product à plusieurs OptionValue (couleur, taille…).
    """
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    sku = models.CharField(max_length=100, unique=True)
    option_values = models.ManyToManyField(OptionValue, related_name='variants')
    extra_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        values = ", ".join([str(v) for v in self.option_values.all()])
        return f"{self.product.name} [{values}]"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')
    order = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(3)])  # 0-3 pour max 4 images
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']
        unique_together = ['product', 'order']

    def __str__(self):
        return f"Image {self.order + 1} pour {self.product.name}"
