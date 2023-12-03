from django.forms import ModelForm

from .models import Analysis


class AnalysisAdminForm(ModelForm):
    class Meta:
        model = Analysis
        fields = [
            "name",
            "symbol",
            "min_normal",
            "max_normal",
            "unit",
            "translations",
        ]
