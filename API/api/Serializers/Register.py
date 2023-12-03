from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from rest_framework.serializers import ModelSerializer, EmailField, CharField
from rest_framework.validators import UniqueValidator
from django.core.validators import RegexValidator

from User.models.User import User


class RegisterSerializer(ModelSerializer):
    mobile_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",  # ^(\+\d{1,3})?,?\s?\d{8,13}
        message=_(
            _(
                "Mobile Number must not consist of space and requires country code. eg : +6591258565."
            )
        ),
    )
    name = CharField(
        max_length=100,
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message=_(
                    "Name ID Used. chosse Another",
                ),
            ),
        ],
    )
    national_id = CharField(
        max_length=14,
        min_length=14,
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message=_(
                    "National ID Used. chosse Another",
                ),
            ),
        ],
    )
    email = EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message=_(
                    "E-Mail is Used.",
                ),
            ),
        ],
    )
    mobile = CharField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message=_(
                    "Mobile Number is Used. chosse Another",
                ),
            ),
            mobile_regex,
        ],
    )
    password = CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = [
            "name",
            "national_id",
            "email",
            "mobile",
            "password",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "name": {"required": True},
            "national_id": {"required": True},
            "email": {"required": True},
            "mobile": {"required": True},
            "password": {
                "required": True,
                "write_only": True,
            },
        }
