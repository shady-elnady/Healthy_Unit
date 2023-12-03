from django import forms
from django.contrib.auth.forms import UserCreationForm
from User.models.User import User


class LoginForm(forms.Form):
    national_id = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "National ID", "class": "form-control"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        )
    )


class SignUpForm(UserCreationForm):
    national_id = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "National ID", "class": "form-control"}
        )
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Name", "class": "form-control"})
    )
    mobile = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Mobile", "class": "form-control"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password check", "class": "form-control"}
        )
    )

    class Meta:
        model = User
        fields = (
            "national_id",
            "name",
            "mobile",
            "email",
            "password1",
            "password2",
        )
