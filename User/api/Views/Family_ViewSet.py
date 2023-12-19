from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import (
    TokenAuthentication,
    SessionAuthentication,
    BasicAuthentication,
)
from rest_framework.viewsets import ModelViewSet

from User.models.Family import Family
from ..Serializers.Family_Serializer import FamilySerializer


class FamilyViewSet(ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]
