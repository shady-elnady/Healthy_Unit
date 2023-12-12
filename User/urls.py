from django.urls import path
from django.contrib.auth import views as auth_views

from .views import (
    SuccessVerifyEmailView,
    verify_account_email,
    # EMailVerifyView,
    logIn,
)

app_name = "User"


urlpatterns = [
    path(
        "log_in/",
        logIn,
        name="Log_In",
    ),
    path(
        "success_verify_account_email/",
        SuccessVerifyEmailView.as_view(),
        name="Success_Verify_Account_EMail",
    ),
    # path(
    #     "verify_account_email/",
    #     EMailVerifyView.as_view(),
    #     name="Verify_Account_EMail",
    # ),
    path(
        "verify_account_email/<str:id>/",
        verify_account_email,
        name="Verify_Account_EMail",
    ),
    # url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    # url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.password_reset_confirm, name='password_reset_confirm'),
    # url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]
