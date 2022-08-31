from unicodedata import name
from django.db import models
class Soda(models.Model):

    name = models.CharField(max_length=300)
    description = models.CharField(max_length=500)

