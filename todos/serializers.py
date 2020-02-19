from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'username', 'email']


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"


class TodoGroupSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True)

    class Meta:
        model = TodoGroup
        fields = "__all__"
