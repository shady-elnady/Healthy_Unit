from django.contrib import admin
from django.db import models

from Language.widgets.myTranslation_json_widget import MyTranslationWidget
from .forms import BrandAdminForm
from .models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    form = BrandAdminForm
    formfield_overrides = {
        models.JSONField: {
            "widget": MyTranslationWidget,
        },
    }
