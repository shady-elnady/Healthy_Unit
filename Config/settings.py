"""
Django settings for Config project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os, random, string, inspect
import django_dyn_dt
import re
import django
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.db.backends.postgresql.psycopg_any import IsolationLevel
from templated_email.backends.vanilla_django import TemplateBackend
import environ


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    TEMPLATE_DEBUG=(bool, False),
    BASE_URL=(str, "http://127.0.0.1:8000/"),
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

ASSETS_DIR = os.path.join(BASE_DIR, "Assets")

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

BASE_URL = env("BASE_URL")

SECRET_KEY = env("SECRET_KEY")
if not SECRET_KEY:
    SECRET_KEY = "".join(random.choice(string.ascii_lowercase) for i in range(32))

# SECURITY WARNING: don't run with debug turned on in production!
# False if not in os.environ because of casting above

DEBUG = env("DEBUG")

TEMPLATE_DEBUG = env("TEMPLATE_DEBUG")

AUTH_USER_MODEL = "User.User"

# # for Access User Profile example(profile = request.user.get_profile())
AUTH_PROFILE_MODEL = "User.Profile"

ALLOWED_HOSTS = [
    "*",
    "localhost",
    "127.0.0.1",
    "herokuapp.com",
]


# Add here your deployment HOSTS
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "http://localhost:5085",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5085",
]

RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


CORS_ALLOWED_ORIGINS = ["http://localhost:3000"]

CORS_ALLOW_CREDENTIALS = True

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by email
    # "allauth.account.auth_backends.AuthenticationBackend",
]

# Application definition

# 3rd Libraries
THIRD_LIBRARIES = [
    "django.contrib.gis",
    "polymorphic_tree",
    "polymorphic",
    "mptt",
    "rest_framework",  # Django rest framework (drf)
    "rest_framework_gis",
    "rest_framework.authtoken",  # Adding token based authentication from drf
    "django_filters",
    "corsheaders",
    "anymail",
    "templated_email",
    "mapwidgets",
    "django_dyn_dt",
]

# My Applications
MY_APPS = [
    "Utils",
    "EMail",
    "Language",
    "Currency",
    "Category",
    "Address",
    "Brand",
    "User",
    "Employee",
    "Doctor",
    "Client",
    "Notification",
    "Service",
    "Drug",
    "Vaccination",
    "Analysis",
    "VitalSign",
    "Visit",
    "Radiology",
    ##
    # "Logs",
    ## API RestFrameWork & GraphQL
    "API",
    ## Corona Dashboard
    "CoronaDashboard",
    ## End My Apps
    "Tool",
]

# Admin Dashboard Libraries
ADMIN_DASHBOARDS = {
    "gradient": {
        "app": "admin_gradient.apps.AdminGradientConfig",
        "url": "admin_gradient.urls",
    },
    "corporate": {
        "app": "admin_corporate.apps.AdminCorporateConfig",
        "url": "admin_corporate.urls",
    },
    "black": {
        "app": "admin_black.apps.AdminBlackConfig",
        "url": "admin_black.urls",
    },
    "atlantis": {
        "app": "admin_atlantis.apps.AdminAtlantisConfig",
        "url": "admin_atlantis.urls",
    },
    "datta": {
        "app": "admin_datta.apps.AdminDattaConfig",
        "url": "admin_datta.urls",
    },
}

ADMIN_DASHBOARD = ADMIN_DASHBOARDS["black"]

INSTALLED_APPS = [
    ADMIN_DASHBOARD["app"],
    "django.contrib.admin",
    # "Utils.Helpers.adminpanel.AdminConfig",  # Custom Admin Panel
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # "django.contrib.sites",  # NEW
    ## 3rd Libraraies
    *THIRD_LIBRARIES,
    ## My Apps
    *MY_APPS,
    "django.forms",
]

SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",  # for Multi Languages & Translation
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # for corsheaders
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "Config.urls"

FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")  # ROOT dir for templates
TEMPLATE_DIR_DATATB = os.path.join(
    BASE_DIR, "django_dyn_dt/templates"
)  # <-- NEW: Dynamic_DT
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            TEMPLATE_DIR,
            django.__path__[0] + "/forms/templates",
            TEMPLATE_DIR_DATATB,
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",  # for Multi Languages & Translation
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "Config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': str(os.path.join(BASE_DIR, "DataBase", "db.sqlite3")),
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
        # "OPTIONS": {
        #     "service": "my_service",
        #     "passfile": ".my_pgpass",
        #     "isolation_level": IsolationLevel.SERIALIZABLE,
        # },
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# GOOGLE MAP
GOOGLE_API_KEY = env("GOOGLE_API_KEY")

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

# LANGUAGE_CODE = "en-us"
LANGUAGE_CODE = "en"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

PHONENUMBER_DEFAULT_REGION = "EG"

# Supported Languages
LANGUAGES = [
    ("ar", _("Arabic")),
    ("en", _("English")),
    ("fr", _("French")),
]
# True for right-to-left languages like Arabic, and to False otherwise
# LANGUAGE_BIDI = False
# Languages using BiDi (right-to-left) layout
LANGUAGES_BIDI = [
    "ar",
    # "he", "ar-dz", "fa", "ur"
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, "Locales"),
    # "/home/www/project/common_files/locale",
    # "/var/local/translations/locale",
]

INTERNAL_IPS = [
    "127.0.0.1",
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(ASSETS_DIR, "staticfiles")

DYN_DB_PKG_ROOT = os.path.dirname(inspect.getfile(django_dyn_dt))  # <-- NEW: Dynamic_DT

STATICFILES_DIRS = (
    os.path.join(ASSETS_DIR, "static"),
    os.path.join(DYN_DB_PKG_ROOT, "templates/static"),  # <-- NEW: Dynamic_DT
)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.DefaultStorageFinder",
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)


MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(ASSETS_DIR, "media")

# ### DYNAMIC_DATATB Settings ###
DYNAMIC_DATATB = {
    # SLUG -> Import_PATH
    "category": "Category.models.Category",
    "brand": "Brand.models.Brand",
}
########################################

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


####
ADMINS = (("Shady", "shadyelnady@gmail.com"),)

MANAGERS = ADMINS

EXTERNAL_USER = "Shady"

## Currency
CURRENCIES = (
    "USD",
    "EUR",
)
CURRENCY_CHOICES = [
    ("USD", "USD $"),
    ("EUR", "EUR €"),
]

DEFAULT_CURRENCY = "EG"

##
LOGIN_URL = reverse_lazy("User:Log_In")
# LOGIN_REDIRECT_URL = reverse_lazy("Logs:Home")
LOGOUT_REDIRECT_URL = reverse_lazy("User:Log_In")
# LOGOUT_URL = reverse_lazy("Logs:LogOut")

## Twilio
ACCOUNT_SID = env("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = env("TWILIO_AUTH_TOKEN")
COUNTRY_CODE = env("TWILIO_COUNTRY_CODE")
TWILIO_WHATSAPP_NUMBER = env("TWILIO_WHATSAPP_NUMBER")
TWILIO_PHONE_NUMBER = env("TWILIO_PHONE_NUMBER")

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "elnadylab1@gmail.com"
EMAIL_HOST_PASSWORD = "bkekshkjvgrgkrfo"
EMAIL_USE_SSL = False

## REST_FRAMEWORK
REST_FRAMEWORK = {
    # "DATE_FORMAT": "%d/%m/%Y",
    # Use Django"s standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_SCHEMA_CLASS": "rest_framework_gis.schema.GeoFeatureAutoSchema",
    "DEFAULT_PERMISSION_CLASSES": [
        # "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly",
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 2,
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "ORDERING_PARAM": "sorters[0][field]",
    # "EXCEPTION_HANDLER": "API.exceptions.django_error_handler"  ## Excepitions
}

ANYMAIL = {
    # "MAILJET_API_KEY": env("MAILJET_API_KEY"),
    # "MAILJET_SECRET_KEY": env("MAILJET_SECRET_KEY"),
}
# EMAIL_BACKEND = "anymail.backends.mailjet.EmailBackend"
# MAILJET_API_URL = "https://api.mailjet.com/v3.1/"
# This replaces django.core.mail.EmailMessage

## django-templated-email
# You can also use a class directly
TEMPLATED_EMAIL_BACKEND = TemplateBackend
TEMPLATED_EMAIL_EMAIL_MESSAGE_CLASS = "anymail.message.AnymailMessage"
# This replaces django.core.mail.EmailMultiAlternatives
TEMPLATED_EMAIL_EMAIL_MULTIALTERNATIVES_CLASS = "anymail.message.AnymailMessage"
TEMPLATED_EMAIL_TEMPLATE_DIR = os.path.join(TEMPLATE_DIR, "emails", "templated_emails/")
TEMPLATED_EMAIL_FILE_EXTENSION = "email"
TEMPLATED_EMAIL_DJANGO_SUBJECTS = {
    "welcome": _("Welcome to Healthy Unit Website"),
    "verify_email": _("Verify Your Account E-Mail"),
}


BASE_APP_URL = "http://localhost:3000"
BASE_API_URL = "http://localhost:8000"
GOOGLE_OAUTH2_CLIENT_ID = "Your_google_client_id"
GOOGLE_OAUTH2_CLIENT_SECRET = "Your_google_client_secret"
