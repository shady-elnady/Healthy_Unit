# from django.db import models
from django.db.models import PositiveSmallIntegerField, OneToOneField, CASCADE
from django.utils.translation import gettext_lazy as _

from Utils.models.BaseModel import BaseAutoIncrementNameModel
from .Profile import Profile

# Create your models here.


class NickName(BaseAutoIncrementNameModel):
    user = OneToOneField(
        Profile,
        on_delete=CASCADE,
        related_name=_("Nick_Name"),
        verbose_name=_("User"),
    )

    class Meta:
        verbose_name = _("Nick Name")
        verbose_name_plural = _("Nick Names")
