# from django.db import models
from django.contrib.gis.db.models import PolygonField, ForeignKey, CASCADE
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.geos import Polygon

from Language.models.BaseTranslationModel import BaseTranslationModel
from .State import State

# Create your models here.


class Locality(BaseTranslationModel):
    state = ForeignKey(
        State,
        on_delete=CASCADE,
        related_name=_("Areas"),
        verbose_name=_("State"),
    )
    geo_location = PolygonField(
        null=True,
        blank=True,
        geography=True,
        srid=4326,
        default=Polygon(
            (
                (31.419075961717734, 31.12482780296244),
                (31.41688727916211, 31.120492692203932),
                (31.426843639023275, 31.11593693869261),
                (31.42911815226795, 31.120713126343354),
                (31.419075961717734, 31.12482780296244),
            )
        ),
        verbose_name=_("Geo Location"),
    )

    class Meta:
        verbose_name = _("Locality")
        verbose_name_plural = _("Localities")
