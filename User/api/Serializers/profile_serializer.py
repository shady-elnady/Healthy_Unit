from rest_framework.serializers import HyperlinkedModelSerializer

from Language.api.Serializer import LanguageSerializer
from Address.api.Serializer import AddressSerializer
from Currency.api.Serializer import CurrencySerializer
from .family_serializer import FamilySerializer
from .user_serializer import UserSerializer
from ...models.Profile import Profile, ProfileImage


class ProfileImageSerializer(HyperlinkedModelSerializer):
        
        model = ProfileImage
        fields = [
            "url",
            "id",
            "profile",
            "image",
            "created_at",
            "last_updated",
        ]


class ProfileSerializer(HyperlinkedModelSerializer):
    user = UserSerializer(many=False)
    language = LanguageSerializer(many=False)
    currency = CurrencySerializer(many=False)
    address = AddressSerializer(many=False)
    family = FamilySerializer(many=False)
    ProfileImages = ProfileImageSerializer(many=True)

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
            "ProfileImages",
            "created_at",
            "last_updated",
        ]
