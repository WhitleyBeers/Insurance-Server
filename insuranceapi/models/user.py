from django.db import models

class User(models.Model):
  
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10)
    profile_image_url = models.URLField(max_length=254)
    uid = models.CharField(max_length=50)
