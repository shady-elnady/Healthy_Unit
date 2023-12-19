import pytest
from pytest_factoryboy import register

from ..Repository.FireBase_User_Repository import FireBaseUserRepository
from .factories import FireBaseUserFactory


register(FireBaseUserFactory, name="fire_user_factory")


@pytest.fixture
def user_repo():
    return FireBaseUserRepository()
