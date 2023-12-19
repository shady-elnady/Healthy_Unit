from rest_framework.authtoken.models import Token
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings


def get_token_model():
    if "rest_framework.authtoken" not in settings.INSTALLED_APPS:
        raise ImproperlyConfigured(
            "You must include `rest_framework.authtoken` in INSTALLED_APPS "
        )
    return Token


TokenModel = get_token_model()
