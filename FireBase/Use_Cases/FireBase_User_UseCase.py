from uuid import UUID

from FireBase.Repositories.Abstract_FireBase_User import AbstractFireBaseUserRepository
from FireBase.Entities.FireBaseUser_Entity import FireBaseUserEntity
from .Abstract_FireBase_User_UseCase import AbstractFireBaseUserUseCase


class FireBaseUserUseCase(AbstractFireBaseUserUseCase):
    def __init__(self, fire_user_repo: AbstractFireBaseUserRepository):
        self.fire_user_repo: AbstractFireBaseUserRepository = fire_user_repo

    def get_by_id(self, user_uid: UUID):
        return self.fire_user_repo.get_by_id(user_uid)

    def insert(self, user: FireBaseUserEntity):
        return self.fire_user_repo.insert(user)

    def update(self, user: FireBaseUserEntity):
        return self.fire_user_repo.update(user)

    def delete(self, user_uid: UUID):
        self.fire_user_repo.delete(user_uid)

    def list(self):
        return self.fire_user_repo.list()
