import re
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response
from rest_framework import status, generics

from User.utils.check_email import check_is_email

# from accounts.models import Role
from django.contrib.auth import get_user_model


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "is_superuser",
            "name",
            "email",
            "password",
            "first_name",
            "last_name",
            "phone_number",
            "date_joined",
            "last_login",
            "bio",
            "age",
        ]
        read_only_fields = [
            "is_superuser",
            "password",
        ]
