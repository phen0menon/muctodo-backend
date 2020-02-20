from django.conf.urls import url
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import BasicAuthentication

schema_view = get_schema_view(
    openapi.Info(
        title="MUCTODO API",
        default_version='v1',
        description="MUCTodo REST API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=(JSONWebTokenAuthentication, BasicAuthentication)
)


urlpatterns = [
    path('swagger', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc'),
    path('', include("todos.router")),
]
