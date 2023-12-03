from django.forms import ModelForm

from .models import Employee


class EmployeeAdminForm(ModelForm):
    class Meta:
        model = Employee
        fields = [
            "salary",
        ]
