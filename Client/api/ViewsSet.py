from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import (
    TokenAuthentication,
    SessionAuthentication,
    BasicAuthentication,
)
import django_filters.rest_framework
from django.conf import settings

from .user_polymorphic_serializer import UserPolymorphicSerializer
from ..models import Client
from .Serializer import ClientSerializer
from User.models.User import User


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]
    filter_backends = (
        filters.OrderingFilter,  # http://example.com/api/users?ordering=account,username
        filters.SearchFilter,  # http://example.com/api/users?search=russell
        django_filters.rest_framework.DjangoFilterBackend,
    )
    ordering_fields = ("id", "created_at", "last_updated")
    filterset_fields = ["id", "created_at", "last_updated"]
    search_fields = [
        "national_id",
        "email",
        "mobile",
    ]
    # This will be used as the default ordering
    ordering = "-last_updated"


class UserPolymorphicViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserPolymorphicSerializer
    permission_classes = [IsAuthenticated]