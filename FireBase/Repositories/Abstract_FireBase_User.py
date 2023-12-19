from abc import ABC, abstractmethod
from typing import Optional, Sequence

from FireBase.Entities.FireBaseUser_Entity import FireBaseUserEntity


class AbstractFireBaseUserRepository(ABC):
    @abstractmethod
    def insert(self, user: FireBaseUserEntity) -> Optional[FireBaseUserEntity]:
        """ """

    @abstractmethod
    def update(self, user: FireBaseUserEntity) -> FireBaseUserEntity:
        """ """

    @abstractmethod
    def get_by_id(self, user_id) -> Optional[FireBaseUserEntity]:
        """ """

    @abstractmethod
    def delete(self, user_id):
        """ """

    @abstractmethod
    def list(self) -> Optional[Sequence[FireBaseUserEntity]]:
        """ """
