from rest_framework.serializers import HyperlinkedModelSerializer

from ...models.Family import Family


class FamilySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Family
        fields = [
            "url",
            "id",
            "name",
            "base_family",
            "created_at",
            "last_updated",
        ]
