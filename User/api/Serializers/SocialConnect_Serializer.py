# from django.core.exceptions import ValidationError as DjangoValidationError
# from django.utils.translation import gettext_lazy as _
# from rest_framework import serializers

# from .SocialLogin_Serializer import SocialLoginSerializer


# class SocialConnectMixin:
#     def get_social_login(self, *args, **kwargs):
#         """
#         Set the social login process state to connect rather than login
#         Refer to the implementation of get_social_login in base class and to the
#         allauth.socialaccount.helpers module complete_social_login function.
#         """
#         social_login = super().get_social_login(*args, **kwargs)
#         social_login.state["process"] = AuthProcess.CONNECT
#         return social_login


# class SocialConnectSerializer(SocialConnectMixin, SocialLoginSerializer):
#     pass


# class RegisterSerializer(serializers.Serializer):
#     username = serializers.CharField(
#         max_length=get_username_max_length(),
#         min_length=allauth_account_settings.USERNAME_MIN_LENGTH,
#         required=allauth_account_settings.USERNAME_REQUIRED,
#     )
#     email = serializers.EmailField(required=allauth_account_settings.EMAIL_REQUIRED)
#     password1 = serializers.CharField(write_only=True)
#     password2 = serializers.CharField(write_only=True)

#     def validate_username(self, username):
#         username = get_adapter().clean_username(username)
#         return username

#     def validate_email(self, email):
#         email = get_adapter().clean_email(email)
#         if allauth_account_settings.UNIQUE_EMAIL:
#             if email and EmailAddress.objects.is_verified(email):
#                 raise serializers.ValidationError(
#                     _("A user is already registered with this e-mail address."),
#                 )
#         return email

#     def validate_password1(self, password):
#         return get_adapter().clean_password(password)

#     def validate(self, data):
#         if data["password1"] != data["password2"]:
#             raise serializers.ValidationError(
#                 _("The two password fields didn't match.")
#             )
#         return data

#     def custom_signup(self, request, user):
#         pass

#     def get_cleaned_data(self):
#         return {
#             "username": self.validated_data.get("username", ""),
#             "password1": self.validated_data.get("password1", ""),
#             "email": self.validated_data.get("email", ""),
#         }

#     def save(self, request):
#         adapter = get_adapter()
#         user = adapter.new_user(request)
#         self.cleaned_data = self.get_cleaned_data()
#         user = adapter.save_user(request, user, self, commit=False)
#         if "password1" in self.cleaned_data:
#             try:
#                 adapter.clean_password(self.cleaned_data["password1"], user=user)
#             except DjangoValidationError as exc:
#                 raise serializers.ValidationError(
#                     detail=serializers.as_serializer_error(exc)
#                 )
#         user.save()
#         self.custom_signup(request, user)
#         setup_user_email(request, user, [])
#         return user
