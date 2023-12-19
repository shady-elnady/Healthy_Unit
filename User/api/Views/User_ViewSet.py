from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import (
    TokenAuthentication,
    SessionAuthentication,
    BasicAuthentication,
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from http import HTTPMethod
from uuid import UUID
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from EMail.Helpers.EMail_Sender import EMailSender
from User.models.User import User
from ..Serializers.User_Serializer import UserSerializer

# import pyotp


class UserViewSet(ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """

    basename = "user"
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]

    @action(
        detail=True,
        methods=[HTTPMethod.POST],
        # permission_classes=[IsSelf],
        name="Password ReSet",
        url_path="password_reset",
        url_name="password_reset",
    )
    def password_reset(self, request, uid: UUID = None):
        user: User = self.get_object()
        user_email = getattr(user, User.get_email_field_name())
        context = {
            "name": user.display_name,
            "password_rest_url": UserViewSet.reverse_action(
                UserViewSet.password_reset_confirm.url_name,
                args=[
                    urlsafe_base64_encode(force_bytes(user.uid)),
                    default_token_generator.make_token(user),
                ],
            ),
        }
        EMailSender(
            user_email,
        ).send_template(
            template_name="password_reset",
            context=context,
        )
        return Response(
            data=urlsafe_base64_encode(force_bytes(user.uid)),
            status=status.HTTP_200_OK,
        )

    # @action(
    #     detail=True,
    #     methods=[HTTPMethod.GET],
    #     permission_classes=[IsSelf],
    #     name="Password ReSet Confirm",
    #     url_path="password_reset_confirm",
    #     url_name="password_reset_confirm",
    # )
    # def password_reset_confirm(self, request, uid: UUID = None, token: str = None):
    #     user: User = self.get_object()
    #     serializer: PasswordResetSerializer = PasswordResetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         user.set_password(serializer.validated_data["password"])
    #         user.save()
    #         return Response({"status": "password set"})
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @action(detail=True, methods=[HTTPMethod.POST])
    # def set_password(self, request, pk=None):
    #     user = self.get_object()
    #     serializer = PasswordSerializer(data=request.data)
    #     if serializer.is_valid():
    #         user.set_password(serializer.validated_data["password"])
    #         user.save()
    #         return Response({"status": "password set"})
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @action(detail=False)
    # def recent_users(self, request):
    #     recent_users = User.objects.all().order_by("-last_login")

    #     page = self.paginate_queryset(recent_users)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)

    #     serializer = self.get_serializer(recent_users, many=True)
    #     return Response(serializer.data)


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
