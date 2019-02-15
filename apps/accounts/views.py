
from django.shortcuts import render
from rest_framework.decorators import api_view, action
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.authtoken.models import Token

from .models import User, Group
from .serializers import UserSerializer, GroupSerializer
from .permissions import GroupMemberPermission
#from .authentications import ExpirationTokenAuthentication

class CheckView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (
        #authentication.SessionAuthentication, 
        authentication.BasicAuthentication, 
        #authentication.TokenAuthentication,
    )
    def get(self, request, format=None):
        content = {'user': str(request.user), 'auth': str(request.auth)}
        return Response(content)


class SessionView(APIView):
    authentication_classes = (
        authentication.SessionAuthentication, 
        #authentication.BasicAuthentication, 
        #authentication.TokenAuthentication,
    )
    def get(self, request):
        return Response({'session': request.session.session_key})


class TokenView(APIView):
    authentication_classes = (
        #authentication.SessionAuthentication, 
        #authentication.BasicAuthentication, 
        authentication.TokenAuthentication,
        #ExpirationTokenAuthentication,
    )
    def get(self, request):
        user_id = request.user.id
        if not user_id:
            return Response({'token': None})
        token, _ = Token.objects.get_or_create(user_id=user_id)
        return Response({'token': str(token)})


@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})


class UserNameAPI(APIView):
    def get(self, request, format=None):
        usernames = [user.name for user in User.objects.all()]
        return Response(usernames)


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
    permission_classes = (permissions.IsAuthenticated, GroupMemberPermission,)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    @action(methods=['get'], detail=True)
    def users(self, request, pk=None):
        group = self.get_object()
        serializer = UserSerializer(group.users.all(), many=True)
        return Response(serializer.data)
