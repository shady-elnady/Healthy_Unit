import pytest
from pydantic import ValidationError

from ..Domain.Entities.FireBaseUser_Entity import FireBaseUserEntity
from Utils.Exceptions.api_exceptions import InvalidPhoneNumberException


def test_user_create():
    user = FireBaseUserEntity(
        display_name="test",
        email="xyz@example.com",
        phone_number="+25499919191919",
        photo_url="user",
    )

    assert user
    assert user.display_name == "test"
    assert user.email == "xyz@example.com"
    assert user.phone_number == "+25499919191919"
    assert user.photo_url == "user"


def test_user_create_throws_invalid_email_exception():
    with pytest.raises(ValidationError) as exc:
        FireBaseUserEntity(
            display_name="test1",
            email="xyz@exampl",
            phone_number="+25499919191919",
            photo_url="user",
        )
    assert exc.value.errors()[0]["loc"][0] == "email"
    assert exc.value.errors()[0]["msg"] == "value is not a valid email address"


def test_user_create_throws_invalid_phone_number_exception():
    with pytest.raises(InvalidPhoneNumberException) as exc:
        FireBaseUserEntity(
            display_name="test2",
            email="xyz@exampl",
            phone_number="+25499919",
            photo_url="user",
        )
    assert isinstance(exc.value, InvalidPhoneNumberException)
