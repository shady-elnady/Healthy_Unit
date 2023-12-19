import uuid
from requests import Response
from rest_framework.views import APIView
from rest_framework import status

from FireBase.Domain.Entities.FireBaseUser_Entity import UserEntity
from FireBase.Repository.FireBase_User_Repository import UserRepository
from FireBase.Use_Case.FireBase_User_UseCase import UserUseCase
from .User_Serializers import UserCreateSerializer


class UserAPIView(APIView):
    def post(self, request):
        user_serializer = UserCreateSerializer(data=request.data)
        if not user_serializer.is_valid():
            return Response(
                user_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
        user_entity = UserEntity(**user_serializer.validated_data)
        user_repo = UserRepository()
        user = UserUseCase(user_repo).insert(user_entity)
        return Response(
            user.model_dump(),
            status=status.HTTP_201_CREATED,
        )

    def put(self, request, user_uid: uuid.UUID):
        user_repo = UserRepository()
        user = UserUseCase(user_repo).get_by_id(user_uid)
        if not user:
            return Response(
                {"message": "User with that Id Doesnot exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            user_serializer = UserCreateSerializer(data=request.data)
            if not user_serializer.is_valid():
                return Response(
                    user_serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST,
                )
            user_entity = UserEntity(**user_serializer.validated_data)
            user_entity.id = user.id
            user_repo = UserRepository()
            user = UserUseCase(user_repo).update(user_entity)
            return Response(
                user.model_dump(),
                status=status.HTTP_200_OK,
            )

    def get(self, request, user_uid: uuid.UUID=None):
        user_repo = UserRepository()
        if not user_uid:
            if users := UserUseCase(user_repo).list():
                users_dict = [user.__dict__ for user in users]
            else:
                users_dict = {}
            return Response(
                {
                    "message": users_dict,
                },
                status=status.HTTP_200_OK,
            )
        else:
            if user := UserUseCase(user_repo).get_by_id(user_uid):
                return Response(
                    user.model_dump(),
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"message": "user with that Id DoesNot exist"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
