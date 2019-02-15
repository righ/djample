from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)

urlpatterns = [
    path('hello/', views.hello_world),
    path('check/', views.CheckView.as_view()),
    path('session/', views.SessionView.as_view()),
    path('token/', views.TokenView.as_view()),
    path('names/', views.UserNameAPI.as_view()),
    path('list/', views.UserList.as_view()),
    path('', include(router.urls)),
]
