from django.forms import ModelForm

from .models import VitalSign


class VitalSignAdminForm(ModelForm):
    class Meta:
        model = VitalSign
        fields = [
            "name",
            "min_normal",
            "max_normal",
            "unit",
            "translations",
        ]
