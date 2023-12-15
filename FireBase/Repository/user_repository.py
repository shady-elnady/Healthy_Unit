from typing import Optional, Sequence
from .base_user import AbstractUserRepository

from User.models.User import User
from ..Domain.Entities.user_entity import UserEntity


class UserRepository(AbstractUserRepository):
    def update(self, obj: UserEntity) -> UserEntity:
        User.objects.filter(uid=obj.uid).update(**obj.dict())
        user = User.objects.get(uid=obj.uid)
        return UserEntity(**user.__dict__)

    def insert(self, obj: UserEntity) -> UserEntity:
        user = User.objects.create(**obj.model_dump())
        return UserEntity(**user.__dict__)

    def get_by_id(self, User_uid) -> Optional[UserEntity]:
        if user := User.objects.filter(uid=User_uid).first():
            return UserEntity(**user.__dict__)
        else:
            return None

    def delete(self, User_uid) -> None:
        User.objects.get(uid=User_uid).delete()

    def list(self) -> Optional[Sequence[UserEntity]]:
        users = User.objects.all()
        return [UserEntity(**user.__dict__) for user in users]
