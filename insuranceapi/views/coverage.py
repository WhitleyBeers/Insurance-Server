"""View module for handling requests about coverage"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from insuranceapi.models import Coverage


class CoverageView(ViewSet):
    """Level up coverage view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single coverage
        Returns:
            Response -- JSON serialized coverage
        """
        coverage = Coverage.objects.get(pk=pk)
        serializer = CoverageSerializer(coverage)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all coverages
        Returns:
            Response -- JSON serialized list of coverages
        """

        coverages = Coverage.objects.all()
        serializer = CoverageSerializer(coverages, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
        Response -- JSON serialized Coverage instance
        """

        coverage = Coverage.objects.create(
            type=request.data["type"]
        )
        serializer = CoverageSerializer(coverage)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a Coverage

        Returns:
        Response -- Empty body with 204 status code
        """

        coverage = Coverage.objects.get(pk=pk)
        coverage.type = request.data["type"]
        coverage.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        coverage = Coverage.objects.get(pk=pk)
        coverage.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class CoverageSerializer(serializers.ModelSerializer):
    """JSON serializer for Coverages
    """

    class Meta:
        model = Coverage
        fields = ('id', 'type')
