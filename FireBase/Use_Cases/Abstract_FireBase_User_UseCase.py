from abc import ABC, abstractmethod
from uuid import UUID

from FireBase.Entities.FireBaseUser_Entity import FireBaseUserEntity


class AbstractFireBaseUserUseCase(ABC):
    @abstractmethod
    def get_by_id(self, user_uid: UUID):
        """ """

    @abstractmethod
    def insert(self, user: FireBaseUserEntity):
        """ """

    @abstractmethod
    def update(self, user: FireBaseUserEntity):
        """ """

    @abstractmethod
    def delete(self, user_uid: UUID):
        """ """

    @abstractmethod
    def list(self):
        """ """
