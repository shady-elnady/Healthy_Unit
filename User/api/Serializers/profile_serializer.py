from rest_framework.serializers import HyperlinkedModelSerializer

from Language.api.Serializer import LanguageSerializer
from Address.api.Serializer import AddressSerializer
from Currency.api.Serializer import CurrencySerializer
from User.models.Profile import Profile
from .User_Serializer import UserSerializer
from .Family_Serializer import FamilySerializer
from .Avatar_Serializer import AvatarSerializer


class ProfileSerializer(HyperlinkedModelSerializer):
    user = UserSerializer(many=False)
    language = LanguageSerializer(many=False)
    currency = CurrencySerializer(many=False)
    address = AddressSerializer(many=False)
    family = FamilySerializer(many=False)
    Avatars = AvatarSerializer(many=True)

    class Meta:
        model = Profile
        fields = [
            "url",
            "id",
            "user",
            "image",
            "marital_status",
            "job",
            "family",
            "birth_date",
            "gender",
            "address",
            "currency",
            "language",
            "age",
            "Avatars",
            "created_at",
            "last_updated",
        ]
