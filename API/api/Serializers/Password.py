from rest_framework.serializers import Serializer, CharField, EmailField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

# User = get_user_model()


class ResetPasswordEmailSerializer(Serializer):
    email = EmailField(required=True)


class ChangePasswordSerializer(Serializer):
    old_password = CharField(required=True)
    new_password = CharField(required=True)
