from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .api_views import *


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'todos', TodoViewSet)
router.register(r'todo_groups', TodoGroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', obtain_jwt_token),
    path('api-verify', verify_jwt_token),
]
