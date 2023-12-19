from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField

from ..models import Employee

# Serializers define the API representation.


class EmployeeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "url",
            "uid",
            "name",
            "display_name",
            "national_id",
            "email",
            "phone_number",
            "photo_url",
            "Profile",
            "salary",
            "created_at",
            "last_updated",
        ]

    extra_kwargs = {
        "url": {"view_name": "employee-detail", "lookup_field": "uid"},
    }
