"""View module for handling requests about gamers"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Gamer


class GamerView(ViewSet):
    """Level up gamers view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized gamer
        """

        try:
            gamer = Gamer.objects.get(pk=pk)
            serializer = GamerSerializer(gamer)
            return Response(serializer.data)
        except Gamer.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all gamers
        Returns:
            Response -- JSON serialized list of gamers
        """

        gamers = Gamer.objects.all()
        serializer = GamerSerializer(gamers, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a gamer

        Returns:
        Response -- Empty body with 204 status code
        """

        gamer = Gamer.objects.get(pk=pk)
        gamer.uid = request.data["uid"]
        gamer.bio = request.data["bio"]

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        game = Gamer.objects.get(pk=pk)
        game.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class GamerSerializer(serializers.ModelSerializer):
    """JSON serializer for gamers
    """
    class Meta:
        model = Gamer
        fields = ('id', 'uid', 'bio')
