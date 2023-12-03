from django.urls import path, re_path
from .views import login_view, register_user, index, pages
from django.contrib.auth.views import LogoutView


app_name = "CoronaDashboard"

urlpatterns = [
    path("login/", login_view, name="LogIn"),
    path("register/", register_user, name="Register"),
    path("logout/", LogoutView.as_view(), name="LogOut"),
    # The home page
    path("", index, name="Home"),
    # Matches any html file
    re_path(r"^.*\.*", pages, name="Pages"),
]
