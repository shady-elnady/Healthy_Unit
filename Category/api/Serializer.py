from rest_framework.serializers import HyperlinkedModelSerializer, ListSerializer

from ..models import Category

# Serializers define the API representation.


class CategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = [
            "url",
            "id",
            "name",
            "category_parent",
            "translations",
            "created_at",
            "last_updated",
        ]

