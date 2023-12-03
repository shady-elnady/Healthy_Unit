# from django.db import models
from django.db.models import CharField, BooleanField
from django.utils.translation import gettext_lazy as _

from Utils.models.BaseModel import BaseNativeModel

# Create your model


class Language(BaseNativeModel):
    iso_639_1 = CharField(
        max_length=2,
        unique=True,
        verbose_name=_("ISO 639-1"),
    )
    iso_639_2T = CharField(
        max_length=3,
        unique=True,
        verbose_name=_("ISO 639-2/T"),
    )
    is_bidi = BooleanField(
        default=False,
        verbose_name=_("is Bidirectional Language"),
    )

    class Meta:
        verbose_name = _("Language")
        verbose_name_plural = _("Languages")


# activate language to auth user
"""


from django.conf import settings
from django.contrib.auth.views import LoginView
from django.urls import translate_url
from django.utils.translation import activate, LANGUAGE_SESSION_KEY

# available languages should be obtained from settings.LANGUAGES
available_languages = [lang_code for (lang_code, lang_name) in settings.LANGUAGES]

class CustomLoginView(LoginView):
    def get_success_url(self):
        url = super(CustomLoginView, self).get_success_url()
        user = self.request.user
        if user.is_authenticated():
            language = user.get_setting('language')

            if language in available_languages:
                url = translate_url(url, language)
                activate(language)
                if hasattr(self.request, 'session'):
                    self.request.session[LANGUAGE_SESSION_KEY] = language

        return url
"""

# What's the correct way to set up Django translation?
"""
https://stackoverflow.com/questions/20467626/whats-the-correct-way-to-set-up-django-translation#76475418

https://stackoverflow.com/questions/53962200/django-store-the-language-of-user-in-database

"""
