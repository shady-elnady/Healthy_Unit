from typing import Optional, Sequence, Union
from uuid import UUID

from .Abstract_User_Repository import AbstractUserRepository
from User.Entities.User_Entity import UserEntity
from User.models.User import User as UserModel


class UserRepository(AbstractUserRepository):
    def get_by_id(self, User_uid: UUID) -> Union[UserEntity, Exception]:
        try:
            if user := UserModel.objects.filter(uid=User_uid).first():
                return UserEntity(**user.__dict__)
            else:
                return None
        except Exception as e:
            return e

    def get_all(self) -> Union[Sequence[UserEntity], Exception]:
        try:
            return [UserEntity(**user.__dict__) for user in UserModel.objects.all()]
        except Exception as e:
            return e

    def insert(self, user_obj: UserEntity) -> Union[UserEntity, Exception]:
        try:
            return UserEntity(
                **UserModel.objects.create(**user_obj.model_dump()).__dict__,
            )
        except Exception as e:
            return e
        
    def update(self, user_obj: UserEntity) -> Union[UserEntity, Exception]:
        try:
            UserModel.objects.filter(uid=user_obj.uid).update(
                **user_obj.model_dump()
            )
            return UserEntity(
                **UserModel.objects.get(
                    uid=user_obj.uid,
                ).__dict__,
            )
        except Exception as e:
            return e

    def delete(self, User_uid: UUID) -> None:
        UserModel.objects.get(uid=User_uid).delete()
