from rest_framework.serializers import HyperlinkedModelSerializer

from ..models import Client

# Serializers define the API representation.


class ClientSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = [
            "url",
            "id",
            "national_id",
            "email",
            "mobile",
            "created_at",
            "last_updated",
        ]

    extra_kwargs = {
        "url": {"view_name": "client-detail", "lookup_field": "id"},
    }
