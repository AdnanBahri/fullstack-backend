from rest_framework import serializers
from django.utils.text import slugify
from .models import Category, Product, ProductImage, Brand, ProductType, ProductSpecification, ProductSpecificationValue


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["image", "alt_text"]


class SpecificationValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecificationValue
        fields = '__all__'


class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecification
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductTypeSerielizer(serializers.ModelSerializer):
    specification_values = SpecificationValueSerializer(many=True)

    class Meta:
        model = ProductType
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False, allow_blank=True)

    class Meta:
        model = Product
        fields = ["id", "category", "name", "is_active", "type", "description",
                  "price", "old_price", "slug", "created_at", "updated_at"]

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
