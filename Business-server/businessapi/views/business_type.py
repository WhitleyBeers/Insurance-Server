"""View module for handling requests about business types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from businessapi.models import BusinessType


class BusinessTypeView(ViewSet):
    """ business types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single business type
        Returns:
            Response -- JSON serialized business type
        """

        try:
            business_type = BusinessType.objects.get(pk=pk)
            serializer = BusinessTypeSerializer(business_type)
            return Response(serializer.data)
        except BusinessType.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all business types
        Returns:
            Response -- JSON serialized list of business types
        """

        business_types = BusinessType.objects.all()
        serializer = BusinessTypeSerializer(business_types, many=True)
        return Response(serializer.data)


class BusinessTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for business types
    """
    class Meta:
        model = BusinessType
        fields = ('id', 'label')
