import json
from builtins import super

from django import forms
from django.conf import settings

from Language.models.Language import Language


class MyTranslationWidget(forms.Widget):
    # class Media:
    #     js = (
    #         getattr(settings, "JSON_EDITOR_JS", 'dist/jsoneditor.min.js'),
    #     )
    #     css = {
    #         'all': (
    #             getattr(settings, "JSON_EDITOR_CSS", 'dist/jsoneditor.min.css'),
    #         )
    #     }

    template_name = "Widgets/myTranslation_json_widget.html"

    def __init__(
        self,
        attrs=None,
        languages=Language.objects.all(),
    ):
        self.languages = languages
        super(MyTranslationWidget, self).__init__(attrs=attrs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["widget"]["languages"] = self.languages
        return context
