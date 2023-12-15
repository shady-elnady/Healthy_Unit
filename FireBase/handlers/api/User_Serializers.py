from rest_framework.serializers import ModelSerializer

from User.models.User import User


class UserBaseSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "uid",
            "name",
            "display_name",
            "national_id",
            "email",
            "phone_number",
            "photo_url",
        ]


class UserCreateSerializer(UserBaseSerializer):
    """ """


class UserPutOrPatchSerializer(UserBaseSerializer):
    """ """


class UserDetailSerializer(UserBaseSerializer):
    """ """


class UserListSerializer(UserBaseSerializer):
    class Meta:
        model = User
        fields = UserBaseSerializer.Meta.fields + [
            "uid",
        ]
