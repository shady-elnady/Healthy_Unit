import pytest
from pytest_factoryboy import register

from ..Repository.user_repository import UserRepository
from .factories import UserFactory


register(UserFactory, name="user_factory")


@pytest.fixture
def user_repo():
    return UserRepository()
