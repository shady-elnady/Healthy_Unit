import base64
from datetime import datetime
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import (
    TokenAuthentication,
    SessionAuthentication,
    BasicAuthentication,
)
import django_filters.rest_framework

from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status, filters
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import action
from rest_framework.response import Respons
from http import HTTPMethod

from User.models.User import User
from User.api.Permissions.Is_AdminOrIs_Self import IsAdminOrIsSelf
from ..Serializers.User_Serializer import UserSerializer
from ..Serializers.Password_Serializer import PasswordSerializer

# import pyotp


class UserViewSet(ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]
    basename = "user"  # Meta.model()

    @action(detail=True, methods=[HTTPMethod.POST])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data["password"])
            user.save()
            return Response({"status": "password set"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False)
    def recent_users(self, request):
        recent_users = User.objects.all().order_by("-last_login")

        page = self.paginate_queryset(recent_users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["post"], permission_classes=[IsAdminOrIsSelf])
    def set_password(self, request, pk=None):
        pass

    @action(detail=True, methods=["put"], name="Change Password")
    def password(self, request, pk=None):
        """Update the user's password."""

    @password.mapping.delete
    def delete_password(self, request, pk=None):
        """Delete the user's password."""


"""
    def post(
        self,
        request,
    ):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response(
                {
                    "token": user.auth_token.key,
                },
            )
        else:
            return Response(
                {
                    "error": "Wrong Credentials",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
"""
