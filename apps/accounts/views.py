
from django.shortcuts import render
from rest_framework.decorators import api_view, action
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import pagination
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser, MultiPartParser

from apps.parsers import YamlParser
from .models import User, Group
from .serializers import UserSerializer, GroupSerializer
from .permissions import GroupMemberPermission
from .authentication import ExpirationTokenAuthentication


class EchoView(APIView):
    parser_classes = [YamlParser]

    def post(self, request):
        return Response(request.data)


class CheckView(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    authentication_classes = [ExpirationTokenAuthentication]
    
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


class MyNumberPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 50
    last_page_strings = ['-1']


class MyLOPagination(pagination.LimitOffsetPagination):
    default_limit = 1
    max_limit = 10


class MyCursorPagination(pagination.CursorPagination):
    ordering = ['email']
    page_size = 1


@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})


class UserNameAPI(APIView):
    def get(self, request, format=None):
        usernames = [user.name for user in User.objects.all()]
        return Response(usernames)


from rest_framework import filters
#from django_filters.rest_framework import DjangoFilterBackend


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        # DjangoFilterBackend,
    ]
    filter_fields = ('name',)
    search_fields = ('name', '^email')
    ordering_fields = ('id', 'name')

    #pagination_class = MyNumberPagination
    #pagination_class = MyLOPagination
    #pagination_class = MyCursorPagination




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = [
        # JSONParser,
        MultiPartParser,
    ]

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

