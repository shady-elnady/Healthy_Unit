from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    EmailField,
)

from User.models.User import User

# Serializers define the API representation.


class UserSerializer(ModelSerializer):
    password = CharField(write_only=True)

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
            "password",
        ]

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserUpdateSerializer(ModelSerializer):
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
        read_only_fields = [
            "uid",
            "national_id",
        ]


class UserEmailUpdateSerializer(ModelSerializer):
    uid = CharField(required=True)
    email = EmailField(required=True)

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
        read_only_fields = [
            "uid",
            "national_id",
        ]
