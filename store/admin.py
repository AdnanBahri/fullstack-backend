from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (
    Category,
    Product,
    ProductImage,
    ProductSpecification,
    ProductSpecificationValue,
    ProductType,
    Brand
)

admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Brand)


class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification


class ProductSpecificationValueInline(admin.TabularInline):
    model = ProductSpecificationValue


class ProductImageInline(admin.TabularInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
    ]


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    filter_horizontal = ['specifications']


@admin.register(ProductSpecification)
class ProductSpecificationAdmin(admin.ModelAdmin):
    inlines = [
        ProductSpecificationValueInline,
    ]
