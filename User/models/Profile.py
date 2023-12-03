from django.db.models import (
    CharField,
    PositiveSmallIntegerField,
    OneToOneField,
    ForeignKey,
    DateField,
    CASCADE,
    PROTECT,
)
from django.utils.translation import gettext_lazy as _
from datetime import date
import calendar

from Utils.models.BaseModel import (
    BaseImageModel,
    AgeModel,
    BaseModel,
    BaseTimeStampModel,
)
from Utils.models.Choices import GENDERS, JOBS, MARITAL_STATUS
from Language.models.Language import Language
from Currency.models import Currency
from Address.models.Address import Address
from .Family import Family
from .User import User


class Profile(BaseTimeStampModel, BaseImageModel):
    user = OneToOneField(
        User,
        on_delete=CASCADE,
        related_name="Profile",
        verbose_name=_("User"),
    )
    marital_status = CharField(
        max_length=1,
        null=True,
        blank=True,
        choices=MARITAL_STATUS.choices,
        verbose_name=_("Marital Status"),
    )  # الحاله الاجتماعيه
    job = CharField(
        max_length=2,
        null=True,
        blank=True,
        choices=JOBS.choices,
        verbose_name=_("Job"),
    )
    family = ForeignKey(
        Family,
        on_delete=PROTECT,
        blank=True,
        null=True,
        related_name=_("Persons"),
        verbose_name=_("Family"),
    )
    birth_date = DateField(
        blank=True,
        null=True,
        verbose_name=_("Birth Date"),
    )
    gender = CharField(
        max_length=1,
        blank=True,
        null=True,
        choices=GENDERS.choices,
        verbose_name=_("Gender"),
    )
    address = ForeignKey(
        Address,
        on_delete=PROTECT,
        blank=True,
        null=True,
        related_name="%(class)s",
        verbose_name=_("Address"),
    )
    currency = ForeignKey(
        Currency,
        on_delete=PROTECT,
        blank=True,
        null=True,
        related_name=_("Persons"),
        verbose_name=_("Currency"),
    )
    language = ForeignKey(
        Language,
        on_delete=PROTECT,
        blank=True,
        null=True,
        related_name=_("Persons"),
        verbose_name=_("Language"),
    )

    @property
    def age(self):
        born = self.birth_date
        calendar.setfirstweekday(calendar.SUNDAY)
        today = date.today()
        if today.month >= born.month:
            year = today.year
        else:
            year = today.year - 1
        age_years = year - born.year
        try:  # raised when birth day is February 29 and the current year is not a leap year
            age_days = (today - (born.replace(year=year))).days
        except ValueError:
            age_days = (today - (born.replace(year=year, day=born.day - 1))).days + 1
        month = born.month
        age_months = 0
        while age_days > calendar.monthrange(year, month)[1]:
            age_days = age_days - calendar.monthrange(year, month)[1]
            if month == 12:
                month = 1
                year += 1
            else:
                month += 1
            age_months += 1
        return AgeModel(
            year=age_years,
            month=age_months,
            day=age_days,
        )

    def __str__(self) -> str:
        return f"{self.user.name}"

    def __decode__(self) -> str:
        return f"{self.user.name}"

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")


class ProfileImage(BaseModel, BaseImageModel):
    profile = ForeignKey(
        Profile,
        on_delete=CASCADE,
        related_name="%(class)s",
        verbose_name=_("Profile"),
    )
    position = PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=_("Position"),
    )

    class Meta:
        verbose_name = _("Profile Image")
        verbose_name_plural = _("Profiles Images")
