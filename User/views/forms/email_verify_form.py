from django.forms import Form, CharField
from django.core.validators import RegexValidator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _

from User.models.User import User


class EMailVerifyForm(Form):
    national_id_regex = RegexValidator(
        regex=r"^\d{14}$",  # ^(\+\d{1,3})?,?\s?\d{8,13}
        message=_("National ID must be 14 Numbers. eg : 11111111111111"),
    )
    national_id = CharField(
        min_length=14,
        max_length=14,
        required=True,
        label=_("National ID"),
        help_text=_("Enter Your National Number"),
        validators=[national_id_regex],
        localize=True,
    )

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()
        return cl_data.get("national_id").strip()

    def email_verify(self):
        try:
            user = get_object_or_404(User, national_id=self.get_info())
            if not user.email_verified:
                user.email_verified = True
                user.is_verified = True
                user.save()
        except Exception as e:
            raise HttpResponse(f"Error > {e}")
