from rest_framework.serializers import HyperlinkedModelSerializer, ListSerializer

from Category.api.Serializer import CategorySerializer
from Address.api.Serializer import CountrySerializer
from ..models import Brand

# Serializers define the API representation.


class BrandSerializer(HyperlinkedModelSerializer):
    category = CategorySerializer(many=False)
    made_in = CountrySerializer(many=False)

    class Meta:
        model = Brand
        fields = [
            "url",
            "id",
            "name",
            "category",
            "made_in",
            "image",
            "translations",
            "created_at",
            "last_updated",
        ]
