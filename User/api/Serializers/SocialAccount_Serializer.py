# from rest_framework import serializers
# from django.utils.translation import gettext_lazy as _

# try:
#     from allauth.socialaccount.models import SocialAccount
# except ImportError:
#     raise ImportError("allauth needs to be added to INSTALLED_APPS.")


# class SocialAccountSerializer(serializers.ModelSerializer):
#     """
#     serialize allauth SocialAccounts for use with a REST API
#     """

#     class Meta:
#         model = SocialAccount
#         fields = (
#             "id",
#             "provider",
#             "uid",
#             "last_login",
#             "date_joined",
#         )
