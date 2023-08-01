from django.db import models
from .user import User


class Policy(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=200)
    vehicle = models.CharField(max_length=200)
