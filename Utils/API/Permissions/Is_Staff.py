from rest_framework import permissions


class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        return request.user.is_staff

    def has_object_permission(self, request, view, obj) -> bool:
        return request.user.is_staff
