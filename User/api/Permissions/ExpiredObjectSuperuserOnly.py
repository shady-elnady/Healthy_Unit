from datetime import datetime, timedelta

from django.utils import timezone
from rest_framework import permissions


class ExpiredObjectSuperuserOnly(permissions.BasePermission):
    def object_expired(self, obj):
        expired_on = timezone.make_aware(datetime.now() - timedelta(minutes=10))
        return obj.created < expired_on

    def has_object_permission(self, request, view, obj):
        if self.object_expired(obj) and not request.user.is_superuser:
            return False
        else:
            return True
