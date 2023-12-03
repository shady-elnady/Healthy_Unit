# from django.db import models
from django.db.models import Model, CharField, TextField, ForeignKey, CASCADE
from django.utils.translation import gettext_lazy as _

from Doctor.models import Doctor
from User.models.Profile import Profile
from Utils.models.BaseModel import BaseBarCodeModel
from Utils.models.Choices import LOW_OR_NORMAL_OR_HIGH, NEGATIVE_OR_POSITIVE
from VitalSign.models import VitalSign

# Create your models here.


class Visit(BaseBarCodeModel):
    doctor = ForeignKey(
        Doctor,
        on_delete=CASCADE,
        related_name="Visits",
        verbose_name=_("Doctor"),
    )
    patient = ForeignKey(
        Profile,
        on_delete=CASCADE,
        related_name="Visits",
        verbose_name=_("Patient"),
    )
    diagnosis = TextField(
        verbose_name=_("Diagnosis"),
    )

    class Meta:
        verbose_name = _("Visit")
        verbose_name_plural = _("Visits")


class VisitVitalSign(Model):  # المؤشرات الحيويه للمريض اثناء الزياره
    visit = ForeignKey(
        Visit,
        on_delete=CASCADE,
        related_name=_("Patient_Visit_Vital_Signs"),
        verbose_name=_("Visit"),
    )
    vital_sign = ForeignKey(
        VitalSign,
        on_delete=CASCADE,
        related_name=_("Prescriptions"),
        verbose_name=_("Vital Sign"),
    )
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
        unique_together = [
            [
                "visit",
                "vital_sign",
            ],
        ]
        verbose_name = _("Visit Vital Sign")
        verbose_name_plural = _("Visit Vital Signs")
