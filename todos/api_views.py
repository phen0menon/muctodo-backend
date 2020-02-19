from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from .models import *
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TodoGroupViewSet(viewsets.ModelViewSet):
    queryset = TodoGroup.objects.all()
    serializer_class = TodoGroupSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
