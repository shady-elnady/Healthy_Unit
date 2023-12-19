from rest_framework.serializers import Serializer, EmailField
from django.utils.translation import gettext_lazy as _


class ResendEmailVerificationSerializer(Serializer):
    email = EmailField(required=True)
