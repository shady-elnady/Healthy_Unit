from rest_framework.permissions import BasePermission, SAFE_METHODS


class AuthorAllStaffAllButEditOrReadOnly(BasePermission):
    edit_methods = ("PUT", "PATCH")  # 'GET', 'HEAD', 'OPTIONS'

    def has_permission(self, request, view) -> bool:
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj) -> bool:
        if request.user.is_superuser:
            return True

        if request.method in SAFE_METHODS:
            return True

        if obj.author == request.user:
            return True

        if request.user.is_staff and request.method not in self.edit_methods:
            return True

        return False
