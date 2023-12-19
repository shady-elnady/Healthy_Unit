# from django.forms import Form, EmailField, EmailInput
# from django.contrib.auth.tokens import default_token_generator
# from django.contrib.sites.shortcuts import get_current_site
# from django.utils.translation import get_language
# from django.utils.encoding import force_bytes
# from django.utils.http import urlsafe_base64_encode
# from django.utils.translation import gettext_lazy as _
# from pydantic import EmailStr
# from typing import Dict

# from EMail.Helpers.EMail_Sender import EMailSender
# from User.api.Views.User_ViewSet import UserViewSet
# from User.models.User import User
# from User.utils.unicode_compare import unicode_ci_compare


# class PasswordResetForm(Form):
#     email = EmailField(
#         label=_("E-Mail"),
#         max_length=254,
#         required=True,
#         widget=EmailInput(attrs={"autocomplete": "email"}),
#     )

#     def get_users(self, email):
#         """Given an email, return matching user(s) who should receive a reset.

#         This allows subclasses to more easily customize the default policies
#         that prevent inactive users and users with unusable passwords from
#         resetting their password.
#         """
#         email_field_name = User.get_email_field_name()
#         active_users = User._default_manager.filter(
#             **{
#                 "%s__iexact" % email_field_name: email,
#                 "is_active": True,
#             }
#         )
#         return (
#             u
#             for u in active_users
#             if u.has_usable_password()
#             and unicode_ci_compare(email, getattr(u, email_field_name))
#         )

#     def save(
#         self,
#         domain_override=None,
#         use_https=False,
#         token_generator=default_token_generator,
#         request=None,
#         extra_email_context=None,
#     ):
#         """
#         Generate a one-use only link for resetting password and send it to the
#         user.
#         """
#         email = self.cleaned_data["email"]
#         # if not domain_override:
#         #     current_site = get_current_site(request)
#         #     site_name = current_site.name
#         #     domain = current_site.domain
#         # else:
#         #     site_name = domain = domain_override
#         # protocol = "https" if use_https else "http"
#         email_field_name = User.get_email_field_name()
#         for user in self.get_users(email):
#             user_email = getattr(user, email_field_name)
#             context = {
#                 # "email": user_email,
#                 # "domain": domain,
#                 # "site_name": site_name,
#                 # "uid": urlsafe_base64_encode(force_bytes(user.uid)),
#                 # "token": token_generator.make_token(user),
#                 "name": user.display_name,
#                 "password_rest_url": UserViewSet.reverse_action(
#                     UserViewSet.password_reset_confirm.url_name,
#                     args=[
#                         urlsafe_base64_encode(force_bytes(user.uid)),
#                         token_generator.make_token(user),
#                     ],
#                 ),
#                 # "password_rest_url": f"{ protocol }://{ domain }/{get_language()}{ password_reset_confirm }uidb64=uid token=token",
#                 "message": _(
#                     "Thank you for joining us.\n Log In To Active Your Account.",
#                 ),
#                 **(extra_email_context or {}),
#             }
#             return EMailSender(
#                 user_email,
#             ).send_template(
#                 template_name="password_reset",
#                 context=context,
#             )
