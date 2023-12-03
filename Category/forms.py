from django.forms import ModelForm

from .models import Category


class CategoryAdminForm(ModelForm):
    class Meta:
        model = Category
        fields = [
            "name",
            "category_parent",
            "translations",
        ]
