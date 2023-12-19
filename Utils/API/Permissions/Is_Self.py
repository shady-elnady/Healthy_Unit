from rest_framework.permissions import BasePermission


class IsSelfPermission(BasePermission):
    def has_permission(self, request, view) -> bool:
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj) -> bool:
        return obj == request.user
