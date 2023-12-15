import pytest

from FireBase.Use_Case.base import AbstractUserUseCase
from .user_use_case import UserUseCase
from ..Domain.Entities.user_entity import UserEntity


pytestmark = pytest.mark.django_db


def test_create_customer_use_case(customer_factory, customer_repo: AbstractUserUseCase):
    customer_use_case = UserUseCase(customer_repo=customer_repo)
    customer_data = customer_factory.build()
    customer_entity = UserEntity(**customer_data.__dict__)
    customer = customer_use_case.insert(customer_entity)
    assert customer
    assert customer.display_name == customer_data.display_name
    assert customer.email == customer_data.email
    assert customer.phone == customer_data.phone


def test_update_customer_use_case(customer_factory, customer_repo: AbstractUserUseCase):
    customer_use_case = UserUseCase(customer_repo=customer_repo)
    customer_data = customer_factory()
    customer_entity = UserEntity(**customer_data.__dict__)
    customer_entity.display_name = "Test_1"
    customer_entity.last_name = "User_1"
    customer_entity.email = "abc@example.com"

    customer = customer_use_case.update(customer_entity)
    assert customer
    assert customer.display_name == "Test_1"
    assert customer.last_name == "User_1"
    assert customer.email == "abc@example.com"


def test_get_customer_use_case(customer_factory, customer_repo: AbstractUserUseCase):
    customer_use_case = UserUseCase(customer_repo=customer_repo)
    customer_data = customer_factory()
    customer = customer_use_case.get_by_id(customer_data.id)
    assert customer
    assert customer.display_name == customer_data.display_name
    assert customer.last_name == customer_data.last_name
    assert customer.email == customer_data.email


def test_list_customer_use_case(customer_factory, customer_repo: AbstractUserUseCase):
    customer_use_case = UserUseCase(customer_repo=customer_repo)
    customer_factory(phone="+9551370037")
    customer_factory(phone="+9551370038")
    customer_factory(phone="+9551370039")
    customer = customer_use_case.list()
    assert customer
    assert len(customer) == 3


def test_delete_customer_use_case(customer_factory, customer_repo: AbstractUserUseCase):
    customer_use_case = UserUseCase(customer_repo=customer_repo)

    customer_data = customer_factory()
    customer_use_case.delete(customer_data.id)

    customer = customer_use_case.get_by_id(customer_data.id)
    assert not customer
