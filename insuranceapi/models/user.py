from django.db import models


class User(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    uid = models.CharField(max_length=50)
    address = models.Charfield(max_length=254)
    phone_number = models.CharField(max_length=20)
    profile_image_url = models.URLField(max_langth=200)
