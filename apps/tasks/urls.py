from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('statuses', views.StatusViewSet)
router.register('tags', views.TagViewSet)
router.register('tasks', views.TaskViewSet)

urlpatterns = [
    path('record/', views.TimeRecordView.as_view()),
    path('', include(router.urls)),
]
