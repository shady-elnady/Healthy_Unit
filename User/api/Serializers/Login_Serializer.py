from rest_framework.serializers import Serializer, CharField, ValidationError

from User.models.User import User
from User.utils.backends import MyModelBackend
from Utils.Assets.messages import Messages
from Utils.Validators.Regex_Validators import RegexValidators


class LoginSerializer(Serializer):
    nationalID_or_EMail_or_Phone_or_Name_or_DisplayName = CharField(required=True)
    password = CharField(required=True, style={"input_type": "password"})

    # def validate_nationalID_or_EMail_or_Phone_or_Name_or_DisplayName(self, value: str):
    #     """
    #     Check that the blog post is about Django.
    #     """
    #     if RegexValidators.NATIONAL_ID_REGEX.match(value):
    #         raise ValidationError(Messages.NAME_INVALID_VALIDATION)
    #     return value

    def validate_password(self, value: str):
        """
        Check that the blog post is about Django.
        """
        if RegexValidators.PASSWORD_REGEX.match(value):
            raise ValidationError(Messages.PASSWORD_INVALID_VALIDATION)
        return value

    @staticmethod
    def _validate_account_disable_status(user: User):
        if user.disabled:
            raise ValidationError(Messages.USER_DISABLED)

    @staticmethod
    def _validate_account_active_status(user: User):
        if not user.is_active:
            raise ValidationError(Messages.USER_NOT_ACTIVATE)

    @staticmethod
    def _validate_account_verification_status(user: User):
        if not user.is_verified:
            raise ValidationError(Messages.USER_NOT_VERIFIED)

    @staticmethod
    def _validate_email_verification_status(user: User):
        if not user.email_verified:
            raise ValidationError(Messages.EMAIL_NOT_VERIFIED)

    @staticmethod
    def _validate_phone_number_verification_status(user: User):
        if not user.phone_number_verified:
            raise ValidationError(Messages.EMAIL_NOT_VERIFIED)

    def validate(self, data):
        nationalID_or_EMail_or_Phone_or_Name_or_DisplayName = data.get(
            "nationalID_or_EMail_or_Phone_or_Name_or_DisplayName"
        )
        password = data.get("password")

        if user := MyModelBackend.authenticate(
            nationalID_or_EMail_or_Phone_or_Name_or_DisplayName=nationalID_or_EMail_or_Phone_or_Name_or_DisplayName,
            password=password,
        ):
            self._validate_account_disable_status(user)
            self._validate_account_active_status(user)
            self._validate_account_verification_status(user)
            self._validate_email_verification_status(user)
            self._validate_phone_number_verification_status(user)
            data["user"] = user
            return data
        else:
            raise ValidationError(Messages.USER_NOT_FOUND)
