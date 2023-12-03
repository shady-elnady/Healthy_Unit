from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField

from Employee.api.Serializer import EmployeeSerializer
from User.api.Serializers.profile_serializer import ProfileSerializer

from ..models import Service, ParentService, ServiceRecord

# Serializers define the API representation.


class ServiceSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = [
            "url",
            "id",
            "name",
            "parent",
            "content_type",
            "translations",
            "created_at",
            "last_updated",
        ]


class ParentServiceSerializer(HyperlinkedModelSerializer):
    managing_director = EmployeeSerializer(many=False)

    class Meta:
        model = ParentService
        fields = [
            "url",
            "id",
            "name",
            "parent",
            "content_type",
            "managing_director",
            "translations",
            "created_at",
            "last_updated",
        ]


class ServiceRecordSerializer(HyperlinkedModelSerializer):
    service = ServiceSerializer(many=False)
    patient = ProfileSerializer(many=False)

    class Meta:
        model = ServiceRecord
        fields = [
            "url",
            "bar_code",
            "service",
            "patient",
            "diagnosis",
            "note",
            "content_type",
            "created_at",
            "last_updated",
        ]
