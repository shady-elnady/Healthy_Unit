# from django.db import models
from django.db.models import TextField, ForeignKey, CASCADE
from django.utils.translation import gettext_lazy as _

from Utils.models.BaseModel import BaseAutoIncrementModel, BaseImageModel
from Service.models import Service, ServiceRecord
from Doctor.models import Doctor

# Create your models here.


class Radiology(Service):
    class Meta:
        verbose_name = _("Radiology")
        verbose_name_plural = _("Radiologies")


class RadiologySession(ServiceRecord):
    class Meta:
        verbose_name = _("Radiology Session")
        verbose_name_plural = _("Radiologies Sessions")


class RadiologyImage(BaseImageModel, BaseAutoIncrementModel):
    RadiologySession = ForeignKey(
        RadiologySession,
        on_delete=CASCADE,
        related_name="Radiologies_Images",
        verbose_name=_("Radiology Session"),
    )

    class Meta:
        verbose_name = _("Radiology Image")
        verbose_name_plural = _("Radiologies Images")


##  https://pyradiomics.readthedocs.io/en/latest/installation.html
