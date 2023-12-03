from django.contrib import admin
from django.db import models

from Language.widgets.myTranslation_json_widget import MyTranslationWidget
from .forms import AnalysisAdminForm
from .models import Analysis


# @admin.register(Analysis)
# class AnalysisAdmin(admin.ModelAdmin):
#     form = AnalysisAdminForm
#     formfield_overrides = {
#         models.JSONField: {
#             "widget": MyTranslationWidget,
#         },
#     }
