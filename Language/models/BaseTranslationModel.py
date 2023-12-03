# from django.db import models
from django.db.models import JSONField
from django.utils.translation import gettext_lazy as _

from Utils.models.BaseModel import BaseAutoIncrementNameModel

# Create your model


class BaseTranslationModel(BaseAutoIncrementNameModel):
    translations = JSONField(
        null=True,
        blank=True,
        verbose_name=_("Translations"),
    )

    class Meta:
        abstract = True
