from rest_framework import status
from rest_framework.exceptions import APIException


class NoAuthToken(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "No authentication token provided"
    default_code = "no_auth_token"


class ExpiredAuthToken(APIException):
    """
    Exception class for expired authentication token.
    """

    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Expired authentication token provided."
    default_code = "expired_auth_token"


class InvalidAuthToken(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Invalid authentication token provided"
    default_code = "invalid_token"


class FirebaseError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "The user provided with the auth token is not a valid Firebase user, it has no Firebase UID"
    default_code = "no_firebase_uid"


class EmailVerification(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Email not verified."
    default_code = "email_not_verified"
