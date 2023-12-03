from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField

from ..models import Doctor

# Serializers define the API representation.


class DoctorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            "url",
            "id",
            "name",
            "national_id",
            "email",
            "mobile",
            "salary",
            "medical_specialty",
            "created_at",
            "last_updated",
        ]

    extra_kwargs = {
        "url": {"view_name": "doctor-detail", "lookup_field": "id"},
    }
