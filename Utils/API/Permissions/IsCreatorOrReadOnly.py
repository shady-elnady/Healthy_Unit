from rest_framework.permissions import BasePermission, SAFE_METHODS
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from User.models import User


class IsCreatorOrReadOnlyPermission(BasePermission):
    """
    Object-level permission to only allow creators of an object
    to edit / delete it. Assumes the model instance has a
    `creator` attribute."""

    def has_object_permission(self, request, view, obj)-> bool:
        # Always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True
        # Instance must have an attribute named `creator`.
        return obj.creator == request.user
