from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User, Group


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'file')
        extra_kwargs = {
            'gravatar': {'read_only': True},
            'password': {'write_only': True},
        }


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', 'users', 'owner')
        extra_kwargs = {
        }
