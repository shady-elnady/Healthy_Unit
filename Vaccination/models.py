# from django.db import models
from django.db.models import Model, DateField, ForeignKey, CASCADE
from django.utils.translation import gettext_lazy as _

from Service.models import Service, ServiceRecord
from Utils.models.BaseModel import BaseAutoIncrementModel


class Vaccination(Service):
    class Meta:
        verbose_name = _("Vaccination")
        verbose_name_plural = _("Vaccinations")


class Campaign(BaseAutoIncrementModel):
    vaccination = ForeignKey(
        Vaccination,
        on_delete=CASCADE,
        related_name="%(class)s",
        verbose_name=_("Vaccination"),
    )
    campaign_date = DateField(
        verbose_name=_("Campaign Date"),
    )

    class Meta:
        verbose_name = _("Campaign")
        verbose_name_plural = _("Campaigns")


class VaccinationRecord(ServiceRecord):
    class Meta:
        verbose_name = _("Vaccination Record")
        verbose_name_plural = _("Vaccinations Records")
