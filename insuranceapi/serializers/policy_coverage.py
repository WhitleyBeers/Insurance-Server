from rest_framework import serializers
from insuranceapi.models import PolicyCoverage, Coverage
from insuranceapi.views.coverage import CoverageSerializer


class PolicyCoverageSerializer(serializers.ModelSerializer):
    """Json serializer for policy coverages"""
    class Meta:
        model = PolicyCoverage
        fields = ('coverage_id', )
        depth = 1
