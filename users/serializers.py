from rest_framework import serializers
from .models import CustomerProfile, Address
from django.contrib.auth import get_user_model


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class CustomerProfileSerializer(serializers.ModelSerializer):
    # user_addresses = AddressSerializer(many=True)

    class Meta:
        model = CustomerProfile
        fields = ['avatar', 'phone', 'user_addresses',
                  'user', 'created_at', 'updated_at']
        read_only_fields = ('user',)


class CustomerSerializer(serializers.ModelSerializer):
    profile = CustomerProfileSerializer(required=False)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'password', 'created_at',
                  'updated_at', 'profile', 'is_active', 'is_staff', 'is_superuser']
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('profile',)

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user
