from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
import re

from ..utils.authentication import FireBaseAdminAuth
from ..utils.email_verfication_link import (
    generate_custom_email_from_firebase,
)
from Config.settings import pyrebase_auth
from ..handlers.api.Serializers import UserSerializer


class CreateNewUserView(APIView):
    """
    API endpoint to create a new user.
    """

    permission_classes = [AllowAny]
    authentication_classes = []

    @swagger_auto_schema(
        operation_summary="Create a new  user",
        operation_description="Create a new user by providing the required fields.",
        tags=["User Management"],
        request_body=UserSerializer,
        responses={201: UserSerializer(many=False), 400: "User creation failed."},
    )
    def post(self, request, format=None):
        data = request.data
        email = data.get("email")
        password = data.get("password")
        display_name = data.get("display_name")
        phone_number = data.get("phone_number")
        photo_url = data.get("photo_url")

        included_fields = [email, password, display_name, phone_number]
        # Check if any of the required fields are missing
        if not all(included_fields):
            bad_response = {"status": "failed", "message": "All fields are required."}
            return Response(bad_response, status=status.HTTP_400_BAD_REQUEST)

        # Check if email is valid
        if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            bad_response = {
                "status": "failed",
                "message": "Enter a valid email address.",
            }
            return Response(bad_response, status=status.HTTP_400_BAD_REQUEST)

        # Check if password is less than 8 characters
        if len(password) < 8:
            bad_response = {
                "status": "failed",
                "message": "Password must be at least 8 characters long.",
            }
            return Response(bad_response, status=status.HTTP_400_BAD_REQUEST)
        # Check if password contains at least one uppercase letter, one lowercase letter, one digit, and one special character
        if password and not re.match(
            r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_+{}\[\]:;<>,.?~\\-]).{8,}$",
            password,
        ):
            bad_response = {
                "status": "failed",
                "message": "Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character.",
            }
            return Response(bad_response, status=status.HTTP_400_BAD_REQUEST)

        try:
            # create user on firebase
            user = pyrebase_auth.create_user_with_email_and_password(email, password)
            # create user on django database
            uid = user["localId"]
            data["firebase_uid"] = uid
            data["is_active"] = True

            # sending custom email verification link
            try:
                user_email = email
                display_name = display_name.capitalize()
                generate_custom_email_from_firebase.delay(user_email, display_name)
            except Exception:
                # delete user from firebase if email verification link could not be sent
                FireBaseAdminAuth.delete_user(uid)
                bad_response = {
                    "status": "failed",
                    "message": "Email verification link could not be sent; Please try again.",
                }
                return Response(bad_response, status=status.HTTP_400_BAD_REQUEST)

            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                response = {
                    "status": "success",
                    "message": "User created successfully.",
                    "data": serializer.data,
                }
                return Response(response, status=status.HTTP_201_CREATED)
            else:
                pyrebase_auth.delete_user_account(user["idToken"])
                bad_response = {
                    "status": "failed",
                    "message": "User signup failed.",
                    "data": serializer.errors,
                }
                return Response(bad_response, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            bad_response = {"status": "failed", "message": str(e)}
            return Response(bad_response, status=status.HTTP_400_BAD_REQUEST)
