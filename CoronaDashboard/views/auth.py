from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy

from ..forms import LoginForm, SignUpForm
from User.models.User import User


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":
        if form.is_valid():
            national_id = form.cleaned_data.get("national_id")
            password = form.cleaned_data.get("password")
            user = authenticate(national_id=national_id, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse_lazy("CoronaDashboard:Home"))
            else:
                msg = "Invalid credentials"
        else:
            msg = "Error validating the form"

    return render(request, "Corona/accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            national_id = form.cleaned_data.get("national_id")
            name = form.cleaned_data.get("name")
            mobile = form.cleaned_data.get("mobile")
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            # user = authenticate(national_id=national_id, password=raw_password)
            User.objects.create_user(
                name=name,
                national_id=national_id,
                mobile=mobile,
                email=email,
                password=raw_password,
            )
            msg = 'User created - please <a href="/corona_dashboard/login">login</a>.'
            success = True

            # return redirect("corona_dashboard/login/")

        else:
            msg = "Form is not valid"
    else:
        form = SignUpForm()

    return render(
        request,
        "Corona/accounts/register.html",
        {"form": form, "msg": msg, "success": success},
    )
