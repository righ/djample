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


class RecursiveField(serializers.Field):
    def to_representation(self, obj):
        parent = self.parent.__class__(obj, processed=self.parent.processed)
        if obj.id in self.parent.processed:
            return
        self.parent.processed.add(obj.id)
        return parent.data


class GroupSerializer(serializers.ModelSerializer):
    parent = RecursiveField()

    def __init__(self, *args, **kwargs):
        processed = kwargs.pop('processed', set())
        super().__init__(*args, **kwargs)
        self.processed = processed

    class Meta:
        model = Group
        fields = ('id', 'name', 'users', 'owner', 'parent')
        extra_kwargs = {
        }
