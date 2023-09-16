from businessapi.models import User
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
            'phone_number': user.phone_number,
            'image': user.image,
            'uid': user.uid
        }
        return Response(data)
    else:
        data = {'valid': False}
        return Response(data)


@api_view(['POST'])
def register_user(request):
    """handles the creation of a new user for authentication"""
    user = User.objects.create(
        email=request.data["email"],
        first_name=request.data["first_name"],
        last_name=request.data["last_name"],
        phone_number=request.data["phone_number"],
        image=request.data["image"],
        uid=request.data["uid"],
    )

    data = {
        'id': user.id,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'phone_number': user.phone_number,
        'image': user.image,
        'uid': user.uid
    }
    return Response(data)
