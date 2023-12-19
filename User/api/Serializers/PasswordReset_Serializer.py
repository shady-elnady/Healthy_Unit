# from rest_framework.serializers import Serializer, EmailField
# from rest_framework.exceptions import ValidationError
# from django.utils.translation import gettext_lazy as _
# from django.conf import settings
# from pydantic import EmailStr

# from User.views.forms.PasswordReset_Form import PasswordResetForm


# class PasswordResetSerializer(Serializer):
#     """
#     Serializer for requesting a password reset e-mail.

#     لطلب البريد الإلكتروني إعادة تعيين كلمة المرور.
#     """

#     email = EmailField(required=True)

#     reset_form = None

#     @property
#     def password_reset_form_class(self):
#         return PasswordResetForm


#     def validate_email(self, value: EmailStr):
#         # Create PasswordResetForm with the serializer
#         self.reset_form = self.password_reset_form_class(data=self.initial_data)
#         if not self.reset_form.is_valid():
#             raise ValidationError(self.reset_form.errors)
#         return value

#     def save(self):
#         from django.contrib.auth.tokens import default_token_generator

#         request = self.context.get("request")
#         # Set some values to trigger the send_email method.
#         opts = {
#             "use_https": request.is_secure(),
#             "from_email": getattr(settings, "DEFAULT_FROM_EMAIL"),
#             "request": request,
#             "token_generator": default_token_generator,
#         }
#         self.reset_form.save(**opts)
