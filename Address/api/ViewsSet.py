import base64
from datetime import datetime
from django.contrib.auth import authenticate

from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status, filters
from django.core.exceptions import ObjectDoesNotExist
import django_filters.rest_framework
from rest_framework_gis.pagination import GeoJsonPagination
from rest_framework_gis.filters import (
    InBBoxFilter,
    DistanceToPointOrderingFilter,
    TMSTileFilter,
    DistanceToPointFilter,
)

from ..models.Address import Address
from ..models.Locality import Locality
from ..models.Street import Street
from ..models.State import State
from ..models.City import City
from ..models.Governorate import Governorate
from ..models.Country import Country
from .Serializer import (
    AddressSerializer,
    StateSerializer,
    LocalitySerializer,
    CitySerializer,
    CountrySerializer,
    GovernorateSerializer,
    StreetSerializer,
)

# import pyotp


class AddressViewSet(ModelViewSet):
    """
    API endpoint that allows Addresss to be viewed or edited.
    """

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
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


"""
    ?page=1&size=15&sorters[0]

    http://example.com/api/users?ordering=account,username

"""


class StreetViewSet(ModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (
        InBBoxFilter,
        DistanceToPointFilter,
        DistanceToPointOrderingFilter,
        TMSTileFilter,
        filters.OrderingFilter,
    )
    pagination_class = GeoJsonPagination
    bbox_filter_field = "point"
    bbox_filter_include_overlapping = True  # Optional


# class StreetGeojsonLocationList(generics.ListCreateAPIView):
#     # -- other omitted view attributes --- #
#     pagination_class = GeoJsonPagination

# class StreetList(ListAPIView):
#     queryset = Street.objects.all()
#     serializer_class = StreetSerializer
#     bbox_filter_field = 'point'
#     filter_backends = (InBBoxFilter,)
#     bbox_filter_include_overlapping = True # Optional


# https://github.com/openwisp/django-rest-framework-gis#using-geometryserializermethodfield-as-geo_field
# https://docs.djangoproject.com/en/2.0/ref/contrib/gis/functions/


class LocalityViewSet(ModelViewSet):
    queryset = Locality.objects.all()
    serializer_class = LocalitySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.OrderingFilter,)
    # Explicitly specify which fields the API may be ordered against
    ordering_fields = ("id", "created_at", "name")
    # This will be used as the default ordering
    ordering = "last_updated"


class StateViewSet(ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.OrderingFilter,)
    # Explicitly specify which fields the API may be ordered against
    ordering_fields = ("id", "created_at", "name")
    # This will be used as the default ordering
    ordering = "last_updated"


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (
        filters.OrderingFilter,
        # DjangoFilterBackend,
    )
    # Explicitly specify which fields the API may be ordered against
    ordering_fields = ("id", "created_at", "name")
    # This will be used as the default ordering
    ordering = "last_updated"


class GovernorateViewSet(ModelViewSet):
    queryset = Governorate.objects.all()
    serializer_class = GovernorateSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (
        filters.OrderingFilter,
        # DjangoFilterBackend,
    )
    # Explicitly specify which fields the API may be ordered against
    ordering_fields = ("id", "created_at", "name")
    # This will be used as the default ordering
    ordering = "last_updated"


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (
        filters.OrderingFilter,  # http://example.com/api/users?ordering=account,username
        filters.SearchFilter,  # http://example.com/api/users?search=russell
        django_filters.rest_framework.DjangoFilterBackend,
    )
    ordering_fields = ("id", "created_at", "last_updated")
    filterset_fields = ["id", "created_at", "last_updated"]
    search_fields = [
        "name",
        "continent",
        "capital",
        "flag_emoji",
        "currency",
        "language",
        "tel_code",
        "time_zones",
    ]
    # This will be used as the default ordering
