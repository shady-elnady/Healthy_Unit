from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import CharField, EmailField, BooleanField
from django.utils.translation import gettext_lazy as _

from Utils.models.BaseModel import BaseUUIDTimeModel
from Utils.models.BaseTreeNode import BaseTreeNodeMultiModel
from Utils.Assets.messages import Messages
from Utils.Validators.Regex_Validators import RegexValidators
from .managers.user_manager import UserManager

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
        "phone_number",
        "password",
    ]

    objects = UserManager()
    name = CharField(
        max_length=100,
        unique=True,
        error_messages={"unique": Messages.NAME_UNIQUE_VALIDATION},
        validators=[RegexValidators.name_regex],
        verbose_name=_("Name"),
    )
    display_name = CharField(
        max_length=25,
        unique=True,
        error_messages={"unique": Messages.DISPLAY_NAME_UNIQUE_VALIDATION},
        blank=True,
        null=True,
        verbose_name=_("Display Name"),
    )
    national_id = CharField(
        max_length=14,
        unique=True,
        error_messages={"unique": Messages.NATIONAL_ID_UNIQUE_VALIDATION},
        validators=[RegexValidators.national_id_regex],
        verbose_name=_("National ID"),
    )
    email = EmailField(
        unique=True,
        error_messages={"unique": Messages.EMAIL_UNIQUE_VALIDATION},
        verbose_name=_("E-mail"),
    )
    phone_number = CharField(
        max_length=16,
        unique=True,
        error_messages={"unique": Messages.PHONE_UNIQUE_VALIDATION},
        validators=[RegexValidators.phone_number_regex],
        verbose_name=_("Phone Number"),
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
    phone_number_verified = BooleanField(
        default=False,
        verbose_name=_("Phone Number Verified"),
    )
    is_superuser = BooleanField(
        default=False,
        verbose_name=_("is Super User"),
    )
    is_staff = BooleanField(
        default=False,
        verbose_name=_("is Staff"),
    )
    disabled = BooleanField(
        default=False,
        verbose_name=_("Disabled"),
    )

    def __str__(self) -> str:
        return f"{self.display_name}"

    def __decode__(self) -> str:
        return f"{self.display_name}"

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["-last_updated"]
