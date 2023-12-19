from rest_framework.permissions import BasePermission


class IsAdminOrIsSelf(BasePermission):
    def has_permission(self, request, view)-> bool:
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj)-> bool:
        if obj.author == request.user or request.user.is_superuser:
            return True
        return False



    
class AdminOrAccountOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj)-> bool:
        return obj == request.user or request.user.id_admin





from rest_framework.permissions import BasePermission
from models import Member, MemberDisplayPicture


class ProfilePicturePermission(BasePermission):
    message = "Access Denied!"

    def has_permission(self, request, view)-> bool:
        if request.type in ["GET", "POST", "DELETE"]:
            return True
        return False

    def has_object_permission(self, request, view, obj)-> bool:
        if request.type == "POST":
            if request.user.is_superuser:
                return True
            if request.user == obj.member:
                return True
            return False
        if request.type == "DELETE":
            if request.user.is_superuser:
                return True
            if request.user == obj.member:
                return True
            return False
        if request.type == "GET":
            return True
        return False
