from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated

from ..utils.authentication import FirebaseAuthentication, FireBaseAdminAuth
from ..handlers.api.Serializers import UserSerializer, UserUpdateSerializer
from User.models import User


class RetrieveUpdateDestroyUserView(APIView):
    """
    API endpoint to retrieve, update, or delete an existing user.
    """

    permission_classes = [IsAuthenticated]
    authentication_classes = [FirebaseAuthentication]

    @swagger_auto_schema(
        operation_summary="Retrieve details of an existing user",
        operation_description="Retrieve details of an existing user based on their primary key.",
        tags=["User Management"],
        responses={200: UserSerializer(many=False), 404: "User does not exist."},
    )
    def get(self, request: Request, pk: int):
        try:
            user_firebase_access_token = (
                request.META.get("HTTP_AUTHORIZATION").split(" ").pop()
            )
            decode_access_token = FireBaseAdminAuth.verify_id_token(
                user_firebase_access_token
            )
            user_firebase_uid = decode_access_token.get("uid")
        except Exception:
            bad_response = {
                "status": "failed",
                "message": "Invalid authentication token provided.",
            }
            return Response(bad_response, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(pk=pk, firebase_uid=user_firebase_uid)
        except User.DoesNotExist:
            bad_response = {"status": "failed", "message": "User does not exist."}
            return Response(bad_response, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            bad_response = {"status": "failed", "message": "User does not exist."}
            return Response(bad_response, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(user)
        response = {
            "status": "success",
            "message": "User retrieved successfully.",
            "data": serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Update an existing user's information",
        operation_description="Update an existing user's information by providing the fields to be modified.",
        tags=["User Management"],
        request_body=UserUpdateSerializer,
        responses={
            200: UserUpdateSerializer(many=False),
            400: "User update failed.",
            404: "User does not exist.",
        },
    )
    def patch(self, request: Request, pk: int):
        data = request.data
        try:
            user_firebase_access_token = (
                request.META.get("HTTP_AUTHORIZATION").split(" ").pop()
            )
            decode_access_token = FireBaseAdminAuth.verify_id_token(
                user_firebase_access_token
            )
            user_firebase_uid = decode_access_token.get("uid")
        except Exception:
            bad_response = {
                "status": "failed",
                "message": "Invalid authentication token provided.",
            }
            return Response(bad_response, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(pk=pk, firebase_uid=user_firebase_uid)
        except User.DoesNotExist:
            bad_response = {"status": "failed", "message": "User does not exist."}
            return Response(bad_response, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            bad_response = {"status": "failed", "message": "User does not exist."}
            return Response(bad_response, status=status.HTTP_400_BAD_REQUEST)

        # Check if any keys in data are not in the list of allowed fields
        invalid_keys = [
            key for key in data.keys() if key not in ["first_name", "last_name"]
        ]
        if invalid_keys:
            bad_response = {
                "status": "failed",
                "message": f"Only 'first_name', 'last_name', can be updated. Invalid field(s): {', '.join(invalid_keys)}",
            }
            return Response(bad_response, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserUpdateSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": "success",
                "message": "User updated successfully.",
                "data": serializer.data,
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            bad_response = {
                "status": "failed",
                "message": "User update failed.",
                "data": serializer.errors,
            }
            return Response(bad_response, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Delete an existing user",
        operation_description="Delete an existing user both on firebase and django database  based on their primary key.",
        tags=["User Management"],
        responses={204: "User deleted successfully.", 404: "User does not exist."},
    )
    def delete(self, request: Request, pk):
        try:
            user_firebase_access_token = (
                request.META.get("HTTP_AUTHORIZATION").split(" ").pop()
            )
            decode_access_token = FireBaseAdminAuth.verify_id_token(
                user_firebase_access_token
            )
            user_firebase_uid = decode_access_token.get("uid")
        except Exception:
            bad_response = {
                "status": "failed",
                "message": "Invalid authentication token provided.",
            }
            return Response(bad_response, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(pk=pk, firebase_uid=user_firebase_uid)
            try:
                FireBaseAdminAuth.delete_user(user_firebase_uid)
            except Exception:
                bad_response = {
                    "status": "failed",
                    "message": "User does not exist on firebase.",
                }
                return Response(bad_response, status=status.HTTP_404_NOT_FOUND)
            user.delete()
            response = {"status": "success", "message": "User deleted successfully."}
            return Response(response, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            bad_response = {"status": "failed", "message": "User does not exist."}
            return Response(bad_response, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            bad_response = {"status": "failed", "message": "User does not exist."}
            return Response(bad_response, status=status.HTTP_400_BAD_REQUEST)
