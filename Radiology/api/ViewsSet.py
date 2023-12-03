from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import (
    TokenAuthentication,
    SessionAuthentication,
    BasicAuthentication,
)
import django_filters.rest_framework

from .service_polymorphic_serializer import (
    ServicePolymorphicSerializer,
    ServiceRecordPolymorphicSerializer,
)
from ..models import Radiology, RadiologySession, RadiologyImage
from .Serializer import (
    RadiologyImageSerializer,
    RadiologySerializer,
    RadiologySessionSerializer,
)
from Service.models import Service, ServiceRecord


class ServicePolymorphicViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServicePolymorphicSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]


class ServiceRecordPolymorphicViewSet(ModelViewSet):
    queryset = ServiceRecord.objects.all()
    serializer_class = ServiceRecordPolymorphicSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]


class RadiologyViewSet(ModelViewSet):
    queryset = Radiology.objects.all()
    serializer_class = RadiologySerializer
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
    search_fields = ["name"]
    # This will be used as the default ordering
    ordering = "-last_updated"


class RadiologySessionViewSet(ModelViewSet):
    queryset = RadiologySession.objects.all()
    serializer_class = RadiologySessionSerializer
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
        "patient",
        "treating_doctor",
    ]
    # This will be used as the default ordering
    ordering = "-last_updated"


class RadiologyImageViewSet(ModelViewSet):
    queryset = RadiologyImage.objects.all()
    serializer_class = RadiologyImageSerializer
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
    # ordering_fields = ("id", "created_at", "last_updated")
    # filterset_fields = ["id", "created_at", "last_updated"]
    search_fields = [
        "RadiologySession",
    ]
    # This will be used as the default ordering
    # ordering = "-last_updated"
