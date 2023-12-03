# from django.db import models
from django.db.models import ForeignKey, CASCADE
from django.utils.translation import gettext_lazy as _
from Category.models import Category

from Utils.models.BaseModel import BaseImageModel
from Language.models.BaseTranslationModel import BaseTranslationModel
from Address.models.Country import Country

# Create your models here.


class Brand(BaseTranslationModel, BaseImageModel):
    category = ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=CASCADE,
        related_name="%(class)s+",
        verbose_name=_("Category"),
    )
    made_in = ForeignKey(
        Country,
        null=True,
        blank=True,
        on_delete=CASCADE,
        related_name="Made_Brands",
        verbose_name=_("Made In"),
    )

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")
