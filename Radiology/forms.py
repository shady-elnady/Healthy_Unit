from django.forms import ModelForm

from .models import Radiology


class RadiologyAdminForm(ModelForm):
    class Meta:
        model = Radiology
        fields = [
            "name",
            "translations",
        ]
