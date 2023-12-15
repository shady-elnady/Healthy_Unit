from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
import re

from ..utils.password_reset_link import generate_custom_password_link_from_firebase
from User.models import User


class UserPasswordResetView(APIView):
    """
    API endpoint to reset an existing drive user's password.
    """

    permission_classes = [AllowAny]
    authentication_classes = []

    @swagger_auto_schema(
        operation_summary="Reset an existing user's password",
        operation_description="Reset an existing user's password by providing the email address.",
        tags=["User Management"],
        manual_parameters=[
            openapi.Parameter(
                name="email",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Email of the user",
            )
        ],
        responses={
            200: "Password reset link sent successfully.",
            404: "User does not exist.",
        },
    )
    def get(self, request: Request):
        email = request.query_params.get("email")
        if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            bad_response = {
                "status": "failed",
                "message": "Enter a valid email address.",
            }
            return Response(bad_response, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
            first_name = user.first_name
            # sending custom password reset link
            try:
                user_email = email
                display_name = first_name.capitalize()
                generate_custom_password_link_from_firebase.delay(
                    user_email, display_name
                )
                response = {
                    "status": "success",
                    "message": "Password reset link sent successfully.",
                }
                return Response(response, status=status.HTTP_200_OK)
            except Exception:
                bad_response = {
                    "status": "failed",
                    "message": "Password reset link could not be sent; Please try again.",
                }
                return Response(bad_response, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            bad_response = {"status": "failed", "message": "User does not exist."}
            return Response(bad_response, status=status.HTTP_404_NOT_FOUND)
