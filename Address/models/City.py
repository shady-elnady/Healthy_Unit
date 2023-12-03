# from django.db import models
from django.db.models import ForeignKey, CASCADE
from django.utils.translation import gettext_lazy as _

from Language.models.BaseTranslationModel import BaseTranslationModel
from .Country import Country
from .Governorate import Governorate

# Create your models here.


class City(BaseTranslationModel):
    city_country = ForeignKey(
        Country,
        on_delete=CASCADE,
        related_name=_("Cities"),
        verbose_name=_("Country"),
    )
    city_governorate = ForeignKey(
        Governorate,
        null=True,
        blank=True,
        on_delete=CASCADE,
        related_name=_("Cities"),
        verbose_name=_("Governorate"),
    )

    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")
