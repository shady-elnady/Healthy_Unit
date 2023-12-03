from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from django.utils.translation import gettext_lazy as _

from rest_framework.response import Response
from django.contrib.auth import get_user_model

from django.contrib.auth import login
from rest_framework import permissions, generics, status, serializers
from rest_framework.authtoken.models import Token

# from django.views.decorators.csrf import csrf_exempt
from .Serializers.Register import RegisterSerializer

# Create your views here.


class RegisterViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    # @csrf_exempt
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                "data": serializer.data,
                "success": True,
                "message": _("User created successfully. You Can LogIn now"),
            },
            status=status.HTTP_201_CREATED,
        )

    # def get_queryset(self):
    #     raise serializers.ValidationError(_("This URL To Register "))
