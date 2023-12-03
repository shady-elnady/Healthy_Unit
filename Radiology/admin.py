from django.contrib.admin import site, register, StackedInline
from django.db import models
from django.utils.translation import gettext_lazy as _
from polymorphic_tree.admin import (
    PolymorphicMPTTParentModelAdmin,
    PolymorphicMPTTChildModelAdmin,
)
from polymorphic.admin import (
    PolymorphicParentModelAdmin,
    PolymorphicChildModelAdmin,
    PolymorphicChildModelFilter,
)
from Language.widgets.myTranslation_json_widget import MyTranslationWidget
from Service.forms import ServiceRecordAdminForm
from Service.models import Service, ServiceRecord, ParentService
from Analysis.models import Analysis, Report
from User.models.Profile import Profile
from Vaccination.models import Vaccination, VaccinationRecord
from Radiology.models import Radiology, RadiologySession

# The common admin functionality for all derived models:


class BaseServiceChildAdmin(PolymorphicMPTTChildModelAdmin):
    GENERAL_FIELDSET = (
        None,
        {
            "fields": (
                "parent",
                "name",
                "translations",
            ),
        },
    )

    base_model = Service
    formfield_overrides = {
        models.JSONField: {
            "widget": MyTranslationWidget,
        },
    }
    readonly_fields = [
        "content_type",
    ]
    base_fieldsets = (GENERAL_FIELDSET,)


# Optionally some custom admin code


class ParentServiceChildAdmin(BaseServiceChildAdmin):
    pass


class AnalysisChildAdmin(BaseServiceChildAdmin):
    pass


class RadiologyChildAdmin(BaseServiceChildAdmin):
    pass


class VaccinationChildAdmin(BaseServiceChildAdmin):
    pass


# Create the parent admin that combines it all:


class ServiceAdmin(PolymorphicMPTTParentModelAdmin):
    base_model = Service
    child_models = (
        Service,
        ParentService,
        Analysis,
        Radiology,
        Vaccination,
    )

    list_display = (
        # "parent",
        "name",
        "actions_column",
    )

    class Media:
        css = {"all": ("admin/treenode/css",)}


site.register(ParentService, ParentServiceChildAdmin)
site.register(Analysis, AnalysisChildAdmin)
site.register(Radiology, RadiologyChildAdmin)
site.register(Vaccination, VaccinationChildAdmin)
site.register(Service, ServiceAdmin)


# @register(User)
# class UserAdmin(UserAdmin):
#     # form = UserAdminForm
#     inlines = [
#         ProfileAdmin,
#     ]


################################################################

class ServiceRecordChildAdmin(PolymorphicChildModelAdmin):
    """Base admin class for all child models"""

    base_model = ServiceRecord  # Optional, explicitly set here.

    # By using these `base_...` attributes instead of the regular ModelAdmin `form` and `fieldsets`,
    # the additional fields of the child models are automatically added to the admin form.
    base_form = ServiceRecordAdminForm
    # base_fieldsets = ...


@register(Report)
class ReportAdmin(ServiceRecordChildAdmin):
    base_model = Report  # Explicitly set here!
    # define custom features here


@register(RadiologySession)
class RadiologySessionAdmin(ServiceRecordChildAdmin):
    base_model = RadiologySession  # Explicitly set here!
    # define custom features here


@register(VaccinationRecord)
class VaccinationRecordAdmin(ServiceRecordChildAdmin):
    base_model = VaccinationRecord  # Explicitly set here!
    # define custom features here


@register(ServiceRecord)
class ModelAParentAdmin(PolymorphicParentModelAdmin):
    """The parent model admin"""

    base_model = ServiceRecord  # Optional, explicitly set here.
    child_models = (
        Report,
        RadiologySession,
        VaccinationRecord,
    )
    list_filter = (PolymorphicChildModelFilter,)  # This is optional.
