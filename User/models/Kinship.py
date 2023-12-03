# from django.db import models
from django.db.models import Model, BooleanField, CharField, ForeignKey, CASCADE
from django.utils.translation import gettext_lazy as _

from Utils.models.BaseModel import BaseAutoIncrementModel
from Utils.models.Choices import KINSHIP_RELATIONS
from .Profile import Profile

# Create your models here.


class kinshipRelation(BaseAutoIncrementModel):
    relationship_name = CharField(
        max_length=1,
        choices=KINSHIP_RELATIONS.choices,
        verbose_name=_("Relationship Name"),
    )
    is_only_one = BooleanField(
        default=False,
        verbose_name=_("is Only One"),
    )

    class Meta:
        verbose_name = _("kinship Relation")
        verbose_name_plural = _("kinship Relations")


class Kinship(Model):
    kinship_person = ForeignKey(
        Profile,
        on_delete=CASCADE,
        related_name="Relatives",
        verbose_name=_("Person"),
    )
    kinshiper = ForeignKey(
        Profile,
        on_delete=CASCADE,
        # related_name= "kinshipers",
        verbose_name=_("Kinshiper"),
    )
    relation = ForeignKey(
        kinshipRelation,
        on_delete=CASCADE,
        related_name="Persons+",
        verbose_name=_("relation"),
    )

    def __str__(self) -> str:
        return f"{self.kinship_person} > {self.kinshiper}"

    class Meta:
        unique_together = (
            "kinship_person",
            "kinshiper",
        )
        verbose_name = _("Kinship")
        verbose_name_plural = _("Kinships")
