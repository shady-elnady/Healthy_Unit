from rest_framework.serializers import HyperlinkedModelSerializer, ListSerializer

from Employee.api.Serializer import EmployeeSerializer

from ..models import Vaccination, Campaign, VaccinationRecord

# Serializers define the API representation.


class VaccinationRecordSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = VaccinationRecord
        fields = [
            "url",
            "bar_code",
            "service",
            "patient",
            "diagnosis",
            "note",
            "content_type",
            "created_at",
            "last_updated",
        ]


class VaccinationSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Vaccination
        fields = [
            "url",
            "id",
            "name",
            "parent",
            "content_type",
            "translations",
            "created_at",
            "last_updated",
        ]


class CampaignSerializer(HyperlinkedModelSerializer):
    vaccination = VaccinationSerializer(many=False)
    managing_director = EmployeeSerializer(many=False)

    class Meta:
        model = Campaign
        fields = [
            "url",
            "id",
            "vaccination",
            "campaign_date",
        ]
