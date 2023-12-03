# from django.db import models
from django.db.models import CharField
from django.utils.translation import gettext_lazy as _

from Utils.models.Choices import MEDICAL_SPECIALTIES
from Employee.models import Employee

# Create your models here.


class Doctor(Employee):
    medical_specialty = CharField(
        max_length=2,
        choices=MEDICAL_SPECIALTIES.choices,
        verbose_name=_("Medical Specialty"),
    )  # تخصص طبي

    class Meta:
        verbose_name = _("Doctor")
        verbose_name_plural = _("Doctors")
