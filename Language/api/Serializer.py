from rest_framework.serializers import HyperlinkedModelSerializer

from ..models.Language import Language

# Serializers define the API representation.


class LanguageSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = [
            "url",
            "id",
            "name",
            "native",
            "iso_639_1",
            "iso_639_2T",
            "is_bidi",
            "created_at",
            "last_updated",
        ]
