from typing import Optional, Sequence
from uuid import UUID

from FireBase.Entities.FireBaseUser_Entity import FireBaseUserEntity
from .Abstract_FireBase_User import AbstractFireBaseUserRepository
from User.models.User import User as UserModel


class FireBaseUserRepository(AbstractFireBaseUserRepository):
    def update(self, fire_user_obj: FireBaseUserEntity) -> FireBaseUserEntity:
        UserModel.objects.filter(uid=fire_user_obj.uid).update(
            **fire_user_obj.model_dump()
        )
        user = UserModel.objects.get(uid=fire_user_obj.uid)
        return FireBaseUserEntity(**user.__dict__)

    def insert(self, fire_user_obj: FireBaseUserEntity) -> FireBaseUserEntity:
        user = UserModel.objects.create(**fire_user_obj.model_dump())
        return FireBaseUserEntity(**user.__dict__)

    def get_by_id(self, fire_User_uid: UUID) -> Optional[FireBaseUserEntity]:
        if user := UserModel.objects.filter(uid=fire_User_uid).first():
            return FireBaseUserEntity(**user.__dict__)
        else:
            return None

    def delete(self, fire_User_uid: UUID) -> None:
        UserModel.objects.get(uid=fire_User_uid).delete()

    def list(self) -> Optional[Sequence[FireBaseUserEntity]]:
        users = UserModel.objects.all()
        return [FireBaseUserEntity(**user.__dict__) for user in users]
