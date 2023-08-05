from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from insuranceapi.serializers import UserSerializer, CreateUserSerializer
from insuranceapi.models import User

class UserView(ViewSet):
    """Insurance API Users"""
    def retrieve(self, request, pk):
        """GET request for a single user"""
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
      
    def list(self, request):
        """GET request for a list of users"""
        users = User.objects.all()
        serializer = UserSerializer(users, many=True, context={'request': request})
        return Response(serializer.data)
      
    # def create(self, request):
    #     """POST request to create a user"""
    #     uid = request.META["HTTP_AUTHORIZATION"]
    #     serializer = CreateUserSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(uid=uid)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def update(self, request, pk):
        """PUT request to update a user"""
        user = User.objects.get(pk=pk)
        user.email = request.data['email']
        user.first_name = request.data['firstName']
        user.last_name = request.data['lastName']
        user.address = request.data['address']
        user.phone_number = request.data['phoneNumber']
        user.profile_image_url = request.data['profileImageUrl']
        user.save()
        return Response({'message': 'User updated'}, status=status.HTTP_204_NO_CONTENT)
      
    def destroy(self, request, pk):
        """DELETE request to destroy a user"""
        user = User.objects.get(pk=pk)
        user.delete()
        return Response({'message': 'User deleted'}, status=status.HTTP_204_NO_CONTENT)
