from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import CharField, EmailField, BooleanField
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from Utils.models.BaseModel import BaseUUIDTimeModel
from Utils.models.BaseTreeNode import BaseTreeNodeMultiModel
from ..managers.user_manager import UserManager

# Create your models here.


class User(
    BaseTreeNodeMultiModel,
    AbstractBaseUser,
    PermissionsMixin,
    BaseUUIDTimeModel,
):
    USERNAME_FIELD = "national_id"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = [
        "name",
        "email",
        "mobile",
        "password",
    ]

    mobile_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",  # ^(\+\d{1,3})?,?\s?\d{8,13}
        message=_(
            _(
                "Mobile Number must not consist of space and requires country code. eg : +6591258565."
            )
        ),
    )
    national_id_regex = RegexValidator(
        regex=r"^\d{14}$",  # ^(\+\d{1,3})?,?\s?\d{8,13}
        message=_("National ID must be 14 Numbers. eg : 11111111111111"),
    )

    objects = UserManager()
    name = CharField(
        max_length=100,
        unique=True,
        error_messages={"unique": _("The Name must Unique")},
        verbose_name=_("Name"),
    )
    otp = CharField(
        max_length=25,
        blank=True,
        null=True,
        verbose_name=_("OTP"),
    )
    national_id = CharField(
        max_length=14,
        unique=True,
        error_messages={"unique": _("National ID must Unique")},
        validators=[national_id_regex],
        verbose_name=_("National ID"),
    )
    email = EmailField(
        unique=True,
        error_messages={"unique": _("E-Mail Is Used")},
        verbose_name=_("E-mail"),
    )
    mobile = CharField(
        max_length=16,
        unique=True,
        validators=[mobile_regex],
        error_messages={"unique": _("Mobile Is Used")},
        verbose_name=_("Mobile"),
    )
    is_active = BooleanField(
        default=False,
        verbose_name=_("is Active"),
    )
    is_verified = BooleanField(
        default=False,
        verbose_name=_("is Verfied"),
    )
    email_verified = BooleanField(
        default=False,
        verbose_name=_("E-mail Verified"),
    )
    mobile_verified = BooleanField(
        default=False,
        verbose_name=_("Mobile Verified"),
    )
    is_superuser = BooleanField(
        default=False,
        verbose_name=_("is Super User"),
    )
    is_staff = BooleanField(
        default=False,
        verbose_name=_("is Staff"),
    )

    def __str__(self) -> str:
        return f"{self.email}"

    def __decode__(self) -> str:
        return f"{self.email}"

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
