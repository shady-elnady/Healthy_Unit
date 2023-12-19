from rest_framework.serializers import HyperlinkedModelSerializer

from ...models.Profile import Avatar


class AvatarSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Avatar
        fields = [
            "url",
            "id",
            "profile",
            "image",
            "created_at",
            "last_updated",
        ]
