import pytest
from pydantic import ValidationError

from ..Entities.user_entity import UserEntity
from ..Exceptions.mobile_number import InvalidMobileNumberException


def test_user_create():
    user = UserEntity(
        display_name="test",
        email="xyz@example.com",
        mobile="+25499919191919",
        photo_url="user",
    )

    assert user
    assert user.display_name == "test"
    assert user.email == "xyz@example.com"
    assert user.mobile == "+25499919191919"
    assert user.photo_url == "user"


def test_user_create_throws_invalid_email_exception():
    with pytest.raises(ValidationError) as exc:
        UserEntity(
            display_name="test1",
            email="xyz@exampl",
            mobile="+25499919191919",
            photo_url="user",
        )
    assert exc.value.errors()[0]["loc"][0] == "email"
    assert exc.value.errors()[0]["msg"] == "value is not a valid email address"


def test_user_create_throws_invalid_mobile_exception():
    with pytest.raises(InvalidMobileNumberException) as exc:
        UserEntity(
            display_name="test2",
            email="xyz@exampl",
            mobile="+25499919",
            photo_url="user",
        )
    assert isinstance(exc.value, InvalidMobileNumberException)
