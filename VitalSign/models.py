# from django.db import models
from django.db.models import (
    CharField,
    FloatField,
    ForeignKey,
    CASCADE,
)
from django.utils.translation import gettext_lazy as _

from Language.models.BaseTranslationModel import BaseTranslationModel
from Utils.models.Choices import UNIT

# Create your models here.


class VitalSign(BaseTranslationModel):
    min_normal = FloatField(
        null=True,
        blank=True,
        verbose_name=_("Minmum Normal Value"),
    )
    max_normal = FloatField(
        null=True,
        blank=True,
        verbose_name=_("Maximum Normal Value"),
    )
    unit = CharField(
        max_length=10,
        choices=UNIT.choices,
        null=True,
        blank=True,
        verbose_name=_("Unit"),
    )

    class Meta:
        verbose_name = _("Vital Sign")
        verbose_name_plural = _("Vital Signs")
