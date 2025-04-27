# catalog/admin.py
from django.contrib import admin
from .models import Category, Product, Option, OptionValue, ProductVariant, ProductImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'image')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    fieldsets = (
        (None, {'fields': ('name', 'slug', 'parent', 'image')}),
    )

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    max_num = 4

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock_quantity', 'created', 'main_image')
    list_filter = ('category', 'created')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')
    date_hierarchy = 'created'
    inlines = [ProductImageInline]
    fieldsets = (
        (None, {'fields': ('name', 'slug', 'category', 'description', 'price', 'stock_quantity', 'main_image')}),
        ('Attributs avancés', {'fields': ('attributes',)}),
    )

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(OptionValue)
class OptionValueAdmin(admin.ModelAdmin):
    list_display = ('option', 'value')
    list_filter = ('option',)
    search_fields = ('value',)

class ProductVariantInline(admin.TabularInline):
    model = ProductVariant.option_values.through
    extra = 1

@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('product', 'sku', 'extra_price')
    inlines = [ProductVariantInline]
    filter_horizontal = ('option_values',)
