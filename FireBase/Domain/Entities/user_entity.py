import re
from typing import Optional
import uuid
from pydantic import BaseModel, EmailStr, Field, validator, constr

from User.models.User import User

from ..Exceptions.phone_number import InvalidPhoneNumberException


class UserEntity(BaseModel):
    uid: uuid.UUID = Field(default_factory=lambda: uuid.uuid4())
    display_name: str
    email: EmailStr
    phone_number: str
    photo_url: str
    password: str
    email_verified: bool
    disabled: bool
    ##
    # phone_number: Optional[
    #     constr(
    #         strip_whitespace=True,
    #         min_length=9,
    #         max_length=15,
    #     )
    # ]
    ##
    # phone_number: Optional[
    #     constr(
    #         strip_whitespace=True,
    #         regex=r"^(\+)[1-9][0-9\-\(\)\.]{9,15}$",
    #     )
    # ]

    @validator("phone_number")
    def phone_number_validation(cls, value):
        # For reference - https://stackoverflow.com/questions/70414211/pydantic-custom-data-type-for-phone_number-number
        # -value-error-missing
        regex = r"^(\+)[1-9][0-9\-\(\)\.]{9,15}$"
        if value and not re.search(regex, value, re.I):
            raise InvalidPhoneNumberException("Invalid Phone Number.")
        # another Method
        prog = re.compile(regex)
        if prog.search(value):
            raise InvalidPhoneNumberException("Invalid Phone Number.")
        # query a user with the same phone_number
        if User.objects.filter(phone_number=value).all():
            raise ValueError("Phone Number must be unique")
        return value

    @validator("display_name")
    def validate_unique_display_name(cls, value):
        # query a user with the same Display Name
        res = User.objects.filter(display_name=value).all()
        if res:
            raise ValueError("Display Name must be unique")
        return value

    @validator("email")
    def validate_unique_display_name(cls, value):
        # query a user with the same E-Mail
        res = User.objects.filter(email=value).all()
        if res:
            raise ValueError("E-Mail must be unique")
        return value
