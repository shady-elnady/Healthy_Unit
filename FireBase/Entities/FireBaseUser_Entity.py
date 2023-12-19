from pydantic import BaseModel, UUID4, EmailStr, FileUrl, Field, field_validator
from pydantic_extra_types.phone_numbers import PhoneNumber
from uuid import uuid4
# from typing_extensions import NotRequired
from typing import Optional

from Utils.Validators.Regex_Validators import RegexValidators
from Utils.Assets.messages import Messages
from User.models.User import User


class FireBaseUserEntity(BaseModel):
    uid: UUID4 = Field(default_factory=lambda: uuid4())  # .hex)
    display_name: str
    email: EmailStr
    phone_number: PhoneNumber = Field(pattern=RegexValidators.MY_PHONE_REGEX)
    password: str = Field(pattern=RegexValidators.PASSWORD_REGEX)
    photo_url: Optional[FileUrl]
    email_verified: bool = False
    disabled: bool = False

    @field_validator("email")
    @classmethod
    def email_validation(cls, value) -> EmailStr:
        if User.objects.filter(email=value).all():
            raise ValueError(Messages.EMAIL_UNIQUE_VALIDATION)
        if not RegexValidators.EMAIL_REGEX.match(value):
            raise ValueError(Messages.EMAIL_INVALID_VALIDATION)
        return value

    @field_validator("password")
    @classmethod
    def password_validation(cls, value) -> str:
        if not RegexValidators.PASSWORD_REGEX.match(value):
            raise ValueError(Messages.PASSWORD_INVALID_VALIDATION)
        return value

    @field_validator("display_name")
    @classmethod
    def display_name_validation(cls, value) -> str:
        if User.objects.filter(display_name=value).all():
            raise ValueError(Messages.NAME_UNIQUE_VALIDATION)
        return value

    @field_validator("phone_number")
    @classmethod
    def phone_number_validation(cls, value) -> str:
        if not RegexValidators.MY_PHONE_REGEX.match(value):
            raise ValueError(Messages.PHONE_INVALID_VALIDATION)
        if User.objects.filter(phone_number=value).all():
            raise ValueError(Messages.PHONE_UNIQUE_VALIDATION)
        return value
