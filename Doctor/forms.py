from django.forms import ModelForm

from .models import Doctor


class DoctorAdminForm(ModelForm):
    class Meta:
        model = Doctor
        fields = [
            # "national_id",
            # "email",
            # "mobile",
            "salary",
            "medical_specialty",
        ]
