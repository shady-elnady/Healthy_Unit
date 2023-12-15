from django.urls import path
from rest_framework.authtoken import views
from rest_framework.authtoken.views import obtain_auth_token  # <-- NEW

from .views import (
    CreateNewUserView,
    LogInView,
    RetrieveUpdateDestroyUserView,
    UpdateUserEmailView,
    UserPasswordResetView,
)


app_name = "FireBase"


urlpatterns = [
    path(
        "sign-up/",
        CreateNewUserView.as_view(),
        name="Create-New-User",
    ),
    path(
        "sign-in/",
        LogInView.as_view(),
        name="Log-In",
    ),
    path(
        "<str:pk>/",
        RetrieveUpdateDestroyUserView.as_view(),
        name="Retrieve-Update-Destroy-User",
    ),
    path(
        "update-email/",
        UpdateUserEmailView.as_view(),
        name="Update-User-Email",
    ),
    path(
        "reset-password/",
        UserPasswordResetView.as_view(),
        name="User-Password-Reset",
    ),
]
