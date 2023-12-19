from rest_framework.serializers import (
    Serializer,
    CharField,
    SerializerMethodField,
    DateTimeField,
)
from django.utils.translation import gettext_lazy as _

from .UserDetails_Serializer import UserDetailsSerializer


class JWTSerializer(Serializer):
    """
    Serializer for JWT authentication.
    """

    access = CharField()
    refresh = CharField()
    user = SerializerMethodField()

    def get_user(self, obj):
        """
        Required to allow using custom USER_DETAILS_SERIALIZER in
        JWTSerializer. Defining it here to avoid circular imports
        """
        JWTUserDetailsSerializer = UserDetailsSerializer

        user_data = JWTUserDetailsSerializer(obj["user"], context=self.context).data
        return user_data


class JWTSerializerWithExpiration(JWTSerializer):
    """
    Serializer for JWT authentication with expiration times.
    """

    access_expiration = DateTimeField()
    refresh_expiration = DateTimeField()
