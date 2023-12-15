from django.conf import settings
import requests
import json

from Utils.entities.Value_Objects import UUID
from ..utils.authentication import FireBaseAdminAuth
from .repository.abstract_fire_helper import AbstractFireBaseHelper
from User.models import User


class ByBaseController(AbstractFireBaseHelper):
    def get_user(
        self,
        uid: UUID = None,
        email: str = None,
        mobile: str = None,
    ) -> "User":
        try:
            if uid:
                return FireBaseAdminAuth.get_user(uid)
            elif email:
                return FireBaseAdminAuth.get_user_by_email(email)
            elif mobile:
                return FireBaseAdminAuth.get_user_by_phone_number(mobile)
        except Exception:
            pass

    def get_users(
        self,
        uid1: UUID = None,
        email: str = None,
        mobile: str = None,
    ) -> ["User"]:
        try:
            result = FireBaseAdminAuth.get_users(
                [
                    FireBaseAdminAuth.UidIdentifier(uid1),
                    FireBaseAdminAuth.EmailIdentifier(email),
                    FireBaseAdminAuth.PhoneIdentifier(mobile),
                    FireBaseAdminAuth.ProviderIdentifier("google.com", "google_uid4"),
                ]
            )

            print("Successfully fetched user data:")
            for user in result.users:
                print(user.uid)

            print("Unable to find users corresponding to these identifiers:")
            for uid in result.not_found:
                print(uid)
        except Exception:
            pass

    def create_user(
        self,
        uid: UUID,
        email: str,
        phone_number: str,
        display_name: str,
        photo_url: str,
        password: str,
        email_verified: bool = False,
        disabled: bool = False,
    ) -> "UUID":
        """
        Function for creating firebase user.
        """
        try:
            created_user = FireBaseAdminAuth.create_user(
                uid=uid,
                email=email,
                email_verified=email_verified,
                phone_number=phone_number,
                password=password,
                display_name=display_name,
                photo_url=photo_url,
                disabled=disabled,
            )
            return created_user.uid
        except Exception:
            pass

    def update_user(
        self,
        uid: UUID,
        email: str,
        phone_number: str,
        display_name: str,
        photo_url: str,
        password: str,
        email_verified: bool = False,
        disabled: bool = False,
    ) -> "UUID":
        """
        Function for creating firebase user.
        """
        try:
            updated_user = FireBaseAdminAuth.update_user(
                uid,
                email=email,
                email_verified=email_verified,
                phone_number=phone_number,
                password=password,
                display_name=display_name,
                photo_url=photo_url,
                disabled=disabled,
            )
            return updated_user.uid
        except Exception:
            pass

    def delete_user(self, uid) -> bool:
        """
        Function for deleting firebase user.
        """
        try:
            FireBaseAdminAuth.delete_user(uid)
            return True
        except Exception:
            return False

    def delete_many_users(self, uids: ["UUID"]) -> {}:
        """
        Function for deleting firebase user.
        """
        try:
            result = FireBaseAdminAuth.delete_users(uids)
            return {
                "success_count": result.success_count,
                "failure_count": result.failure_count,
                "errors": [
                    {
                        "index": result.index,
                        "reason": result.reason,
                    }
                    for err in result.errors
                ],
            }
        except Exception as e:
            return e

    def login_by_email(self, email, password):
        """
        Function for login firebase user.
        """
        payload = json.dumps(
            {"email": email, "password": password, "returnSecureToken": True}
        )

        r = requests.post(
            settings.REST_API_URL,
            params={"key": settings.FIREBASE_WEB_API_KEY},
            data=payload,
        )
        return r.json()

    def verify_token(self, id_token: str):
        try:
            decoded_token = FireBaseAdminAuth.verify_id_token(id_token)
            uid = decoded_token["uid"]
            return uid
        except Exception:
            pass

    def logout(uid):
        FireBaseAdminAuth.revoke_refresh_tokens(uid)


"""
    https://firebase.google.com/docs/auth/admin/manage-users
"""
