from django.db import models


class BusinessType(models.Model):

    label = models.CharField(max_length=100)
