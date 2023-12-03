from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from django.db.models import JSONField
from django.contrib.gis.db import models
from mapwidgets.widgets import GooglePointFieldWidget
from Language.widgets.myTranslation_json_widget import MyTranslationWidget
from .models.Country import Country
from .models.Governorate import Governorate
from .models.City import City
from .models.State import State
from .models.Locality import Locality
from .models.Street import Street
from .models.Address import Address

from .forms import (
    CountryAdminForm,
    GovernorateAdminForm,
    CityAdminForm,
    StateAdminForm,
    LocalityAdminForm,
    StreetAdminForm,
    AddressAdminForm,
)

# Register your models here.


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    form = CountryAdminForm
    formfield_overrides = {
        JSONField: {
            "widget": MyTranslationWidget,
        },
    }


@admin.register(Governorate)
class GovernorateAdmin(admin.ModelAdmin):
    form = GovernorateAdminForm
    formfield_overrides = {
        JSONField: {
            "widget": MyTranslationWidget,
        },
    }


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    form = CityAdminForm
    formfield_overrides = {
        JSONField: {
            "widget": MyTranslationWidget,
        },
    }


@admin.register(State)
class StateAdmin(OSMGeoAdmin):
    form = StateAdminForm
    formfield_overrides = {
        JSONField: {
            "widget": MyTranslationWidget,
        },
    }


@admin.register(Locality)
class LocalityAdmin(OSMGeoAdmin):
    form = LocalityAdminForm
    formfield_overrides = {
        JSONField: {
            "widget": MyTranslationWidget,
        },
    }


@admin.register(Street)
class StreetAdmin(OSMGeoAdmin):
    form = StreetAdminForm
    formfield_overrides = {
        JSONField: {
            "widget": MyTranslationWidget,
        },
    }


@admin.register(Address)
class AddressAdmin(OSMGeoAdmin):
    form = AddressAdminForm
    formfield_overrides = {
        JSONField: {
            "widget": MyTranslationWidget,
        },
        models.PointField: {
            "widget": GooglePointFieldWidget,
        },
    }
