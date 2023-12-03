from django.db.models import ForeignKey, PROTECT
from django.utils.translation import gettext_lazy as _

from Utils.models.BaseModel import BaseAutoIncrementNameModel


class Family(BaseAutoIncrementNameModel):
    base_family = ForeignKey(
        "self",
        null=True,
        blank=True,
        limit_choices_to={"base_family__isnull": True},
        on_delete=PROTECT,
        related_name="Sub_Families",
        verbose_name=_("Base Family"),
    )
    class Meta:
        verbose_name = _("Family")
        verbose_name_plural = _("Families")


