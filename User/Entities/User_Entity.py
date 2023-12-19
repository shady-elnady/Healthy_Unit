from pydantic import BaseModel, UUID4, EmailStr, FileUrl, Field, field_validator
from pydantic_extra_types.phone_numbers import PhoneNumber
from datetime import datetime
from uuid import uuid4

# from typing_extensions import NotRequired
from typing import Optional

from Utils.Validators.Regex_Validators import RegexValidators
from Utils.Assets.messages import Messages
from User.models.User import User


class UserEntity(BaseModel):
    uid: UUID4 = Field(default_factory=lambda: uuid4())  # .hex)
    name: str = Field(pattern=RegexValidators.NAME_REGEX)
    display_name: str
    email: EmailStr
    national_id: str = Field(pattern=RegexValidators.NATIONAL_ID_REGEX)
    phone_number: PhoneNumber = Field(pattern=RegexValidators.MY_PHONE_REGEX)
    password: str = Field(pattern=RegexValidators.PASSWORD_REGEX)
    photo_url: Optional[FileUrl]
    is_staff: bool = False
    is_superuser: bool = False
    is_active: bool = False
    is_verified: bool = False
    email_verified: bool = False
    phone_number_verified: bool = False
    disabled: bool = False
    last_login: datetime = None
    created_at: datetime
    last_updated: datetime

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

    @field_validator("name")
    @classmethod
    def name_validation(cls, value) -> str:
        if User.objects.filter(display_name=value).all():
            raise ValueError(Messages.NAME_UNIQUE_VALIDATION)
        if not RegexValidators.NAME_REGEX.match(value):
            raise ValueError(Messages.NAME_INVALID_VALIDATION)
        return value

    @field_validator("phone_number")
    @classmethod
    def phone_number_validation(cls, value) -> str:
        if not RegexValidators.MY_PHONE_REGEX.match(value):
            raise ValueError(Messages.PHONE_INVALID_VALIDATION)
        if User.objects.filter(phone_number=value).all():
            raise ValueError(Messages.PHONE_UNIQUE_VALIDATION)
        return value
