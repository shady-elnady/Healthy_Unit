from django.utils.translation import gettext_lazy as _
from rest_framework.serializers import ModelSerializer

from User.models.TokenModel import TokenModel


class TokenSerializer(ModelSerializer):
    """
    Serializer for Token model.
    """

    class Meta:
        model = TokenModel
        fields = ("key",)
