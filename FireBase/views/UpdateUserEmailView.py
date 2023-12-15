from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
import re
from Config.settings import pyrebase_auth

from ..utils.authentication import FirebaseAuthentication, FireBaseAdminAuth
from ..handlers.api.Serializers import UserEmailUpdateSerializer
from User.models import User


class UpdateUserEmailView(APIView):
    """
    API endpoint to update an existing  user's email address on firebase and in the database.
    """

    permission_classes = [IsAuthenticated]
    authentication_classes = [FirebaseAuthentication]

    @swagger_auto_schema(
        operation_summary="Update an existing  user's email address on firebase and in the database",
        operation_description="Update an existing user's email address on firebase by providing the new email and firebase uid.",
        tags=["User Management"],
        request_body=UserEmailUpdateSerializer,
        responses={
            200: "User email updated successfully.",
            400: "new email and firebase uid are required.",
            404: "User does not exist.",
        },
    )
    def patch(self, request: Request):
        data = request.data
        email = data.get("email")
        firebase_uid = data.get("firebase_uid")
        included_fields = [email, firebase_uid]
        if not all(included_fields):
            bad_response = {
                "status": "failed",
                "message": "new email and firebase uid are required.",
            }
            return Response(bad_response, status=status.HTTP_400_BAD_REQUEST)

        if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            bad_response = {
                "status": "failed",
                "message": "Enter a valid email address.",
            }
            return Response(bad_response, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = FireBaseAdminAuth.update_user(firebase_uid, email=email)
        except Exception:
            bad_response = {"status": "failed", "message": "User does not exist."}
            return Response(bad_response, status=status.HTTP_404_NOT_FOUND)
        try:
            existing_user = User.objects.get(uid=firebase_uid)
            existing_user.email = email
            existing_user.save()
            response = {
                "status": "success",
                "message": "User email updated successfully.",
            }
            return Response(response, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            pyrebase_auth.delete_user_account(user["idToken"])
            bad_response = {"status": "failed", "message": "User does not exist."}
            return Response(bad_response, status=status.HTTP_404_NOT_FOUND)
