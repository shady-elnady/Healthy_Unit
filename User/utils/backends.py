from .authenticate_check import check_is_email, check_is_mobile, check_is_nationalID
from django.utils.translation import gettext_lazy as _

from ..models.User import User


class EmailOrNationalIDOrMobileBackend(object):
    def authenticate(
        self,
        national_id_or_email_or_mobile=None,
        national_id=None,
        email=None,
        mobile=None,
        password=None,
        **kargs,
    ) -> "User":
        user = None
        try:
            if national_id_or_email_or_mobile is None:
                if email is not None:
                    user = User.objects.get(email=email, **kargs)
                elif national_id is not None:
                    user = User.objects.get(national_id=national_id, **kargs)
                elif mobile is not None:
                    user = User.objects.get(mobile=mobile, **kargs)
                else:
                    raise ValueError(_("Enter your E-Mail or National ID or Mobile"))
            else:
                if check_is_email(national_id_or_email_or_mobile):
                    user = User.objects.get(
                        email=national_id_or_email_or_mobile,
                        **kargs,
                    )
                elif check_is_nationalID(national_id_or_email_or_mobile):
                    user = User.objects.get(
                        national_id=national_id_or_email_or_mobile,
                        **kargs,
                    )
                elif check_is_mobile(national_id_or_email_or_mobile):
                    user = User.objects.get(
                        mobile=national_id_or_email_or_mobile,
                        **kargs,
                    )
                else:
                    raise ValueError(
                        _(
                            "national_id_or_email_or_mobile Not E-Mail or National ID or Mobile",
                        )
                    )
        except User.DoesNotExist:
            raise ValueError(_("User Not Exist."))
        try:
            if user.check_password(password):
                return user
        except:
            raise ValueError(_("Password is Wrong."))

    def get_user_by_id(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
