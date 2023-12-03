"""
URL configuration for Config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include, re_path
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from API.Router.router import router


urlpatterns = [
    path(
        "i18n/", include("django.conf.urls.i18n")
    ),  # for Multi Languages & Translation
]

urlpatterns += i18n_patterns(
    # path("", include("django.contrib.auth.urls")), # include all auth views
    # path("", include("Logs.urls", namespace="Logs")),
    path("", include("User.urls", namespace="User")),
    # Rest_Fram_Work
    path("api/", include("API.urls", namespace="API")),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # anymail
    path("anymail/", include("anymail.urls")),
    path(
        "templated_email",
        include("templated_email.urls", namespace="templated_email"),
    ),
    # Admin
    path("admin/", admin.site.urls),
    path("", include("admin_black.urls")),  # Black Dashboard
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
