from rest_framework import serializers
from django.utils.text import slugify
from .models import Category, Product, ProductImage, Brand, ProductType, Specification, SpecificationValue, ProductVariant, Detail, ProductColor


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["image", "alt_text"]


class SpecificationValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificationValue
        fields = '__all__'


class SpecificationSerializer(serializers.ModelSerializer):
    specification_values = SpecificationValueSerializer(many=True)

    class Meta:
        model = Specification
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        fields = '__all__'


class ProductTypeSerielizer(serializers.ModelSerializer):
    # specification_values = SpecificationValueSerializer(many=True)

    class Meta:
        model = ProductType
        fields = '__all__'


class VariantSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False, allow_blank=True)
    specifications = SpecificationSerializer(many=True)

    class Meta:
        model = ProductVariant
        fields = ["id", "category", "name", "product", "is_active", "specifications", "color",
                  "price", "old_price", "slug", "variant_images", "created_at", "updated_at"]

    def create(self, validated_data):
        name = validated_data.get('name')
        slug = validated_data.get('slug')

        if not slug:
            slug = slugify(name)

        validated_data['slug'] = slug
        return super().create(validated_data)

    def update(self, instance, validated_data):
        name = validated_data.get('name')
        slug = validated_data.get('slug')

        if not slug:
            slug = slugify(name)

        validated_data['slug'] = slug
        return super().update(instance, validated_data)


class ProductSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False, allow_blank=True)

    class Meta:
        model = Product
        fields = ["id", "category", "name", "is_active", "type", "description", "brand",
                  "price", "slug", "product_images", "created_at", "updated_at"]

    def create(self, validated_data):
        name = validated_data.get('name')
        slug = validated_data.get('slug')

        if not slug:
            slug = slugify(name)

        validated_data['slug'] = slug
        return super().create(validated_data)

    def update(self, instance, validated_data):
        name = validated_data.get('name')
        slug = validated_data.get('slug')

        if not slug:
            slug = slugify(name)

        validated_data['slug'] = slug
        return super().update(instance, validated_data)


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False, allow_blank=True)

    class Meta:
        model = Category
        fields = ["name", "slug", "parent"]

    def create(self, validated_data):
        name = validated_data.get('name')
        slug = validated_data.get('slug')

        if not slug:
            slug = slugify(name)

        validated_data['slug'] = slug
        return super().create(validated_data)

    def update(self, instance, validated_data):
        name = validated_data.get('name')
        slug = validated_data.get('slug')

        if not slug:
            slug = slugify(name)

        validated_data['slug'] = slug
        return super().update(instance, validated_data)
