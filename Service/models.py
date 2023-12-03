# from django.db import models
from django.db.models import TextField, ForeignKey, CASCADE
from django.utils.translation import gettext_lazy as _
from User.models.Profile import Profile

from Utils.models.BaseModel import BaseBarCodeModel, BaseImageModel
from Utils.models.BasePolymorphic import BasePolymorphicSingleModel
from Utils.models.BaseTreeNode import BaseTreeNodeSingleModel
from Language.models.BaseTranslationModel import BaseTranslationModel
from Client.models import Client
from Employee.models import Employee

# Create your models here.


class Service(BaseTranslationModel, BaseTreeNodeSingleModel):
    def save(self, *args, **kwargs):
        self.full_clean()
        if self.__class__.__name__ == "ParentService":
            self.parent = None
        else:
            self.parent, created = Service.objects.get_or_create(
                name=self.__class__.__name__,
            )
        return super(Service, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")


class ParentService(Service, BaseImageModel):
    managing_director = ForeignKey(
        Employee,
        null=True,
        blank=True,
        on_delete=CASCADE,
        related_name="%(class)s",
        verbose_name=_("Managing Director"),
    )  # المدير المسؤول

    class Meta:
        verbose_name = _("Parent Service")
        verbose_name_plural = _("Parent Services")


class ServiceRecord(BaseBarCodeModel, BasePolymorphicSingleModel):
    service = ForeignKey(
        Service,
        on_delete=CASCADE,
        related_name="%(class)s",
        limit_choices_to={"parent__isnull": False},
        verbose_name=_("Service"),
    )
    patient = ForeignKey(
        Profile,  # Profile
        on_delete=CASCADE,
        related_name="%(class)s",
        verbose_name=_("Patient"),
    )
    diagnosis = TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Diagnosis"),
    )
    note = TextField(
        verbose_name=_("Note"),
    )

    class Meta:
        verbose_name = _("Service Record")
        verbose_name_plural = _("Services Records")
