from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from insuranceapi.models import Policy, User, Coverage, PolicyCoverage
from insuranceapi.serializers import PolicyCoverageSerializer


class PolicyView(ViewSet):
    """Policy View"""

    def retrieve(self, request, pk):
        """get single"""
        try:
            policy = Policy.objects.get(pk=pk)
            serializer = PolicySerializer(policy)
            return Response(serializer.data)

        except Policy.DoesNotExist as ex:
            return Response({'message': ex.args[0]},
                            status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """get all"""
        policies = Policy.objects.all()
        serializer = PolicySerializer(policies, many=True)
        return Response(serializer.data)

    def create(self, request):
        """create"""

        user_id = User.objects.get(pk=request.data["user_id"])

        policy = Policy.objects.create(
            company=request.data["company"],
            vehicle=request.data["vehicle"],
            user_id=user_id
        )
        serializer = PolicySerializer(policy)
        return Response(serializer.data)

    def update(self, request, pk):
        """update"""
        policy = Policy.objects.get(pk=pk)
        policy.company = request.data["company"]
        policy.vehicle = request.data["vehicle"]

        user_id = User.objects.get(pk=request.data["userId"])
        policy.user_id = user_id
        policy.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """delete"""

        policy = Policy.objects.get(pk=pk)
        policy.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    @action(methods=['post'], detail=True)
    def addcoverage(self, request, pk):
        """post request to add coverage to policy"""
        coverage = Coverage.objects.get(id=request.data["coverageId"])
        policy = Policy.objects.get(pk=pk)
        policy_coverage = PolicyCoverage.objects.create(
            coverage_id = coverage,
            policy_id = policy
        )
        return Response({'message': 'Coverage added to policy'}, status=status.HTTP_201_CREATED)
    
    @action(methods=['delete'], detail=True)
    def deletecoverage(self, request, pk):
        """delete request to delete coverage from policy"""
        policy_coverage = PolicyCoverage.objects.get(id=request.data["policyCoverageId"])
        policy_coverage = PolicyCoverage.objects.get(
            id = policy_coverage.id
        )
        policy_coverage.delete()
        return Response({'message': 'Coverage removed from policy'}, status=status.HTTP_204_NO_CONTENT)


class PolicySerializer(serializers.ModelSerializer):
    """policy serializer"""
    coverages = PolicyCoverageSerializer(many=True, read_only=True, source='policy_coverage')
    class Meta:
        model = Policy
        fields = ('id', 'user_id', 'company', 'vehicle', 'coverages')
