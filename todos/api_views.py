from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from .models import *
from .serializers import *
from rest_framework.exceptions import NotAuthenticated
from rest_framework.response import Response
from rest_framework import status as HTTPstatus
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi, inspectors
from drf_yasg.inspectors import SerializerInspector


def can_user_create_todos(request, related_user):
    return request.user.pk == related_user


custom_schemas = {
    "todogroup_create": {
        "operation_description": "Create todo group with todo items in it for currently logged in user",
        "request_body": openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['todo_group_data'],
            properties={
                'todo_group_data': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    required=['title'],
                    properties={"title": openapi.Schema(
                        type=openapi.TYPE_STRING, description="Title of todo group")}
                ),
                'todo_group_items': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        required=['content'],
                        properties={
                            "content": openapi.Schema(type=openapi.TYPE_STRING, description="Content of todo item"),
                            "remind_at": openapi.Schema(type=openapi.TYPE_STRING, description="Datetime in ISO8601 format")}
                    ))
            },
        ),
        "responses": {200: TodoGroupExtendedSerializer(many=True)}
    },

    "todogroup_list": {
        "operation_description": "Create todo group with todo items in it for currently logged in user",
        "responses": {200: TodoGroupExtendedSerializer(many=True)}
    }
}


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TodoGroupViewSet(viewsets.ModelViewSet):
    queryset = TodoGroup.objects.all()
    serializer_class = TodoGroupSerializer
    serializer_extended_class = TodoGroupExtendedSerializer

    @swagger_auto_schema(**custom_schemas['todogroup_create'])
    def create(self, request):
        todo_group_data = request.data.get('todo_group_data')
        todo_group_items = request.data.get('todo_group_items')

        todo_group_data['user'] = request.user.pk
        todo_group_serializer = self.get_serializer(data=todo_group_data)
        todo_group_serializer.is_valid(raise_exception=True)
        todo_group_instance = todo_group_serializer.save()

        todo_items_payload = [{**todo, 'group': todo_group_instance.pk}
                              for todo in todo_group_items]

        todo_items_serializer = TodoSerializer(
            data=todo_items_payload, many=True)
        todo_items_serializer.is_valid(raise_exception=True)
        todo_items_instances = todo_items_serializer.save()

        headers = self.get_success_headers(todo_group_serializer.data)
        return Response(
            todo_group_serializer.data,
            status=HTTPstatus.HTTP_201_CREATED,
            headers=headers
        )

    @swagger_auto_schema(**custom_schemas['todogroup_list'])
    def list(self, request):
        data = self.queryset.filter(user=request.user)
        serialized_data = self.serializer_extended_class(data, many=True)
        return Response(serialized_data.data)


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
