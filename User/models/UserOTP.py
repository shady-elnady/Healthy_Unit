from django.db.models import (
    CharField,
    BooleanField,
    DateTimeField,
    ForeignKey,
    CASCADE,
)
from django.contrib.auth.hashers import check_password
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from datetime import timedelta

from Utils.models.BaseModel import BaseModel
from .User import User


class UserOTP(BaseModel):
    user = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name="Profile",
        verbose_name=_("User"),
    )
    otp = CharField(
        max_length=100,
        verbose_name=_("OTP"),
    )
    expiry = DateTimeField(
        blank=True,
        null=True,
        verbose_name=_("Expiry"),
    )
    is_verified = BooleanField(
        default=False,
        help_text=_("Whether the OTP has been used to log into the system."),
        verbose_name=_("is Verfied"),
    )

    def __str__(self):
        return f"OTP for '{self.user.name}' created on {self.created_at.date()} at {self.created_at.time()}."

    def save(self, *args, **kwargs):
        self.expiry = self.created_at + timedelta(minutes=settings.OTP_EXPIRY_MINUTES)
        super(UserOTP, self).save(*args, **kwargs)

    def authenticate_otp(self, otp: str = None):
        return check_password(password=otp, encoded=self.otp)

    class Meta:
        verbose_name = "User One-Time-Password"
        verbose_name_plural = "User One-Time-Passwords"
        ordering = ("-created_at",)
