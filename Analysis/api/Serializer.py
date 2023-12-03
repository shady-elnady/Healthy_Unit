from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField

from User.api.Serializers.profile_serializer import ProfileSerializer

from ..models import Analysis, Report

# Serializers define the API representation.


class AnalysisSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Analysis
        fields = [
            "url",
            "id",
            "name",
            "parent",
            "symbol",
            "min_normal",
            "max_normal",
            "unit",
            "translations",
            "content_type",
            "created_at",
            "last_updated",
        ]


class ReportSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Report
        fields = [
            "url",
            "bar_code",
            "service",
            "patient",
            "diagnosis",
            "note",
            "content_type",
            "result",
            "neg_or_pos",
            "description_level",
            "created_at",
            "last_updated",
        ]
