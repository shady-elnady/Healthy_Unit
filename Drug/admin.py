# from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline, StackedInline, register
from django.db import models
from django.template.loader import get_template
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

# from django.contrib.contenttypes.admin import GenericTabularInline
# from django.utils.crypto import get_random_string

from .models import PharmaceuticalForm, DrugEffectiveMaterial, Drug, DrugPacking
from Language.widgets.myTranslation_json_widget import MyTranslationWidget
from Utils.Helpers.cach_mixin import CachedMixin
from Utils.Helpers.extended_actions_mixin import ExtendedActionsMixin
from .forms import PharmaceuticalFormAdminForm


@register(PharmaceuticalForm)
class PharmaceuticalFormAdmin(ModelAdmin):
    form = PharmaceuticalFormAdminForm
    formfield_overrides = {
        models.JSONField: {
            "widget": MyTranslationWidget,
        },
    }


@register(DrugPacking)
class DrugPackingModelAdmin(CachedMixin, ExtendedActionsMixin, ModelAdmin):
    fields = (
        "bar_code",
        "drug",
        "pharmaceutical_form",
        "price",
        "currency",
        "image",
    )


class DrugPackingAdminInline(StackedInline):
    extra = 1
    model = DrugPacking


@register(Drug)
class DrugModelAdmin(CachedMixin, ExtendedActionsMixin, ModelAdmin):
    inlines = (DrugPackingAdminInline,)
    fields = (
        "name",
        "category",
        "brand",
        # "drug_effective_material",
        "drug_packing_inline",
        "translations",
    )
    formfield_overrides = {
        models.JSONField: {
            "widget": MyTranslationWidget,
        },
    }
    readonly_fields = ("drug_packing_inline",)

    def changeform_view(self, request, *args, **kwargs):
        self.request = request
        return super().changeform_view(request, *args, **kwargs)

    ###
    def drug_packing_inline(self, *args, **kwargs):
        context = (
            getattr(self.response, "context_data", None) or {}
        )  # somtimes context.copy() is better
        inline = context["inline_admin_formset"] = context["inline_admin_formsets"].pop(
            0
        )
        return get_template(inline.opts.template).render(context, self.request)

    def render_change_form(self, request, context, *args, **kwargs):
        self.request = request
        self.response = super().render_change_form(request, context, *args, **kwargs)
        return self.response


class DrugInlineForm(StackedInline.form):
    def __init__(self, *args, **kwargs):
        super(DrugInlineForm, self).__init__(*args, **kwargs)
        self.instance.form = self

    def is_valid(self):
        return super().is_valid() and self.nested.formset.is_valid()

    @cached_property
    def nested(self):
        modeladmin = DrugModelAdmin(self._meta.model, self.modeladmin.admin_site)

        # get formsets and instances for change/add view depending on the request
        formsets, instances = modeladmin._create_formsets(
            self.modeladmin.request, self.instance, change=self.instance.pk
        )

        # gets the inline from inline_formsets
        inline = modeladmin.get_inline_formsets(
            self.modeladmin.request, formsets[:1], instances[:1], self.instance
        )[0]

        # handles prefix
        inline.formset.prefix = f"{self.prefix}_{formsets[0].prefix}".replace("-", "_")
        return inline

    def is_multipart(self, *args, **kwargs):
        return super().is_multipart() or self.nested.formset.form().is_multipart()

    @cached_property
    def changed_data(self):
        changed_inline_fields = []
        for form in self.nested.formset:
            for name, bf in form._bound_items():
                if bf._has_changed():
                    changed_inline_fields.append(name)
        return super().changed_data + changed_inline_fields

    def save(self, *args, **kwargs):
        response = super().save(*args, **kwargs)
        self.nested.formset.save(*args, **kwargs)
        return response


class DrugInline(StackedInline):
    extra = 3
    model = Drug
    fields = (
        "name",
        "translations",
        "drug_effective_material",
        "category",
        "brand",
        "drug_packing_inline",
    )
    readonly_fields = ("drug_packing_inline",)
    formfield_overrides = {
        models.JSONField: {
            "widget": MyTranslationWidget,
        },
    }
    form = DrugInlineForm

    def drug_packing_inline(self, obj=None, *args, **kwargs):
        context = getattr(self.modeladmin.response, "context_data", None) or {}
        # insert nested inline from form
        return get_template(obj.form.nested.opts.template).render(
            context | {"inline_admin_formset": obj.form.nested}, self.modeladmin.request
        )

    def get_formset(self, *args, **kwargs):
        formset = super().get_formset(*args, **kwargs)
        # from.modeladmin is needed in property form.nested
        # for nested inline
        formset.form.modeladmin = self.modeladmin
        return formset


@register(DrugEffectiveMaterial)
class DrugEffectiveMaterialModelAdmin(CachedMixin, ExtendedActionsMixin, ModelAdmin):
    inlines = (DrugInline,)
    fields = (
        "name",
        "translations",
        "for_child_pregnant",
        # "drug_effective_material_category",
    )
    formfield_overrides = {
        models.JSONField: {
            "widget": MyTranslationWidget,
        },
    }

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
