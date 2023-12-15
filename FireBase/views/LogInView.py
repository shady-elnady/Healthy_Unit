from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import check_password
from Config.settings import pyrebase_auth

from ..handlers.api.Serializers import UserSerializer
from User.models import User


class LogInView(APIView):
    """
    API endpoint to login an existing user.
    """

    permission_classes = [AllowAny]
    authentication_classes = []

    @swagger_auto_schema(
        operation_summary="Login an existing user",
        operation_description="Login an existing user by providing the required fields.",
        tags=["User Management"],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "email": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Email of the user"
                ),
                "password": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Password of the user"
                ),
            },
        ),
        responses={200: UserSerializer(many=False), 404: "User does not exist."},
    )
    def post(self, request: Request):
        data = request.data
        email = data.get("email")
        password = data.get("password")

        try:
            user = pyrebase_auth.sign_in_with_email_and_password(email, password)
        except Exception:
            bad_response = {"status": "failed", "message": "Invalid email or password."}
            return Response(bad_response, status=status.HTTP_400_BAD_REQUEST)

        try:
            existing_user = User.objects.get(email=email)

            # update password if it is not the same as the one in the database
            if not check_password(password, existing_user.password):
                existing_user.set_password(password)
                existing_user.save()

            serializer = UserSerializer(existing_user)
            extra_data = {
                "firebase_id": user["localId"],
                "firebase_access_token": user["idToken"],
                "firebase_refresh_token": user["refreshToken"],
                "firebase_expires_in": user["expiresIn"],
                "firebase_kind": user["kind"],
                "user_data": serializer.data,
            }
            response = {
                "status": "success",
                "message": "User logged in successfully.",
                "data": extra_data,
            }
            return Response(response, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            pyrebase_auth.delete_user_account(user["idToken"])
            bad_response = {"status": "failed", "message": "User does not exist."}
            return Response(bad_response, status=status.HTTP_404_NOT_FOUND)
