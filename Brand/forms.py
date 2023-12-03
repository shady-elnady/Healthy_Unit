from django.forms import ModelForm

from .models import Brand


class BrandAdminForm(ModelForm):
    class Meta:
        model = Brand
        fields = [
            "id",
            "name",
            "category",
            "made_in",
            "image",
            "translations",
        ]
