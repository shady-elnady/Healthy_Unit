from abc import ABC, abstractmethod
import uuid

from FireBase.Domain.Entities.user_entity import UserEntity


class AbstractUserUseCase(ABC):
    @abstractmethod
    def get_by_id(self, user_uid: uuid.UUID):
        """ """

    @abstractmethod
    def insert(self, user: UserEntity):
        """ """

    @abstractmethod
    def update(self, user: UserEntity):
        """ """

    @abstractmethod
    def delete(self, user_uid: uuid.UUID):
        """ """

    @abstractmethod
    def list(self):
        """ """
