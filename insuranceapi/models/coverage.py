from django.db import models


class Coverage(models.Model):

    type = models.CharField(max_length=200)
