# serializers.py
from rest_polymorphic.serializers import PolymorphicSerializer
from Analysis.api.Serializer import AnalysisSerializer, ReportSerializer
from Radiology.api.Serializer import RadiologySerializer, RadiologySessionSerializer

from Service.api.Serializer import (
    ServiceRecordSerializer,
    ServiceSerializer,
    ParentServiceSerializer,
)
from Vaccination.api.Serializer import VaccinationRecordSerializer, VaccinationSerializer


class ServicePolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        "Service": ServiceSerializer,
        "ParentService": ParentServiceSerializer,
        "Radiology": RadiologySerializer,
        "Analysis": AnalysisSerializer,
        "Vaccination": VaccinationSerializer,
    }
    # resource_type_field_name = 'projecttype'


class ServiceRecordPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        "ServiceRecord": ServiceRecordSerializer,
        "RadiologySession": RadiologySessionSerializer,
        "VaccinationRecord": VaccinationRecordSerializer,
        "Report": ReportSerializer,
    }
    # resource_type_field_name = 'projecttype'
