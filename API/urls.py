from django.urls import path
from rest_framework.authtoken import views
from rest_framework.authtoken.views import obtain_auth_token  # <-- NEW

from .views import (
    LogIn,
)


app_name = "API"


urlpatterns = [
    path("login/", LogIn.as_view(), name="LogIn"),
    #     path("get-otp-mobile/", MobileSendOTP.as_view(), name="get_OTP_Mobile"),
    #     path("verify-otp-mobile/", VerifymobileOTPView.as_view(), name="OTP_Verify"),
    #     path("change-password/", change_password, name="Change_Password"),
    #     path("password-recovery/", passwordRecovery.as_view(), name="Password_Recovery"),
    #     path("logout/", LogoutView.as_view(), name="LogOut"),
]

# Lazy-load on routing is needed
# During the first build, API is not yet generated
try:
    urlpatterns.append(path("login/jwt/", view=obtain_auth_token))
except:
    pass


"""
  https://codevoweb.com/django-implement-2fa-two-factor-authentication/

  https://studygyaan.com/tag/django-rest-framework

"""
