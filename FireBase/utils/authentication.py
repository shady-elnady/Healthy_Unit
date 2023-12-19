# import uuid
# from django.conf import settings
# from rest_framework.authentication import BaseAuthentication
# from firebase_admin import (
#     credentials,
#     auth as FireBaseAdminAuth,
#     initialize_app,
# )

# from Utils.Exceptions.api_exceptions import (
#     FirebaseError,
#     InvalidAuthToken,
#     NoAuthToken,
#     EmailVerification,
# )
# from User.models.User import User

# """SETUP FIREBASE CREDENTIALS"""
# cred = credentials.Certificate(
#     {
#         "type": settings.FIREBASE_ACCOUNT_TYPE,
#         "project_id": settings.FIREBASE_PROJECT_ID,
#         "private_key_id": settings.FIREBASE_PRIVATE_KEY_ID,
#         "private_key": settings.FIREBASE_PRIVATE_KEY.replace("\\n", "\n"),
#         "client_email": settings.FIREBASE_CLIENT_EMAIL,
#         "client_id": settings.FIREBASE_CLIENT_ID,
#         "auth_uri": settings.FIREBASE_AUTH_URI,
#         "token_uri": settings.FIREBASE_TOKEN_URI,
#         "auth_provider_x509_cert_url": settings.FIREBASE_AUTH_PROVIDER_X509_CERT_URL,
#         "client_x509_cert_url": settings.FIREBASE_CLIENT_X509_CERT_URL,
#     }
# )
# # cred = os.path.join(
# #    settings.BASE_DIR
# #     "FireBase",
# #     "config",
# #     "healthy-unit-firebase-adminsdk-w4s96-7f59d08a29.json",
# # )

# try:
#     default_app = initialize_app(cred)
# except Exception:
#     raise FirebaseError(
#         "Firebase Admin SDK credentials not found. Please add the path to the credentials file to the FIREBASE_ADMIN_SDK_CREDENTIALS_PATH environment variable."
#     )


# # FIREBASE AUTHENTICATION
# class FirebaseAuthentication(BaseAuthentication):
#     """override authenticate method and write our custom firebase authentication."""

#     keyword = "Bearer"

#     def authenticate(self, request):
#         """Get the authorization Token, It raise exception when no authorization Token is given"""
#         auth_header = request.META.get("HTTP_AUTHORIZATION")
#         if not auth_header:
#             raise NoAuthToken("No auth token provided")
#         """Decoding the Token It rasie exception when decode failed."""
#         id_token = auth_header.split(" ").pop()
#         decoded_token = None
#         try:
#             decoded_token = FireBaseAdminAuth.verify_id_token(id_token)
#         except Exception:
#             raise InvalidAuthToken("Invalid auth token")

#         """Return Nothing"""
#         if not id_token or not decoded_token:
#             return None

#         """verify email"""
#         email_verified = decoded_token.get("email_verified")
#         if not email_verified:
#             raise EmailVerification(
#                 "Email not verified. please verify your email address."
#             )

#         """Get the uid of an user"""
#         try:
#             uid = decoded_token.get("uid")
#         except Exception:
#             raise FirebaseError()
#         """Get or create the user"""
#         # user, created = User.objects.get_or_create(username=uid)
#         # return (user, None)
#         try:
#             user = User.objects.get(uid=uid)
#             return user, None
#         except User.DoesNotExist:
#             return None

#     def get_user(self, user_uid: uuid.UUID) -> "User":
#         try:
#             return User.objects.get(uid=user_uid)
#         except User.DoesNotExist:
#             return None
