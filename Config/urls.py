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
from django.contrib import admin
from django.urls import path, include, re_path
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from API.Router.router import router


schema_view = get_schema_view(
    openapi.Info(
        title="User Management API",
        default_version="v1",
        description="API Documentation",
        terms_of_service="",
        contact=openapi.Contact(email=""),
        license=openapi.License(name=""),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

api_version = "v1"

urlpatterns = [
    path(
        f"{api_version}/i18n/", include("django.conf.urls.i18n")
    ),  # for Multi Languages & Translation
]

urlpatterns += i18n_patterns(
    # path("", include("django.contrib.auth.urls")), # include all auth views
    # path("", include("Logs.urls", namespace="Logs")),
    path("", include("User.urls", namespace="User")),
    # path("fire", include("FireBase.urls", namespace="FireBase")),
    path(
        "corona_dashboard",
        include("CoronaDashboard.urls", namespace="CoronaDashboard"),
    ),
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
    path("", include(settings.ADMIN_DASHBOARD["url"])),
    path("", include("django_dyn_dt.urls")),  # <-- NEW: Dynamic_DT Routing
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        f"swagger/{api_version}/swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        f"redoc/{api_version}/redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
