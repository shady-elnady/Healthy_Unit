from rest_framework.serializers import HyperlinkedModelSerializer

from User.api.Serializers.Profile_Serializer import ProfileSerializer
from ..models import Client

# Serializers define the API representation.


class ClientSerializer(HyperlinkedModelSerializer):
    Profile = ProfileSerializer(many=False)

    class Meta:
        model = Client
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
            "created_at",
            "last_updated",
        ]

    extra_kwargs = {
        "url": {"view_name": "client-detail", "lookup_field": "uid"},
    }
