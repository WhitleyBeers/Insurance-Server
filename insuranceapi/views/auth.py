from insuranceapi.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def check_user(request):
    """checks to see if User has associated account"""
    uid = request.data['uid']
    user = User.objects.filter(uid=uid).first()
    
    if user is not None:
        data = {
            'id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'address': user.address,
            'phone_number': user.phone_number,
            'profile_image_url': user.profile_image_url,
            'uid': user.uid
        }
        return Response(data)
    else:
        data = { 'valid': False }
        return Response(data)


@api_view(['POST'])
def register_user(request):
    """handles the creation of a new user for authentication"""
    user = User.objects.create(
        email = request.data["email"],
        first_name = request.data["firstName"],
        last_name = request.data["lastName"],
        address = request.data["address"],
        phone_number = request.data["phoneNumber"],
        profile_image_url = request.data["profileImageUrl"],
        uid = request.data["uid"],
    )
    
    data = {
        'id': user.id,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'address': user.address,
        'phone_number': user.phone_number,
        'profile_image_url': user.profile_image_url,
        'uid': user.uid
    }
    return Response(data)
