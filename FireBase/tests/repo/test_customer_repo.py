import pytest

from ...Domain.Entities.user_entity import UserEntity

pytestmark = pytest.mark.django_db


def test_customer_repository_insert(customer_factory, customer_repo):
    customer_data = customer_factory.build()
    customer_entity = UserEntity(**customer_data.__dict__)
    customer_repo.insert(customer_entity)
    customer_obj = customer_repo.get_by_id(customer_entity.id)
    assert customer_obj.id == customer_entity.id


def test_customer_repository_get_by_id(customer_factory, customer_repo):
    customer_data = customer_factory()
    customer = customer_repo.get_by_id(customer_data.id)
    assert customer
    assert customer.id == customer_data.id
    assert customer.email == customer_data.email


def test_customer_repository_update(customer_factory, customer_repo):
    customer_data = customer_factory()
    assert customer_data.first_name != "Test_1"
    assert customer_data.last_name != "User_1"
    assert customer_data.email != "abc@example.com"

    customer_entity = UserEntity(**customer_data.__dict__)
    customer_entity.first_name = "Test_1"
    customer_entity.last_name = "User_1"
    customer_entity.email = "abc@example.com"

    customer = customer_repo.update(customer_entity)
    assert customer
    assert customer.id == customer_entity.id
    assert customer.first_name == "Test_1"
    assert customer_entity.last_name == "User_1"
    assert customer_entity.email == "abc@example.com"


def test_customer_repository_delete(customer_factory, customer_repo):
    customer_data = customer_factory()
    customer_repo.delete(customer_data.id)
    customer = customer_repo.get_by_id(customer_data.id)
    assert not customer


def test_customer_repository_list(customer_factory, customer_repo):
    customer_factory(phone="+9551370037")
    customer_factory(phone="+9551370038")
    customer_factory(phone="+9551370039")

    customers = customer_repo.list()
    assert customers
    assert len(customers) == 3
