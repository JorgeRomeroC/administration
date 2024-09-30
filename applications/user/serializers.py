from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'position', 'phone_number', 'photo', 'is_active', 'password1',
                  'password2']

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Las contraseñas no coinciden.")
        return data

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            position=validated_data['position'],
            phone_number=validated_data['phone_number'],
            photo=validated_data['photo'],
            is_active=validated_data['is_active'],
        )
        user.set_password(validated_data['password1'])
        user.save()
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'position', 'phone_number', 'photo', 'is_active']


class UserDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'position', 'phone_number', 'photo', 'is_active']