from rest_framework.permissions import BasePermission

from Utils.models.Blocklist import Blocklist


class BlocklistPermission(BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_permission(self, request, view)-> bool:
        return not Blocklist.objects.filter(
            ip_address=request.META["REMOTE_ADDR"],
        ).exists()
