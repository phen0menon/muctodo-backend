from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .api_views import UserViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
