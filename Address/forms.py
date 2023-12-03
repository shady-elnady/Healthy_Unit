from django.forms import ModelForm

from .models.Country import Country
from .models.Governorate import Governorate
from .models.City import City
from .models.State import State
from .models.Locality import Locality
from .models.Street import Street
from .models.Address import Address


class CountryAdminForm(ModelForm):
    class Meta:
        model = Country
        fields = [
            "id",
            "name",
            "continent",
            "capital",
            "flag_emoji",
            "currency",
            "language",
            "tel_code",
            "time_zones",
            "translations",
        ]


class GovernorateAdminForm(ModelForm):
    class Meta:
        model = Governorate
        fields = [
            "id",
            "name",
            "governorate_country",
            "governorate_tel_code",
            "translations",
        ]


class CityAdminForm(ModelForm):
    class Meta:
        model = City
        fields = [
            "id",
            "name",
            "city_country",
            "city_governorate",
            "translations",
        ]


class StateAdminForm(ModelForm):
    class Meta:
        model = State
        fields = [
            "id",
            "name",
            "city",
            "postal_code",
            "state_type",
            "geo_location",
            "translations",
        ]

    # def __init__(self, *args, **kwargs):
    #     super(StateAdminForm, self).__init__(*args, **kwargs)
    #     states = State.objects.all()
    #     print(states.first().geo_location)
    #     if not self.fields["geo_location"] and len(states) > 0 and states.first().geo_location is not None:
    #         self.fields["geo_location"].initial = (
    #             states.first().geo_location,
    #         )


class LocalityAdminForm(ModelForm):
    class Meta:
        model = Locality
        fields = [
            "id",
            "name",
            "state",
            "geo_location",
            "translations",
        ]


class StreetAdminForm(ModelForm):
    class Meta:
        model = Street
        fields = [
            "id",
            "name",
            "state",
            "geo_location",
            "translations",
        ]


class AddressAdminForm(ModelForm):
    class Meta:
        model = Address
        fields = [
            "id",
            "name",
            "locality",
            "street",
            "geo_location",
            "translations",
        ]


# https://stackoverflow.com/questions/59916324/django-how-to-save-google-maps-polygon-area-javascript-code-to-view
