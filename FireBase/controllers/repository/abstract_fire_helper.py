from abc import ABC, abstractmethod

from Utils.entities.Value_Objects import UUID


class AbstractFireBaseHelper(ABC):
    @abstractmethod
    def create_user(self, email, password) -> "UUID":
        """
        Function for creating firebase user.
        :param email: str
        :param password: str
        :return: str
        """

    @abstractmethod
    def change_user_password(self, new_password, uid):
        """
        Function for changing password of firebase user.
        """

    @abstractmethod
    def change_user_email(self, uid, new_email):
        """
        Function for change email of firebase user.
        """

    @abstractmethod
    def delete_user(self, uid):
        """
        Function for deleting firebase user.
        """

    @abstractmethod
    def login_by_email(self, email, password):
        """
        Function for login firebase user.
        """

    @abstractmethod
    def logout(self, uid) -> bool:
        """
        """