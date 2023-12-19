from django.core.exceptions import MultipleObjectsReturned
from django.contrib.auth.backends import ModelBackend
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from typing import Optional
from uuid import UUID

from ..models.User import User


class MyModelBackend(ModelBackend):
    def authenticate(
        self,
        request,
        nationalID_or_EMail_or_Phone_or_Name_or_DisplayName: str,
        password: str,
        **kwargs,
    ) -> "User":
        try:
            user = User.objects.get(
                Q(name__iexact=nationalID_or_EMail_or_Phone_or_Name_or_DisplayName)
                | Q(
                    phone_number__iexact=nationalID_or_EMail_or_Phone_or_Name_or_DisplayName
                )
                | Q(
                    display_name__iexact=nationalID_or_EMail_or_Phone_or_Name_or_DisplayName
                )
                | Q(
                    national_id__iexact=nationalID_or_EMail_or_Phone_or_Name_or_DisplayName
                )
                | Q(email__iexact=nationalID_or_EMail_or_Phone_or_Name_or_DisplayName)
            )
        except User.DoesNotExist:
            pass
        except MultipleObjectsReturned:
            user = (
                User.objects.filter(
                    national_id__iexact=nationalID_or_EMail_or_Phone_or_Name_or_DisplayName
                )
                .order_by(id)
                .first()
            )
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

    def get_user(self, user_id: UUID) -> Optional[User]:
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
