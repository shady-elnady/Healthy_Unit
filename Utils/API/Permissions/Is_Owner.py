from rest_framework.permissions import BasePermission


class IsOwnerPermission(BasePermission):
    message = "You must be the owner of this object."

    def has_permission(self, request, view)-> bool:
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj)-> bool:
        # return obj == request.user
        return obj.user == request.user
