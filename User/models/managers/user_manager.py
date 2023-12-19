from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
from typing import TYPE_CHECKING, Optional, Any
from django.db import transaction

from polymorphic_tree.managers import PolymorphicMPTTModelManager

if TYPE_CHECKING:
    from ..models.User import User

# from polymorphic.managers import PolymorphicManager


class UserManager(BaseUserManager, PolymorphicMPTTModelManager):
    def create_user(
        self,
        name: str,
        national_id: str,
        email: str,
        phone_number: str,
        password: Optional[str] = None,
        **extra_fields,
    ) -> "User":
        # if not email:
        #     raise ValueError("The Email must be set")
        values = [name, national_id, email, phone_number]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))

        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError(f"{_('The')} {field_name} {_('value must be set')}.")
        with transaction.atomic():
            user = self.model(
                name=name,
                national_id=national_id,
                email=self.normalize_email(email),
                phone_number=phone_number,
                **extra_fields,
            )
            user.set_password(password)
            user.save()
            return user

    def create_staffUser(
        self,
        name: str,
        national_id: str,
        email: str,
        phone_number: str,
        password: Optional[str] = None,
        **extra_fields,
    ) -> "User":
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_staff") is False:
            raise ValueError(f"{_('StaffUser must have')} is_staff=True.")
        return self.create_user(
            name, national_id, email, phone_number, password, **extra_fields
        )

    def create_superUser(
        self,
        name: str,
        national_id: str,
        email: str,
        phone_number: str,
        password: Optional[str] = None,
        **extra_fields,
    ) -> "User":
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_verified", True)
        extra_fields.setdefault("email_verified", True)
        extra_fields.setdefault("phone_number_verified", True)

        if extra_fields.get("is_staff") is False:
            raise ValueError(f"{_('Superuser must have')} is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(f"{_('Superuser must have')} is_superuser=True.")
        return self.create_user(
            name, national_id, email, phone_number, password, **extra_fields
        )

    def get_if_exist(self, **extra_fields: Any) -> "User":
        try:
            return self.get(
                **extra_fields,
            )
        except ObjectDoesNotExist:
            raise ValueError(_("User is Not Exist."))
