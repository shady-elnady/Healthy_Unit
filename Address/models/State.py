# from django.db import models
from django.contrib.gis.db.models import PolygonField, CharField, ForeignKey, CASCADE
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.geos import Polygon
import h3

from Utils.models.Choices import STATES_TYPES
from Language.models.BaseTranslationModel import BaseTranslationModel
from .City import City

# Create your models here.


class State(BaseTranslationModel):
    city = ForeignKey(
        City,
        on_delete=CASCADE,
        related_name=_("Areas"),
        verbose_name=_("City"),
    )
    postal_code = CharField(
        max_length=5,
        null=True,
        blank=True,
        verbose_name=_("Postal Code"),
    )
    state_type = CharField(
        max_length=2,
        choices=STATES_TYPES.choices,
        default=STATES_TYPES.VILLAGE,
        verbose_name=_("State Type"),
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
        verbose_name = _("State")
        verbose_name_plural = _("States")


"""

https://stackoverflow.com/questions/51159241/how-to-generate-shapefiles-for-h3-hexagons-in-a-particular-area

"""
