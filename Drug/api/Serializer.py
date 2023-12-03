from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField
from Brand.api.Serializer import BrandSerializer

from Category.api.Serializer import CategorySerializer
from Currency.api.Serializer import CurrencySerializer

from ..models import PharmaceuticalForm, DrugEffectiveMaterial, Drug, DrugPacking

# Serializers define the API representation.


class PharmaceuticalFormSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = PharmaceuticalForm
        fields = [
            "url",
            "id",
            "name",
            "translations",
            "created_at",
            "last_updated",
        ]


class DrugEffectiveMaterialSerializer(HyperlinkedModelSerializer):
    drug_effective_material_category = CategorySerializer(many=False)

    class Meta:
        model = DrugEffectiveMaterial
        fields = [
            "url",
            "id",
            "name",
            "for_child_pregnant",
            "drug_effective_material_category",
            "translations",
            "created_at",
            "last_updated",
        ]


class DrugPackingSerializer(HyperlinkedModelSerializer):
    pharmaceutical_form = PharmaceuticalFormSerializer(many=False)
    currency = CurrencySerializer(many=False)

    class Meta:
        model = DrugPacking
        fields = [
            "url",
            "id",
            "drug",
            "pharmaceutical_form",
            "price",
            "currency",
            "created_at",
            "last_updated",
        ]


class DrugSerializer(HyperlinkedModelSerializer):
    category = CategorySerializer(many=False)
    brand = BrandSerializer(many=False)
    drug_effective_material = DrugEffectiveMaterialSerializer(many=False)
    Drugs_Packing = DrugPackingSerializer(many=False)

    class Meta:
        model = Drug
        fields = [
            "url",
            "id",
            "name",
            "category",
            "brand",
            "drug_effective_material",
            "Drugs_Packing",
            "translations",
            "created_at",
            "last_updated",
        ]
