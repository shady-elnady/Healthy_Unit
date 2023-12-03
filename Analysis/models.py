# from django.db import models
from django.db.models import CharField, FloatField, ForeignKey, CASCADE
from django.utils.translation import gettext_lazy as _

# from django.utils.translation import get_language

from Utils.models.Choices import LOW_OR_NORMAL_OR_HIGH, NEGATIVE_OR_POSITIVE, UNIT
from Service.models import Service, ServiceRecord

# Create your models here.


class Analysis(Service):
    symbol = CharField(
        max_length=10,
        unique=True,
        verbose_name=_("Symbol"),
    )
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
        verbose_name = _("Analysis")
        verbose_name_plural = _("Analysis")


class Report(ServiceRecord):
    result = CharField(
        verbose_name=_("Result"),
    )
    neg_or_pos = CharField(
        max_length=2,
        choices=NEGATIVE_OR_POSITIVE.choices,
        null=True,
        blank=True,
        verbose_name=_("Description(Positive/Negative)"),
    )
    description_level = CharField(
        max_length=1,
        choices=LOW_OR_NORMAL_OR_HIGH.choices,
        verbose_name=_("Description Level"),
    )

    class Meta:
        verbose_name = _("Report")
        verbose_name_plural = _("Reports")
