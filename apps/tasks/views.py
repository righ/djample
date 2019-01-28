
from django.shortcuts import render
from rest_framework import mixins
from rest_framework.decorators import api_view, action
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import authentication, permissions

from .models import (
    Status,
    Tag,
    Task,
    Time,
)
from .serializers import (
    StatusListSerializer,
    StatusSerializer,
    TagListSerializer,
    TagSerializer,
    TaskListSerializer,
    TaskSerializer,
    TimeSerializer,
)


class StatusViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return StatusSerializer
        else:
            return StatusListSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TagSerializer
        else:
            return TagListSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TaskSerializer
        else:
            return TaskListSerializer
