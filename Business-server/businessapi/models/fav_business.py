from django.db import models
from .business import Business
from .user import User


class FavBusiness(models.Model):

    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
