from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField

from ..models import VitalSign

# Serializers define the API representation.


class VitalSignSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = VitalSign
        fields = [
            "url",
            "id",
            "name",
            "min_normal",
            "max_normal",
            "unit",
            "created_at",
            "last_updated",
        ]
