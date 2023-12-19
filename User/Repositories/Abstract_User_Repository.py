from abc import ABC, abstractmethod
from typing import Optional, Sequence, Union

from User.Entities.User_Entity import UserEntity


class AbstractUserRepository(ABC):
    @abstractmethod
    def get_by_id(self, user_id) -> Union[UserEntity, Exception]:
        """ """

    @abstractmethod
    def get_all(self) -> Union[Sequence[UserEntity], Exception]:
        """ """

    @abstractmethod
    def insert(self, user: UserEntity) -> Union[UserEntity, Exception]:
        """ """

    @abstractmethod
    def update(self, user: UserEntity) -> Union[UserEntity, Exception]:
        """ """

    @abstractmethod
    def delete(self, user_id) -> None:
        """ """
