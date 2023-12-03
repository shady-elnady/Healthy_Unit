from django.forms import ModelForm

from .models import Service, ServiceRecord


class ServiceAdminForm(ModelForm):
    class Meta:
        model = Service
        fields = [
            "parent",
            "name",
            "translations",
            # "content_type",
        ]


class ServiceRecordAdminForm(ModelForm):
    class Meta:
        model = ServiceRecord
        fields = [
            # "bar_code",
            "service",
            "patient",
            "diagnosis",
            "note",
        ]
