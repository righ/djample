from django.contrib.auth.hashers import make_password
from rest_framework import serializers, validators

from .models import User, Group


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[validators.UniqueValidator(queryset=User.objects.all(), message='そのユーザは既にいます')])

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'file', 'belongs')
        extra_kwargs = {
            'gravatar': {'read_only': True},
            'password': {'write_only': True},
        }

    def validate_belongs(self, values):
        print('values', values)
        request = self.context['request']
        for value in values:
            group = Group.objects.filter(id=value.id).first()
            if group and group.owner_id != request.user.id:
                raise serializers.ValidationError('このグループにユーザを追加する権限がありません')


class RecursiveField(serializers.Field):
    def to_representation(self, obj):
        parent = self.parent.__class__(obj, processed=self.parent.processed)
        if obj.id in self.parent.processed:
            return
        self.parent.processed.add(obj.id)
        return parent.data

    def to_internal_value(self, data):
        return data


class GroupSerializer(serializers.ModelSerializer):
    parent = RecursiveField()

    def __init__(self, *args, **kwargs):
        processed = kwargs.pop('processed', set())
        super().__init__(*args, **kwargs)
        self.processed = processed

    class Meta:
        model = Group
        fields = ('id', 'name', 'users', 'owner', 'parent')
        extra_kwargs = {}

    def validate_parent(self, value):
        groups = set()
        group = Group.objects.filter(id=value).first()
        while group:
            if group in groups:
                raise serializers.ValidationError('循環してます')
            groups.add(group)
            group = Group.objects.filter(id=value).first()
        return value
