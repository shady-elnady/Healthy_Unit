from abc import ABC, abstractmethod
from typing import Optional, Sequence

from ..Domain.Entities.user_entity import UserEntity


class AbstractUserRepository(ABC):
    @abstractmethod
    def insert(self, user: UserEntity) -> Optional[UserEntity]:
        """ """

    @abstractmethod
    def update(self, user: UserEntity) -> UserEntity:
        """ """

    @abstractmethod
    def get_by_id(self, user_id) -> Optional[UserEntity]:
        """ """

    @abstractmethod
    def delete(self, user_id):
        """ """

    @abstractmethod
    def list(self) -> Optional[Sequence[UserEntity]]:
        """ """
