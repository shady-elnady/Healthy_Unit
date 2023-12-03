# from django.db import models
from django.contrib.gis.db.models import ForeignKey, CASCADE, PointField
from django.contrib.gis.geos import Point
from django.utils.translation import gettext_lazy as _

from Language.models.BaseTranslationModel import BaseTranslationModel
from .Street import Street
from .Locality import Locality

# Create your models here.


class Address(BaseTranslationModel):
    locality = ForeignKey(
        Locality,
        on_delete=CASCADE,
        related_name=_("Address"),
        verbose_name=_("Locality"),
    )
    street = ForeignKey(
        Street,
        null=True,
        blank=True,
        on_delete=CASCADE,
        related_name=_("Address"),
        verbose_name=_("Street"),
    )
    geo_location = PointField(
        null=True,
        blank=True,
        geography=True,
        srid=4326,
        default=Point(31.419106717505198, 31.121382139307993),
        verbose_name=_("Geo Location"),
    )

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Address")


"""
>>> from django.contrib.gis.geos import GEOSGeometry
>>> pnt = GEOSGeometry('POINT(5 23)') # WKT
>>> pnt = GEOSGeometry('010100000000000000000014400000000000003740') # HEX
>>> pnt = GEOSGeometry(buffer('\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14@\x00\x00\x00\x00\x00\x007@'))
>>> pnt = GEOSGeometry('{ "type": "Point", "coordinates": [ 5.000000, 23.000000 ] }') # GeoJSON
"""