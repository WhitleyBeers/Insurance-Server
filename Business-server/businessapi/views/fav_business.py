from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from businessapi.models import FavBusiness, User
from businessapi.views.business import BusinessSerializer


class FavBusinessView(ViewSet):
    """Honey Buns View"""

    def retrieve(self, request, pk):
        """GET request for a single user"""
        try:
            fav_business = FavBusiness.objects.get(pk=pk)
            serializer = FavBusinessSerializer(fav_business)
            return Response(serializer.data)
        except FavBusiness.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """GET request for a list of users"""
        fav_businesses = FavBusiness.objects.all()
        uid = request.META['HTTP_AUTHORIZATION']
        user = User.objects.get(uid=uid)
        fav_businesses = fav_businesses.filter(user=user)
        serializer = FavBusinessSerializer(
            fav_businesses, many=True, context={'request': request})
        return Response(serializer.data)


class FavBusinessSerializer(serializers.ModelSerializer):
    """JSON serializer for categories"""
    business = BusinessSerializer()

    class Meta:
        model = FavBusiness
        fields = ('id', 'business', 'user')
        depth = 1
