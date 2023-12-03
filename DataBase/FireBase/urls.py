from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView

from .views import (
    save_to_firestroe,
    read_from_firestroe,
)


app_name = "FireBase"


urlpatterns = [
    path("", save_to_firestroe, name="home"),
    path("users/", read_from_firestroe, name="users"),
    # path('', index, name= "home"),
]
