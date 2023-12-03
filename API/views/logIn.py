from django.contrib.auth import authenticate, login, logout
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

from API.api.Serializers.LogIn import LogInSerializer

# # Create your views here.

User = get_user_model()


class LogIn(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LogInSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        national_id = str(request.data["national_id"])
        password = str(request.data["password"])
        try:
            user = User.objects.filter(national_id=national_id).first()
            if user is None:
                return Response(
                    {
                        "success": False,
                        "message": "User Not Found",
                        "status": status.HTTP_400_BAD_REQUEST,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            elif (user is not None) and (not user.check_password(password)):
                return Response(
                    {
                        "success": False,
                        "message": "Password Wrong",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            else:
                if not user.is_verified:
                    return Response(
                        {
                            "success": False,
                            "message": "Please Verfy Your Account",
                        },
                        status=status.HTTP_426_UPGRADE_REQUIRED,
                    )
                # login(request, user=user)
                token, _ = Token.objects.get_or_create(user=user)
                if not user.is_active:
                    user.is_active = True
                    user.save()
                return Response(
                    {
                        "success": True,
                        "message": "User logged successfully",
                        "token": token.key,
                        "data": {
                            "user_id": user.id,
                        },
                    },
                    status=status.HTTP_200_OK,
                )
        except Exception as e:
            return Response(
                {
                    "success": False,
                    "message": f"Error is {e}, with type {type(e)}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
