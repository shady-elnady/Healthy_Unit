from rest_framework.serializers import Serializer, CharField
from django.utils.translation import gettext_lazy as _


class VerifyEmailSerializer(Serializer):
    key = CharField(write_only=True)
