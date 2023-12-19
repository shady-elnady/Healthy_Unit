from rest_framework.permissions import BasePermission, SAFE_METHODS
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from User.models import User


class IsCustomerPermission(BasePermission):
    def has_permission(self, request, view)-> bool:
        if "auth.is_customer" in request.user.get_all_permissions():
            return True
        return False

    def has_object_permission(self, request, view, obj)-> bool:
        if "auth.is_customer" in request.user.get_all_permissions():
            return True
        return False
