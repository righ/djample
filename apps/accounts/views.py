
from django.shortcuts import render
from rest_framework.decorators import api_view, action
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import authentication, permissions

from .models import User, Group
from .serializers import UserSerializer, GroupSerializer


@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})


class UserNameAPI(APIView):
    def get(self, request, format=None):
        usernames = [user.name for user in User.objects.all()]
        return Response(usernames)

    def post(self, request):
        # 普通こんなことはしないが..
        users = [User(username=name) for name in request.POST.getlist('name')]
        User.objects.bulk_create(users)
        return Response({'succeeded': True})


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['get'], detail=True)
    def gravatar(self, request, pk=None):
        user = self.get_object()
        return Response(user.gravatar(request.META['QUERY_STRING']))


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
