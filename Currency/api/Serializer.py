from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField

from ..models import Currency

# Serializers define the API representation.


class CurrencySerializer(HyperlinkedModelSerializer):
    native = SerializerMethodField("get_native_name")

    def get_native_name(self, obj) -> str:
        return obj.translations[self.context.get("user_language", "English")]

    class Meta:
        model = Currency
        fields = [
            "url",
            "id",
            "name",
            "native",
            "iso_code",
            "symbol",
            "created_at",
            "last_updated",
        ]
