from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework_gis.serializers import (
    GeoModelSerializer,
    GeoFeatureModelSerializer,
    GeometryField,
    GeometrySerializerMethodField,
)
from django.contrib.gis.geos import Point, Polygon
from Currency.api.Serializer import CurrencySerializer
from Language.api.Serializer import LanguageSerializer

from ..models.Address import Address
from ..models.Locality import Locality
from ..models.Street import Street
from ..models.State import State
from ..models.City import City
from ..models.Governorate import Governorate
from ..models.Country import Country


class CountrySerializer(HyperlinkedModelSerializer):
    currency = CurrencySerializer(many=False)
    language = LanguageSerializer(many=False)

    class Meta:
        model = Country
        fields = [
            "url",
            "id",
            "name",
            "continent",
            "capital",
            "flag_emoji",
            "currency",
            "language",
            "tel_code",
            "time_zones",
            "translations",
            "created_at",
            "last_updated",
        ]


class GovernorateSerializer(HyperlinkedModelSerializer):
    governorate_country = CountrySerializer(many=False)

    class Meta:
        model = Governorate
        fields = [
            "url",
            "id",
            "name",
            # "native",
            "governorate_country",
            "governorate_tel_code",
            "translations",
            "created_at",
            "last_updated",
        ]


class CitySerializer(HyperlinkedModelSerializer):
    city_country = CountrySerializer(many=False)
    city_governorate = GovernorateSerializer(many=False)

    class Meta:
        model = City
        fields = [
            "url",
            "id",
            "name",
            "city_country",
            "city_governorate",
            "translations",
            "created_at",
            "last_updated",
        ]


class StateSerializer(GeoFeatureModelSerializer):
    city = CitySerializer(many=False)

    class Meta:
        model = State
        geo_field = "geo_location"
        fields = [
            "url",
            "id",
            "name",
            "city",
            "postal_code",
            "state_type",
            "geo_location",
            "translations",
            "created_at",
            "last_updated",
        ]


class StreetSerializer(GeoFeatureModelSerializer):
    state = StateSerializer(many=False)
    geo_location = GeometryField()
    class Meta:
        model = Street
        geo_field = "geo_location"
        fields = [
            "url",
            "id",
            "name",
            "state",
            "geo_location",
            "translations",
            "created_at",
            "last_updated",
        ]
        auto_bbox = True

    # def get_properties(self, instance, fields):
    #     # This is a PostgreSQL HStore field, which django maps to a dict
    #     return instance.metadata

    # def unformat_geojson(self, feature):
    #     attrs = {
    #         self.Meta.geo_field: feature["geometry"],
    #         "metadata": feature["properties"],
    #     }

    #     if self.Meta.bbox_geo_field and "bbox" in feature:
    #         attrs[self.Meta.bbox_geo_field] = Polygon.from_bbox(feature["bbox"])

    #     return attrs


class LocalitySerializer(GeoFeatureModelSerializer):
    state = StateSerializer(many=False)
    geo_location = GeometryField()

    class Meta:
        model = Locality
        fields = [
            "url",
            "id",
            "name",
            "state",
            "geo_location",
            "translations",
            "created_at",
            "last_updated",
        ]
        geo_field = "geo_location"
        auto_bbox = True
        # bbox_geo_field = 'bbox_geometry'


class AddressSerializer(GeoModelSerializer):
    locality = LocalitySerializer(many=False)
    street = StreetSerializer(many=False)
    geo_location = GeometryField()

    class Meta:
        model = Address
        fields = [
            "url",
            "id",
            "name",
            "locality",
            "street",
            "geo_location",
            "translations",
            "created_at",
            "last_updated",
        ]
        geo_field = "geo_location"
