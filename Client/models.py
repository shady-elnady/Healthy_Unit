# from django.db.models import Model
from django.utils.translation import gettext_lazy as _

from User.models.User import User

# Create your models here.


class Client(User):
    class Meta:
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")

