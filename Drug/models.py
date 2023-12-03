# from django.db import models
from django.db.models import FloatField, BooleanField, ForeignKey, CASCADE
from django.utils.translation import gettext_lazy as _

from Language.models.BaseTranslationModel import BaseTranslationModel
from Category.models import Category
from Currency.models import Currency
from Brand.models import Brand
from Utils.models.BaseModel import BaseBarCodeModel, BaseImageModel

# Create your models here.


class PharmaceuticalForm(BaseTranslationModel):
    class Meta:
        verbose_name = _("Pharmaceutical Form")
        verbose_name_plural = _("Pharmaceutical Forms")


class DrugEffectiveMaterial(BaseTranslationModel):
    for_child_pregnant = BooleanField(
        default=True,
        verbose_name=_("for Child Pregnant"),
    )
    drug_effective_material_category = ForeignKey(
        Category,
        on_delete=CASCADE,
        related_name="%(class)s+",
        limit_choices_to={"category_parent__name__isequ": "Drug"},
        verbose_name=_("Drug Effective Material Category"),
    )  # الشكل الصيدلي

    class Meta:
        verbose_name = _("Drug Effective Material")
        verbose_name_plural = _("Drug Effective Materials")


class Drug(BaseTranslationModel):
    category = ForeignKey(
        Category,
        limit_choices_to={"category_parent__isnull": False},
        on_delete=CASCADE,
        related_name="%(class)s",
        verbose_name=_("Category"),
    )
    brand = ForeignKey(
        Brand,
        null=True,
        blank=True,
        on_delete=CASCADE,
        related_name="%(class)s",
        verbose_name=_("Brand"),
    )
    drug_effective_material = ForeignKey(
        DrugEffectiveMaterial,
        on_delete=CASCADE,
        related_name="%(class)s",
        verbose_name=_("Drug Effective Material"),
    )  # الماده الفاعله

    class Meta:
        verbose_name = _("Drug")
        verbose_name_plural = _("Drugs")


class DrugPacking(BaseBarCodeModel, BaseImageModel):
    drug = ForeignKey(
        Drug,
        on_delete=CASCADE,
        related_name="Drugs_Packing",
        verbose_name=_("Drug"),
    )
    pharmaceutical_form = ForeignKey(
        PharmaceuticalForm,
        on_delete=CASCADE,
        related_name="Drugs",
        verbose_name=_("Pharmaceutical Form"),
    )  # الشكل الصيدلي
    price = FloatField(
        verbose_name=_("Price"),
    )
    currency = ForeignKey(
        Currency,
        on_delete=CASCADE,
        related_name="%(class)s+",
        verbose_name=_("Currency"),
    )

    class Meta:
        verbose_name = _("Drug Packing")
        verbose_name_plural = _("Drugs Packings")
