from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email')
        extra_kwargs = {
            'password': {'write_only': True},
        }
