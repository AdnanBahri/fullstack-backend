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


class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification


class ProductSpecificationValueInline(admin.StackedInline):
    model = ProductSpecificationValue
    extra = 1


class ProductImageInline(admin.TabularInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
    ]
    filter_horizontal = ['specifications']


@admin.register(ProductSpecification)
class ProductSpecificationAdmin(admin.ModelAdmin):
    inlines = [
        ProductSpecificationValueInline,
    ]



admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Brand)
admin.site.register(ProductType)
# admin.site.register(ProductSpecification)
# admin.site.register(ProductSpecificationValue)