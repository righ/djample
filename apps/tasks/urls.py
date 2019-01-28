from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('status', views.StatusViewSet)
router.register('tag', views.TagViewSet)
router.register('task', views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
