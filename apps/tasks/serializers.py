
from rest_framework import serializers

from .models import Status, Tag, Task, Time


class StatusListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'name')
        extra_kwargs = {}


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'name', 'description')
        extra_kwargs = {}


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name',)
        extra_kwargs = {}


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'user', 'group', 'created_at', 'updated_at')
        extra_kwargs = {
            'created_at': {'write_only': True},
            'updated_at': {'write_only': True},
        }


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'status', 'content', 'owner')
        extra_kwargs = {}


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = ('id', 'task', 'note', 'start', 'end')
        extra_kwargs = {}


class TaskSerializer(serializers.ModelSerializer):
    # times = TimeSerializer(many=True)
    class Meta:
        model = Task
        fields = ('id', 'status', 'content', 'tags', 'created_at', 'updated_at')
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'times': {'write_only': True},
        }
