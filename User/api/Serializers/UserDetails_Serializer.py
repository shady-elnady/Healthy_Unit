from rest_framework.serializers import ModelSerializer
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from User.models.User import User


class UserDetailsSerializer(ModelSerializer):
    """
    User model w/o password
    """

    @staticmethod
    def validate_national_id(national_id):
        return national_id

    class Meta:
        extra_fields = []
        # see https://github.com/iMerica/dj-rest-auth/issues/181
        # User.XYZ causing attribute error while importing other
        # classes from `serializers.py`. So, we need to check whether the auth model has
        # the attribute or not
        if hasattr(User, "USERNAME_FIELD"):
            extra_fields.append(User.USERNAME_FIELD)
        if hasattr(User, "EMAIL_FIELD"):
            extra_fields.append(User.EMAIL_FIELD)
        if hasattr(User, "first_name"):
            extra_fields.append("first_name")
        if hasattr(User, "last_name"):
            extra_fields.append("last_name")
        model = User
        fields = ("pk", *extra_fields)
        read_only_fields = ("email",)
