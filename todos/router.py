from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .api_views import *


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'todos', TodoViewSet)
router.register(r'todo_groups', TodoGroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
