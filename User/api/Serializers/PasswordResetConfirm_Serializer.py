from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode as uid_decoder
from rest_framework.serializers import Serializer, CharField
from django.contrib.auth.forms import SetPasswordForm
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from django.utils.encoding import force_str
from django.conf import settings

from User.models.User import User


class PasswordResetConfirmSerializer(Serializer):
    """
    Serializer for confirming a password reset attempt.
    """

    new_password1 = CharField(max_length=128)
    new_password2 = CharField(max_length=128)
    uid = CharField()
    token = CharField()

    set_password_form_class = SetPasswordForm

    _errors = {}
    user = None
    set_password_form = None

    def custom_validation(self, attrs):
        pass

    def validate(self, attrs):
        # Decode the uidb64 (allauth use base36) to uid to get User object
        try:
            uid = force_str(uid_decoder(attrs["uid"]))
            self.user = User._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            raise ValidationError({"uid": [_("Invalid value")]})

        if not default_token_generator.check_token(self.user, attrs["token"]):
            raise ValidationError({"token": [_("Invalid value")]})

        self.custom_validation(attrs)
        # Construct SetPasswordForm instance
        self.set_password_form = self.set_password_form_class(
            user=self.user,
            data=attrs,
        )
        if not self.set_password_form.is_valid():
            raise ValidationError(self.set_password_form.errors)

        return attrs

    def save(self):
        return self.set_password_form.save()
