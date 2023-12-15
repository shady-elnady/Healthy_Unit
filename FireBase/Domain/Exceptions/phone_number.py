from rest_framework import status
from rest_framework.exceptions import APIException
from django.utils.translation import gettext_lazy as _


class InvalidPhoneNumberException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = (
        _(
            "Phone Number must not consist of space and requires country code. eg : +6591258565."
        ),
    )
    default_code = "invalid_phone_number"


# class InvalidPhoneNumberException(Exception):
#     def __init__(
#         self,
#         meassage: str = _(
#             "Phone Number must not consist of space and requires country code. eg : +6591258565."
#         ),
#         status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#     ):
#         self.meassage = meassage
#         self.status_code = status_code

#     def __str__(self):
#         return str(self.meassage)
