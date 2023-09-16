from django.db import models
from .business_type import BusinessType
from .user import User


class Business(models.Model):

    name = models.CharField(max_length=100)
    business_type = models.ForeignKey(BusinessType, on_delete=models.CASCADE)
    pitch = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    cost = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def favorited(self):
        """custom property to add favorite to a product"""
        return self.__favorited

    @favorited.setter
    def favorited(self, value):
        self.__favorited = value
