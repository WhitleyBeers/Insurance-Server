from rest_framework import serializers
from businessapi.models import User


class UserSerializer(serializers.ModelSerializer):
    """json serializer for users"""
    class Meta:
        model = User
        fields = ('id',
                  'email',
                  'first_name',
                  'last_name',
                  'phone_number',
                  'image',
                  'uid')


class CreateUserSerializer(serializers.ModelSerializer):
    """json serializer for creating users"""
    class Meta:
        model = User
        fields = ('id',
                  'email',
                  'first_name',
                  'last_name',
                  'address',
                  'phone_number',
                  'image')
