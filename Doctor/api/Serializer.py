from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField

from User.api.Serializers.Profile_Serializer import ProfileSerializer
from ..models import Doctor

# Serializers define the API representation.


class DoctorSerializer(HyperlinkedModelSerializer):
    Profile = ProfileSerializer(many=False)

    class Meta:
        model = Doctor
        fields = [
            "url",
            "uid",
            "name",
            "display_name",
            "national_id",
            "email",
            "phone_number",
            "photo_url",
            "Profile",
            "salary",
            "medical_specialty",
            "created_at",
            "last_updated",
        ]

    extra_kwargs = {
        "url": {"view_name": "doctor-detail", "lookup_field": "id"},
    }
