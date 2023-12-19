from abc import ABC, abstractmethod
from typing import Sequence, Union
from uuid import UUID

from User.Entities.User_Entity import UserEntity
from User.Repositories.Abstract_User_Repository import AbstractUserRepository
from User.Repositories.User_Repository import UserRepository


class AbstractUserInteractor(ABC):
    repository: AbstractUserRepository = None

    @abstractmethod
    def __init__(self, repository: AbstractUserRepository):
        """"""


class UserInteractor(AbstractUserInteractor):
    def __init__(self, repository=UserRepository()):
        self.repository = repository


class GetUserByIDInteractor(UserInteractor):
    def execute(self, User_uid: UUID) -> Union[UserEntity, Exception]:
        return self.repository.get_by_id(User_uid=User_uid)


class GetAllUserListInteractor(UserInteractor):
    def execute(self) -> Union[Sequence[UserEntity], Exception]:
        return self.repository.get_all()


class InsertUserInteractor(UserInteractor):
    def execute(self, user_obj: UserEntity) -> Union[UserEntity, Exception]:
        return self.repository.insert(user_obj=user_obj)


class UpdateUserInteractor(UserInteractor):
    def execute(self, user_obj: UserEntity) -> Union[UserEntity, Exception]:
        return self.repository.update(user_obj=user_obj)


class DeleteUserInteractor(UserInteractor):
    def execute(self, User_uid: UUID) -> None:
        return self.repository.delete(User_uid=User_uid)
