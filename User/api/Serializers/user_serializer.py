from rest_framework.serializers import HyperlinkedModelSerializer

from User.models.User import User
from .Profile_Serializer import ProfileSerializer


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
