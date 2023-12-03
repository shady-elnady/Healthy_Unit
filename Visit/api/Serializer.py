from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField

from Doctor.api.Serializer import DoctorSerializer
from User.api.Serializers.profile_serializer import ProfileSerializer
from VitalSign.api.Serializer import VitalSignSerializer

from ..models import Visit, VisitVitalSign

# Serializers define the API representation.


class VisitSerializer(HyperlinkedModelSerializer):
    doctor = DoctorSerializer(many=False)
    patient = ProfileSerializer(many=False)

    class Meta:
        model = Visit
        fields = [
            "url",
            "id",
            "doctor",
            "patient",
            "diagnosis",
            "created_at",
            "last_updated",
        ]


class VisitVitalSignSerializer(HyperlinkedModelSerializer):
    visit = VisitSerializer(many=False)
    vital_sign = VitalSignSerializer(many=False)

    class Meta:
        model = VisitVitalSign
        fields = [
            "url",
            "id",
            "visit",
            "vital_sign",
            "result",
            "neg_or_pos",
            "description_level",
        ]
