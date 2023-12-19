from rest_framework.permissions import BasePermission, SAFE_METHODS
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from User.models import User


class IsSuperUserPermission(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view)-> bool:
        user: User = request.user
        return bool(user and user.is_superuser)
