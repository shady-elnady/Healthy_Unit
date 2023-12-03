from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth import get_user_model
from templated_email.generic_views import TemplatedEmailFormViewMixin

# Create your views here.


# This view send a welcome email to the author
class UserCreateView(TemplatedEmailFormViewMixin, CreateView):
    model = get_user_model()
    fields = ["name", "email"]
    templated_email_template_name = "verify_email"
    template_name = "authors/create_author.html"
    success_url = "/create_author/"

    def templated_email_get_recipients(self, form):
        return [form.data["email"]]
