from rest_framework import serializers
from insuranceapi.models import User


class UserSerializer(serializers.ModelSerializer):
    """json serializer for users"""
    class Meta:
        model = User
        fields = ('id',
                  'email',
                  'first_name',
                  'last_name',
                  'address',
                  'phone_number',
                  'profile_image_url',
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
                  'profile_image_url')
