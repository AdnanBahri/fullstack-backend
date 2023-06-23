from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (
    Category,
    Product,
    ProductImage,
    Specification,
    SpecificationValue,
    ProductType,
    Brand,
    Detail,
    ProductColor,
    ProductVariant
)


class SpecificationInline(admin.TabularInline):
    model = Specification


class SpecificationValueInline(admin.StackedInline):
    model = SpecificationValue
    extra = 1


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductColorInline(admin.TabularInline):
    model = ProductColor


class ProductDetailInline(admin.TabularInline):
    model = Detail


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
    ]


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    inlines = [
        SpecificationValueInline,
    ]


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
    ]
    filter_horizontal = ['specifications']


admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Brand)
admin.site.register(ProductType)
admin.site.register(Detail)
admin.site.register(ProductColor)
