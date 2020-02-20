from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from .models import *
from .serializers import *
from rest_framework.exceptions import NotAuthenticated
from rest_framework.response import Response
from rest_framework import status as HTTPstatus


def can_user_create_todos(request, related_user):
    return request.user.pk == related_user


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TodoGroupViewSet(viewsets.ModelViewSet):
    queryset = TodoGroup.objects.all()
    serializer_class = TodoGroupSerializer
    serializer_extended_class = TodoGroupExtendedSerializer

    def create(self, request):
        todo_group_data = request.data.get('todo_group_data')
        todo_group_items = request.data.get('todo_group_items')

        todo_group_data['user'] = request.user.pk
        todo_group_serializer = self.get_serializer(data=todo_group_data)
        todo_group_serializer.is_valid(raise_exception=True)
        todo_group_instance = todo_group_serializer.save()

        todo_items_payload = [{**todo, 'group': todo_group_instance.pk}
                              for todo in todo_group_items]

        todo_items_serializer = TodoSerializer(data=todo_items_payload, many=True)
        todo_items_serializer.is_valid(raise_exception=True)
        todo_items_instances = todo_items_serializer.save()

        headers = self.get_success_headers(todo_group_serializer.data)
        return Response(
            todo_group_serializer.data,
            status=HTTPstatus.HTTP_201_CREATED,
            headers=headers
        )

    def list(self, request):
        data = self.queryset.filter(user=request.user)
        serialized_data = self.serializer_extended_class(data, many=True)
        return Response(serialized_data.data)


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
