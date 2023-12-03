# from django.db import models
from django.contrib.gis.db.models import ForeignKey, CASCADE, LineStringField
from django.contrib.gis.geos import LineString
from django.utils.translation import gettext_lazy as _

from Language.models.BaseTranslationModel import BaseTranslationModel
from .State import State

# Create your models here.


class Street(BaseTranslationModel):
    """
    Metadata is stored in a PostgreSQL HStore field, which allows us to
    store arbitrary key-value pairs with a link record.
    """

    # metadata = HStoreField(blank=True, null=True, default=dict)
    # geo_polygon_location = LineStringField(
    #     verbose_name=_("Geo Polygon  Location"),
    # )

    state = ForeignKey(
        State,
        on_delete=CASCADE,
        related_name=_("Streets"),
        verbose_name=_("State"),
    )
    geo_location = LineStringField(
        null=True,
        blank=True,
        srid=4326,
        default=LineString(
            (
                (31.419106717505198, 31.121382139307993),
                (31.42402052441989, 31.11952681573342),
                (31.42402052441989, 31.119379857860135),
                (31.424385304846126, 31.119269639306054),
                (31.424664254583305, 31.119012462181804),
            )
        ),
        verbose_name=_("Geo Location"),
    )

    class Meta:
        verbose_name = _("Street")
        verbose_name_plural = _("Streets")
