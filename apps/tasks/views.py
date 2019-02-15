from datetime import timedelta

from django.shortcuts import render
from django.utils import timezone

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
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TagSerializer
        else:
            return TagListSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TaskSerializer
        else:
            return TaskListSerializer

    @action(methods=['get'], detail=True)
    def times(self, request, pk=None):
        task = self.get_object()
        ts = [
            TimeSerializer(t).data
            for t in task.times.all()
        ]
        return Response(ts)

    @action(methods=['get'], detail=True)
    def seconds(self, request, pk=None):
        task = self.get_object()
        total = sum([
            (t.end or timezone.now()) - t.start
            for t in task.times.all()
        ], timedelta())
        return Response(total.total_seconds())



class TimeRecordView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    queryset = Time.objects.all()
    serializer_class = TimeSerializer
