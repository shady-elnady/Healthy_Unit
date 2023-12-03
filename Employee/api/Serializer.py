from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField

from ..models import Employee

# Serializers define the API representation.


class EmployeeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "url",
            "id",
            "name",
            "national_id",
            "email",
            "mobile",
            "salary",
            "created_at",
            "last_updated",
        ]

    extra_kwargs = {
        "url": {"view_name": "employee-detail", "lookup_field": "id"},
    }
