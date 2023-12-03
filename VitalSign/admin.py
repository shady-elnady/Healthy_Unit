from django.contrib import admin
from django.db import models

from Language.widgets.myTranslation_json_widget import MyTranslationWidget
from .forms import VitalSignAdminForm
from .models import VitalSign


@admin.register(VitalSign)
class VitalSignAdmin(admin.ModelAdmin):
    form = VitalSignAdminForm
    formfield_overrides = {
        models.JSONField: {
            "widget": MyTranslationWidget,
        },
    }
