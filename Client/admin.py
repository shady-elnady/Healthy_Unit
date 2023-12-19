from django.contrib.admin import site, register, ModelAdmin
from django.utils.translation import gettext_lazy as _
from polymorphic_tree.admin import (
    PolymorphicMPTTParentModelAdmin,
    PolymorphicMPTTChildModelAdmin,
)

from User.models.User import User
from Employee.models import Employee
from Employee.forms import EmployeeAdminForm
from Doctor.models import Doctor
from Doctor.forms import DoctorAdminForm
from Client.models import Client

from User.admin import ProfileInline
from Utils.Helpers.cach_mixin import CachedMixin

# The common admin functionality for all derived models:


class BaseChildAdmin(CachedMixin, PolymorphicMPTTChildModelAdmin):
    GENERAL_FIELDSET = (
        None,
        {
            "fields": (
                "parent",
                "name",
                "display_name",
                "national_id",
                "email",
                "phone_number",
                "photo_url",
                # "Profile",
            ),
        },
    )
    readonly_fields = [
        "content_types",
    ]

    base_model = User
    base_fieldsets = (GENERAL_FIELDSET,)
    inlines = (ProfileInline,)

    def changeform_view(self, request, *args, **kwargs):
        self.request = request
        return super().changeform_view(request, *args, **kwargs)

    def render_change_form(self, request, *args, **kwargs):
        self.response = super().render_change_form(request, *args, **kwargs)
        return self.response

    ###
    def get_inline_instances(self, *args, **kwargs):
        yield from (
            (inline, vars(inline).update(modeladmin=self))[0]
            for inline in super().get_inline_instances(*args, **kwargs)
        )


# Optionally some custom admin code


class EmployeeChildAdmin(BaseChildAdmin):
    form = EmployeeAdminForm


class DoctorChildAdmin(BaseChildAdmin):
    form = DoctorAdminForm


class ClientChildAdmin(BaseChildAdmin):
    pass


# Create the parent admin that combines it all:


class UserAdmin(CachedMixin, PolymorphicMPTTParentModelAdmin):
    base_model = User
    child_models = (
        User,
        Employee,
        Doctor,
        Client,
    )

    list_display = (
        "name",
        "national_id",
        "email",
        "phone_number",
        "actions_column",
    )
    inlines = (ProfileInline,)

    def changeform_view(self, request, *args, **kwargs):
        self.request = request
        return super().changeform_view(request, *args, **kwargs)

    def render_change_form(self, request, *args, **kwargs):
        self.response = super().render_change_form(request, *args, **kwargs)
        return self.response

    ###
    def get_inline_instances(self, *args, **kwargs):
        yield from (
            (inline, vars(inline).update(modeladmin=self))[0]
            for inline in super().get_inline_instances(*args, **kwargs)
        )

    class Media:
        css = {"all": ("admin/treenode/admin.css",)}


site.register(Employee, EmployeeChildAdmin)
site.register(Doctor, DoctorChildAdmin)
site.register(Client, ClientChildAdmin)
site.register(User, UserAdmin)
