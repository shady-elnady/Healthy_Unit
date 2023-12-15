from rest_framework.serializers import HyperlinkedModelSerializer

from .profile_serializer import ProfileSerializer
from ...models.User import User


class UserSerializer(HyperlinkedModelSerializer):
    Profile = ProfileSerializer(many=False)

    class Meta:
        model = User
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
        ]
        extra_kwargs = {"password": {"write_only": True}}


"""

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        instance.email = instance.email.lower()
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

"""
