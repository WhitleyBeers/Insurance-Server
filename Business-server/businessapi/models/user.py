from django.db import models


class User(models.Model):

    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    image = models.URLField(max_length=250)
    uid = models.CharField(max_length=50)
