from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
