# from django.db import models
from django.db.models import (
    CharField,
    TextField,
    FloatField,
    ForeignKey,
    DateField,
    DateTimeField,
    BooleanField,
    CASCADE,
)
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now

from Utils.models.BaseModel import BaseAutoIncrementModel
from Utils.models.Choices import EMPLOYEE_ACTIVITIES
from User.models.User import User

# Create your models here.


class Employee(User):
    salary = FloatField(
        null=True,
        blank=True,
        verbose_name=_("Salary"),
    )

    class Meta:
        permissions = [
            (
                "set_published_status",
                "Can set the status of the post to either publish or not",
            )
        ]
        verbose_name = _("Employee")
        verbose_name_plural = _("Employees")


class Bonuss(BaseAutoIncrementModel):  # المكافاءت
    employee = ForeignKey(
        Employee,
        on_delete=CASCADE,
        related_name="%(class)s",
        verbose_name=_("Employee"),
    )
    _date = DateTimeField(
        default=now,
        verbose_name=_("Date"),
    )
    amount = FloatField(
        verbose_name=_("Amount"),
    )
    reason = TextField(
        null=True,
        blank=True,
        verbose_name=_("Reason"),
    )

    class Meta:
        verbose_name = _("Bonuss")
        verbose_name_plural = _("Bonusss")


class Deduction(BaseAutoIncrementModel):  # الخصومات
    employee = ForeignKey(
        Employee,
        on_delete=CASCADE,
        related_name=_("Deductions"),
        verbose_name=_("Employee"),
    )
    deduction_date = DateTimeField(
        default=now,
        verbose_name=_("Deduction Date"),
    )
    amount = FloatField(
        verbose_name=_("Amount"),
    )
    reason = TextField(
        null=True,
        blank=True,
        verbose_name=_("Reason"),
    )

    class Meta:
        verbose_name = _("Deduction")
        verbose_name_plural = _("Deductions")


class Vacation(BaseAutoIncrementModel):  # الاجازات
    employee = ForeignKey(
        Employee,
        on_delete=CASCADE,
        related_name=_("Vacations"),
        verbose_name=_("Employee"),
    )
    vacation_date = DateField(
        verbose_name=_("Vacation Date"),
    )
    is_accepted = BooleanField(
        default=True,
        verbose_name=_("is Accepted"),
    )
    is_paid = BooleanField(
        default=False,
        verbose_name=_("is Paid"),
    )

    class Meta:
        verbose_name = _("Vacation")
        verbose_name_plural = _("Vacations")


class Attendance(BaseAutoIncrementModel):  # الحضور والغياب
    employee = ForeignKey(
        Employee,
        on_delete=CASCADE,
        related_name=_("Attendances"),
        verbose_name=_("Employee"),
    )
    attending_time = DateTimeField(
        verbose_name=_("Attending Time"),
    )  # الحضور
    leaving_time = DateTimeField(
        verbose_name=_("Leaving Time"),
    )  # الانصراف

    @property
    def day_work_time(self):
        return self.leaving_time - self.attending_time

    class Meta:
        verbose_name = _("Laboratory Attendance")
        verbose_name_plural = _("Laboratory Attendances")
