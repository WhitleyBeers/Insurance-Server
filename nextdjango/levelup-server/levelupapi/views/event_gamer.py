"""View module for handling requests about event gamers"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import EventGamer


class EventGamerView(ViewSet):
    """Level up event gamers view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single event gamer
        Returns:
            Response -- JSON serialized event gamer
        """

        try:
            event_gamer = EventGamer.objects.get(pk=pk)
            serializer = EventGamerSerializer(event_gamer)
            return Response(serializer.data)
        except EventGamer.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all event gamers
        Returns:
            Response -- JSON serialized list of event gamers
        """

        event_gamers = EventGamer.objects.all()
        serializer = EventGamerSerializer(event_gamers, many=True)
        return Response(serializer.data)


class EventGamerSerializer(serializers.ModelSerializer):
    """JSON serializer for event gamers
    """
    class Meta:
        model = EventGamer
        fields = ('id', 'gamer', 'event')
