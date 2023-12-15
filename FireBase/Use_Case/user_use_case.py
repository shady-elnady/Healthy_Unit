import uuid

from .base import AbstractUserUseCase
from ..Repository.base_user import AbstractUserRepository
from ..Domain.Entities.user_entity import UserEntity


class UserUseCase(AbstractUserUseCase):
    def __init__(self, user_repo: AbstractUserRepository):
        self.repo: AbstractUserRepository = user_repo

    def get_by_id(self, user_uid: uuid.UUID):
        return self.repo.get_by_id(user_uid)

    def insert(self, user: UserEntity):
        return self.repo.insert(user)

    def update(self, user: UserEntity):
        return self.repo.update(user)

    def delete(self, user_uid: uuid.UUID):
        self.repo.delete(user_uid)

    def list(self):
        return self.repo.list()
