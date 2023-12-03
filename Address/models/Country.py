# from django.db import models
from django.db.models import CharField, ForeignKey, OneToOneField, CASCADE, TextChoices
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
import pytz

from Language.models.BaseTranslationModel import BaseTranslationModel
from Language.models.Language import Language
from Currency.models import Currency

# Create your models here.


class Country(BaseTranslationModel):
    tel_code_regex = RegexValidator(
        regex=r"^\+?1?\d{1,3}$",
        message=_(
            "Country Telephone Code must be entered in the format: '+999'. Up to 3 digits allowed."
        ),
    )

    ## https://en.wikipedia.org/wiki/ISO_3166-1#Current_codes
    class CONTINENTS(TextChoices):
        AFRICA = "AF", _("Africa")
        ASIA = "AS", _("Asia")
        EUROPE = "EU", _("Europe")
        NORTH_AMERICA = "NA", _("North America")
        OCEANIA = "OC", _("Oceania")
        SOUTH_AMERICA = "SA", _("South America")
        ANTARCTICA = "AN", _("Antarctica")

    ALL_TIMEZONES = sorted((item, item) for item in pytz.all_timezones)

    continent = CharField(
        max_length=2,
        choices=CONTINENTS.choices,
        verbose_name=_("Continent Name"),
    )
    capital = OneToOneField(
        to="Address.City",
        on_delete=CASCADE,
        null=True,
        blank=True,
        related_name=_("Capital To +"),
        verbose_name=_("Capital"),
    )
    flag_emoji = CharField(
        max_length=5,
        null=True,
        blank=True,
        verbose_name=_("Flag Emoji"),
    )
    currency = ForeignKey(
        Currency,
        on_delete=CASCADE,
        related_name=_("Countries"),
        verbose_name=_("Currency"),
    )
    language = ForeignKey(
        Language,
        on_delete=CASCADE,
        related_name=_("Countries"),
        verbose_name=_("language"),
    )
    tel_code = CharField(
        max_length=3,
        null=True,
        blank=True,
        validators=[tel_code_regex],
        verbose_name=_("Telphone Code"),
    )
    time_zones = CharField(
        max_length=32,
        null=True,
        blank=True,
        choices=ALL_TIMEZONES,
        verbose_name=_("Time Zones"),
    )

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")


# TODO API FOR COUNTRIES
# https://restcountries.com/#api-endpoints-v3
# https://gitlab.com/restcountries/restcountries

## pip install python-restcountries
# https://github.com/SteinRobert/python-restcountries
""" 
    {
        "name": {
            "common": "Egypt",
            "official": "Arab Republic of Egypt",
            "nativeName": {
                "ara": {
                    "official": "جمهورية مصر العربية",
                    "common": "مصر"
                }
            }
        },
        "tld": [
            ".eg",
            ".مصر"
        ],
        "cca2": "EG",
        "ccn3": "818",
        "cca3": "EGY",
        "cioc": "EGY",
        "independent": true,
        "status": "officially-assigned",
        "unMember": true,
        "currencies": {
            "EGP": {
                "name": "Egyptian pound",
                "symbol": "£"
            }
        },
        "idd": {
            "root": "+2",
            "suffixes": [
                "0"
            ]
        },
        "capital": [
            "Cairo"
        ],
        "altSpellings": [
            "EG",
            "Arab Republic of Egypt"
        ],
        "region": "Africa",
        "subregion": "Northern Africa",
        "languages": {
            "ara": "Arabic"
        },
        "translations": {
            "ara": {
                "official": "جمهورية مصر العربية",
                "common": "مصر"
            },
            "ces": {
                "official": "Egyptská arabská republika",
                "common": "Egypt"
            },
            "cym": {
                "official": "Gweriniaeth Arabaidd yr Aifft",
                "common": "Yr Aifft"
            },
            "deu": {
                "official": "Arabische Republik Ägypten",
                "common": "Ägypten"
            },
            "est": {
                "official": "Egiptuse Araabia Vabariik",
                "common": "Egiptus"
            },
            "fin": {
                "official": "Egyptin arabitasavalta",
                "common": "Egypti"
            },
            "fra": {
                "official": "République arabe d'Égypte",
                "common": "Égypte"
            },
            "hrv": {
                "official": "Arapska Republika Egipat",
                "common": "Egipat"
            },
            "hun": {
                "official": "Egyiptomi Arab Köztársaság",
                "common": "Egyiptom"
            },
            "ita": {
                "official": "Repubblica araba d'Egitto",
                "common": "Egitto"
            },
            "jpn": {
                "official": "エジプト·アラブ共和国",
                "common": "エジプト"
            },
            "kor": {
                "official": "이집트 아랍 공화국",
                "common": "이집트"
            },
            "nld": {
                "official": "Arabische Republiek Egypte",
                "common": "Egypte"
            },
            "per": {
                "official": "جمهوری عربی مصر",
                "common": "مصر"
            },
            "pol": {
                "official": "Arabska Republika Egiptu",
                "common": "Egipt"
            },
            "por": {
                "official": "República Árabe do Egipto",
                "common": "Egito"
            },
            "rus": {
                "official": "Арабская Республика Египет",
                "common": "Египет"
            },
            "slk": {
                "official": "Egyptská arabská republika",
                "common": "Egypt"
            },
            "spa": {
                "official": "República Árabe de Egipto",
                "common": "Egipto"
            },
            "swe": {
                "official": "Arabrepubliken Egypten",
                "common": "Egypten"
            },
            "urd": {
                "official": "مصری عرب جمہوریہ",
                "common": "مصر"
            },
            "zho": {
                "official": "阿拉伯埃及共和国",
                "common": "埃及"
            }
        },
        "latlng": [
            27,
            30
        ],
        "landlocked": false,
        "borders": [
            "ISR",
            "LBY",
            "PSE",
            "SDN"
        ],
        "area": 1002450,
        "demonyms": {
            "eng": {
                "f": "Egyptian",
                "m": "Egyptian"
            },
            "fra": {
                "f": "Égyptienne",
                "m": "Égyptien"
            }
        },
        "flag": "🇪🇬",
        "maps": {
            "googleMaps": "https://goo.gl/maps/uoDRhXbsqjG6L7VG7",
            "openStreetMaps": "https://www.openstreetmap.org/relation/1473947"
        },
        "population": 102334403,
        "gini": {
            "2017": 31.5
        },
        "fifa": "EGY",
        "car": {
            "signs": [
                "ET"
            ],
            "side": "right"
        },
        "timezones": [
            "UTC+02:00"
        ],
        "continents": [
            "Africa"
        ],
        "flags": {
            "png": "https://flagcdn.com/w320/eg.png",
            "svg": "https://flagcdn.com/eg.svg"
        },
        "coatOfArms": {
            "png": "https://mainfacts.com/media/images/coats_of_arms/eg.png",
            "svg": "https://mainfacts.com/media/images/coats_of_arms/eg.svg"
        },
        "startOfWeek": "sunday",
        "capitalInfo": {
            "latlng": [
                30.05,
                31.25
            ]
        },
        "postalCode": {
            "format": "#####",
            "regex": "^(\\d{5})$"
        }
    }
"""
