from django.forms import ModelForm

from .models import PharmaceuticalForm, DrugEffectiveMaterial, Drug, DrugPacking


class PharmaceuticalFormAdminForm(ModelForm):
    class Meta:
        model = PharmaceuticalForm
        fields = [
            "name",
            "translations",
        ]


class DrugEffectiveMaterialAdminForm(ModelForm):
    class Meta:
        model = DrugEffectiveMaterial
        fields = [
            "name",
            "for_child_pregnant",
            # "drug_effective_material_category",
            "translations",
        ]


class DrugAdminForm(ModelForm):
    class Meta:
        model = Drug
        fields = [
            "name",
            "category",
            "brand",
            "drug_effective_material",
            "translations",
        ]
