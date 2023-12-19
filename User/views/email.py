from django import forms
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import FormView, TemplateView

from .forms.EMailVerify_Form import EMailVerifyForm
from ..models.User import User

# Create your views here.


def verify_account_email(request, id):
    try:
        user = get_object_or_404(User, national_id=id)
        if not user.email_verified:
            user.email_verified = True
            user.is_verified = True
            user.save()
        return redirect(
            reverse_lazy("User:Success_Verify_Account_EMail"),
        )
    except Exception as e:
        raise HttpResponse(f"Error > {e}")


# class EMailVerifyView(FormView):
#     template_name = "emails/verify_email.html"
#     form_class = EMailVerifyForm
#     success_url = reverse_lazy("User:Success_Verify_Account_EMail")

#     def form_valid(self, form):
#         # Calls the custom send method
#         form.email_verify()
#         return super().form_valid(form)


class SuccessVerifyEmailView(TemplateView):
    template_name = "emails/success_verify_account_email.html"


# # contact/forms.py
# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=120)
#     email = forms.EmailField()
#     inquiry = forms.CharField(max_length=70)
#     message = forms.CharField(widget=forms.Textarea)

#     def get_info(self):
#         """
#         Method that returns formatted information
#         :return: subject, msg
#         """
#         # Cleaned data
#         cl_data = super().clean()

#         name = cl_data.get("name").strip()
#         from_email = cl_data.get("email")
#         subject = cl_data.get("inquiry")

#         msg = f"{name} with email {from_email} said:"
#         msg += f'\n"{subject}"\n\n'
#         msg += cl_data.get("message")

#         return subject, msg

#     def send(self):
#         subject, msg = self.get_info()

#         send_mail(
#             subject=subject,
#             message=msg,
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=["shadyelnady@gmail.com"],
#         )


# class ContactView(FormView):
#     template_name = "email/contact.html"
#     form_class = ContactForm
#     success_url = reverse_lazy("User:Success")

#     def form_valid(self, form):
#         # Calls the custom send method
#         form.send()
#         return super().form_valid(form)
