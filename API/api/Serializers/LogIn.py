from rest_framework.serializers import Serializer, CharField
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class LogInSerializer(Serializer):
    national_id_regex = RegexValidator(
        regex=r"^\d{14}$",  # ^(\+\d{1,3})?,?\s?\d{8,13}
        message=_("National ID must be 14 Numbers. eg : 11111111111111"),
    )
    national_id = CharField(
        max_length=14,
        min_length=14,
        required=True,
        validators=[
            national_id_regex,
        ],
    )
    password = CharField(
        max_length=128,
        write_only=True,
        required=True,
    )

    # def validate(self, data):
    #     # username = data['username']
    #     return data

    # class Meta:
    #     model = User
    #     fields = ['username', 'email']
