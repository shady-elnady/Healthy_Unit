from django.db.models import TextField, ForeignKey, CASCADE
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from Utils.models.BaseModel import BaseModel

# Create your models here.


UserModel = get_user_model()


class Notification(BaseModel):
    user = ForeignKey(
        UserModel,
        on_delete=CASCADE,
        related_name="Notifications",
        verbose_name=_("User"),
    )
    meassage = TextField(
        max_length=200,
        verbose_name=_("Meassage"),
    )

    class Meta:
        verbose_name = _("Notification")
        verbose_name_plural = _("Notifications")
