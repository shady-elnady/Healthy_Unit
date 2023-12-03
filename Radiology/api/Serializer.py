from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField
from Client.api.Serializer import ClientSerializer

from Doctor.api.Serializer import DoctorSerializer

from ..models import Radiology, RadiologySession, RadiologyImage

# Serializers define the API representation.


class RadiologySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Radiology
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


class RadiologyImageSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = RadiologyImage
        fields = [
            "url",
            "RadiologySession",
            "image",
        ]


class RadiologySessionSerializer(HyperlinkedModelSerializer):
    Radiologies_Images = RadiologyImageSerializer(many=True)

    class Meta:
        model = RadiologySession
        fields = [
            "url",
            "bar_code",
            "service",
            "patient",
            "note",
            "diagnosis",
            "content_type",
            "Radiologies_Images",
            "created_at",
            "last_updated",
        ]
